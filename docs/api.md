# SewaSetu Chatbot: API Documentation & Website Integration Guide

This guide explains the architecture of the **SewaSetu RAG API**, the details of the endpoints, the functions handling conversation history, and the step-by-step process of integrating this chatbot into the actual SewaSetu Chhattisgarh website.

---

## 1. API Endpoints Reference

All API endpoints are hosted by FastAPI (running on port `8000` by default). Below is the details of each endpoint.

### A. List Services
* **URL**: `/api/services`
* **Method**: `GET`
* **Description**: Returns a clean JSON array of the 5 in-scope citizen services from the manifest, mapping serial numbers (`sno`) to target `service_id` keys.
* **Response Format**:
```json
[
  {
    "sno": "1",
    "service_id": "3",
    "name_en": "Marriage Registration",
    "name_hi": "विवाह पंजीकरण",
    "dept_en": "Urban Administration and Development Department",
    "dept_hi": "नगरीय प्रशासन एवं विकास विभाग",
    "is_internal": true
  }
]
```

### B. Get Service Details
* **URL**: `/api/services/{sno}`
* **Method**: `GET`
* **Parameters**:
  - `sno` (Path parameter): The serial number (`1` to `5`) of the service.
  - `lang` (Query parameter): Language preference (`en` or `hi`).
* **Description**: Returns the structured details (fees, time limits, required documents) of a service.
* **Response Format**:
```json
{
  "sno": "1",
  "service_id": "3",
  "name": "Marriage Registration",
  "department": "Urban Administration and Development Department",
  "time_limit": "15 days",
  "contact_details": "Sewa Setu Kendra",
  "fees": {
    "online_fee": "30.0",
    "kiosk_fee": "30.0",
    "raw_text": "Online Fee: 30.0, Kiosk Fee: 30.0"
  },
  "details_link": "https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=en",
  "required_documents_structured": [...],
  "required_documents": [...]
}
```

### C. Chatbot Interface
* **URL**: `/api/chat`
* **Method**: `POST`
* **Request Payload (`ChatRequest`)**:
```json
{
  "messages": [
    {"role": "user", "content": "marriage ki fees?"}
  ],
  "selected_sno": "1",
  "language": "hi",
  "detailed": true,
  "interactive": true,
  "is_option_click": false
}
```
* **Response Generation Safety (Grounding Guardrail):** Before returning a response, the backend routes the output through a zero-temperature grounding check (`verify_answer_grounding`). If the response contains any ungrounded facts, numbers, or rules that do not exist in the retrieved context, it is overridden with the fallback message.
* **Response Format Modes**:
  1. **Standard Text Mode** (`detailed=true`): Returns the answer and intermediate translation steps.
     ```json
     {
       "response": "Marriage registration ke liye fee ₹30.0 hai...",
       "query_lang": "hinglish",
       "english_query": "What is the fee for marriage registration?",
       "service_id": 3
     }
     ```
  2. **Interactivity / Options Mode**: Returns prompt options to guide the user.
     ```json
     {
       "mode": "options",
       "text": "Would you like to check your eligibility...",
       "options": [
         {"label": "📋 Check Eligibility via Document Checklist", "query": "Show required documents checklist for Marriage Registration"}
       ],
       "service_id": 3
     }
     ```
  3. **Interactive Document Checklist Mode**: Returns parsed mandatory and optional document groups.
     ```json
     {
       "mode": "interactive",
       "documents": {
         "groups": [
           {
             "id": "g1",
             "title": "Residential Proof",
             "mandatory": true,
             "anyOne": true,
             "docs": [
               {"id": "d1", "name": "Voters Identity Card", "mandatory": true}
             ]
           }
         ]
       },
       "service_id": 3
     }
     ```

### D. Service Classification Search
* **URL**: `/api/search`
* **Method**: `POST`
* **Request Payload**: `{"query": "caste certificate"}`
* **Description**: Matches raw user query to the correct service `sno` and `service_id` via a scalable **Two-Stage Routing** system:
  1. **Stage 1 (Semantic Search):** Generates query embeddings and calculates cosine similarity over candidate service descriptions to retrieve the Top 3 services.
  2. **Stage 2 (LLM Constrained Classification):** Prompts the LLM to select from these 3 candidates, returning the final `sno` and `service_id`.
* **Response Format**:
```json
{
  "sno": "2",
  "service_id": "4",
  "name": "SC/ST Certificate",
  "confidence": 0.95
}
```

### E. Health Check
* **URL**: `/health`
* **Method**: `GET`
* **Response**: `{"status": "ok", "llm": "sarvam"}`

---

## 2. Core Backend RAG & LLM Routing Functions

The backend coordinates context isolation, service switching, and output verification through these key functions inside `05_webui/backend/main.py` and `05_webui/backend/llm_router.py`:

1. **`sanitize_history(messages)`**: 
   Filters the incoming client messages, dropping empty content, special checklists, and system rules. It returns a sanitized list containing only `user` and `assistant` role dictionary exchanges.
