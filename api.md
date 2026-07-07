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
* **Response Modes**:
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
* **Description**: Matches raw user query to the correct service `sno` and `service_id` via LLM classification.
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

## 2. Conversation History Functions

The backend coordinates context isolation and query resolution through these key functions inside `backend/main.py`:

1. **`sanitize_history(messages)`**: 
   Filters the incoming client messages. It drops empty content, ignores system messages, and returns a sanitized list containing only `user` and `assistant` role dictionary exchanges.
2. **`classify_query_intent(query, history)`**:
   Leverages the LLM router to analyze the query in the context of the conversation history. It returns the detected intent (`greeting`, `farewell`, `thanks`, `identity`, `out_of_scope`, `follow_up`, `new_topic`), the `resolved_query` (vague follow-ups rewritten to self-contained queries), and a `topic_summary`.
3. **`query_contains_service_keywords(query, resolved_query, service_id)`**:
   Validates service switches programmatically. If the LLM router mistakenly classifies a service switch query as a `follow_up`, this function detects new service keywords and overrides the intent to `new_topic` to avoid contaminating context.
4. **`build_condensed_history(sanitized_history, is_follow_up, topic_summary)`**:
   Prepares the history context for the final response synthesis:
   - For `new_topic` (service switch): Returns `[]` (clears context, preventing leakage).
   - For `follow_up`: Returns only the **last 1 turn (2 messages)** + a concise previous topic context summary to prevent historical context magnification.
5. **`get_intent_response(intent, query)`**:
   Early interceptor. If the intent is non-informational (greeting, farewell, thanks, identity, out_of_scope), it returns the correct canned response in the user's language without executing the RAG pipeline or RAG database calls.

---

## 3. Integration Guide: Embedded Chatbot on Live Portal

To deploy this chatbot onto the actual **SewaSetu Chhattisgarh** portal, follow these steps:

### A. Deploying the Backend API
1. **Server Host**: Spin up a containerized instance of the Python backend (FastAPI) on your application server or cloud environment (e.g. AWS EC2, GCP Cloud Run, or Docker Swarm).
2. **Vector DB & Data**: Mount the vector store directory (`chroma_db/`) and metadata folder (`data/`) into your backend instance.
3. **Environment Variables**: Configure the `.env` file on the production server with the appropriate API keys:
   ```env
   SARVAM_API_KEY=your_production_sarvam_key
   PORT=8000
   ```
4. **Production Server Command**: Start FastAPI with high performance using `gunicorn` or `uvicorn`:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
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