2. **`classify_query_intent(query, history)`**:
   Analyzes the query in the context of the conversation history. It returns the detected intent (`greeting`, `farewell`, `thanks`, `identity`, `out_of_scope`, `follow_up`, `new_topic`), the `resolved_query` (vague follow-ups rewritten to self-contained queries), and a `topic_summary`.
3. **`classify_service(query, services_list, use_llm_only)`**:
   Leverages the **Two-Stage Retrieval Routing** process to dynamically map queries to correct service catalog IDs (1 to 5) when `intent == "new_topic"`.
4. **`verify_answer_grounding(context, response)`**:
   Grounding Guardrail. Executes a fast, zero-temperature completion call with Sarvam AI. Compares the generated response against the compiled context. Returns `True` if grounded, or `False` if it contains ungrounded factual details, enabling automatic fallback overrides.
5. **`build_condensed_history(sanitized_history, is_follow_up, topic_summary)`**:
   Prepares the history context for final response synthesis. Clears context (`[]`) on service switches to prevent context leakage, and returns only the last 1 turn on follow-ups to prevent historical magnification.
6. **`get_intent_response(intent, query)`**:
   Early interceptor. If the intent is greeting, farewell, thanks, identity, or out_of_scope, it returns the correct canned response in the user's language without executing the RAG pipeline or RAG database calls.

---

## 3. Integration Guide: Embedded Chatbot on Live Portal

To deploy this chatbot onto the actual **SewaSetu Chhattisgarh** portal, follow these steps:

### A. Deploying the Backend API
1. **Server Host**: Spin up a containerized instance of the Python backend (FastAPI) on your application server or cloud environment (e.g. AWS EC2, GCP Cloud Run, or Docker Swarm).
2. **Vector DB & Data**: Mount the vector store directory (`04_embeddings_and_kg/chroma_db/`) and metadata folder (`01_preprocessing/data/`) into your backend instance.

3. **Environment Variables**: Configure the `.env` file on the production server with the appropriate API keys:
   ```env
   SARVAM_API_KEY=your_production_sarvam_key
   PORT=8000
   ```
4. **Production Server Command**: Start FastAPI with high performance using `gunicorn` or `uvicorn`:
   ```bash
   uvicorn 05_webui.backend.main:app --host 0.0.0.0 --port 8000 --workers 4
   ```

### B. Embedding the Chatbot in the Portal Website (Frontend)
To show the chatbot in the SewaSetu Portal UI, embed a script in the portal's index page or lay out a dedicated widget.

#### 1. The Script Embed (Floating Widget)
Add a floating chat icon in the bottom-right corner of the website. Copy this template snippet into the website footer:
```html
<!-- SewaSetu Chatbot Container -->
<div id="sewasetu-chat-widget" class="collapsed">
  <button id="chat-toggle-btn" onclick="toggleChat()">💬 Chat with SewaSetu Assistant</button>
  <div id="chat-window" style="display: none;">
    <div class="chat-header">SewaSetu AI Assistant</div>
    <div id="chat-messages" class="chat-body"></div>
    <div class="chat-footer">
      <input type="text" id="chat-input" placeholder="Ask about services, fees, documents..."/>
      <button onclick="sendChatMessage()">Send</button>
    </div>
  </div>
</div>
```

#### 2. The API Connection Handler
Create a Javascript handler to manage message states, history sanitization, and API posting:
```javascript
let conversationHistory = [];
let currentServiceId = null; // Map this to the active tab/selection in portal sidebar

function getSelectedSno() {
  // Syncs with the website's active service tab serial number
  return window.activeServiceSno || null; 
}

async function sendChatMessage() {
  const inputEl = document.getElementById("chat-input");
  const queryText = inputEl.value.trim();
  if (!queryText) return;

  // Render user message in UI
  appendMessage("user", queryText);
  inputEl.value = "";

  // Append user message to history
  conversationHistory.push({ role: "user", content: queryText });
  
  // Frontend limits history to last 6 messages (3 turns)
  if (conversationHistory.length > 6) {
    conversationHistory = conversationHistory.slice(-6);
  }

  // API Call
  const response = await fetch("https://api.sewasetu.cg.gov.in/api/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      messages: conversationHistory,
      selected_sno: getSelectedSno(),
      language: detectUILanguage(), // Syncs with the website's language toggle
      interactive: true
    })
  });

  const data = await response.json();
  
  if (data.mode === "options") {
    renderOptionsButtons(data.text, data.options);
  } else if (data.mode === "interactive") {
    renderInteractiveChecklist(data.documents);
  } else {
    appendMessage("assistant", data.response);
    // Append assistant response to history
    conversationHistory.push({ role: "assistant", content: data.response });
  }
}
```

#### 3. Syncing Portal Context (Redirections & Tabs)
- **Automatic Redirect Links**: When the chatbot responds, it returns markdown links in the format `[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=X)`. Make sure the frontend captures click events on these markdown links to redirect the user to the portal's corresponding application page without page refreshes.
- **Sidebar Tab Integration**: When a citizen navigates the service pages on the portal (e.g. clicks Caste Certificate), set `window.activeServiceSno = "2"`. This sends the serial number to the chatbot dynamically so the assistant automatically answers caste-related queries, enabling a seamless co-browsing experience.
