import { useState, useEffect, useRef } from 'react';
import './App.css';

// Translation dictionary for English and Hindi support
const translations = {
  en: {
    brand_title: "SewaSetu RAG",
    brand_sub: "AI Sahayak",
    search_placeholder: "Search services or ID...",
    directory_title: "Services Directory",
    online_agent: "Online RAG Agent",
    welcome_title: "Welcome to SewaSetu RAG Assistant",
    welcome_desc: "Ask me anything about CG citizen services, document list, kiosk fees, or timelines. Click any service on the left to view its details instantly.",
    input_placeholder: "Ask about documents, fees, rules...",
    send: "Send",
    service_details: "Service Details",
    service_name: "Service Name",
    department: "Department",
    time_limit: "Time Limit (SLA)",
    contact_authority: "Contact Authority",
    fee_info: "Fee Information",
    online_fee: "Online Portal Fee",
    kiosk_fee: "Kiosk Center Fee",
    apply_link: "Apply Link",
    apply_desc: "This is an internal service. You can login and apply on the Sewa Setu portal.",
    apply_btn: "Go to Sewa Setu Portal",
    required_docs: "Required Documents",
    form_fields: "Application Form Fields",
    mandatory: "Mandatory",
    optional: "Optional",
    internal: "Internal",
    external: "External",
    error_fetch: "Error loading service catalog.",
    error_chat: "Error getting response from local LLM. Please make sure Ollama is running.",
    error_details: "Error loading service details."
  },
  hi: {
    brand_title: "सेवासेतु RAG",
    brand_sub: "एआई सहायक",
    search_placeholder: "सेवाएं या आईडी खोजें...",
    directory_title: "सेवाएं निर्देशिका",
    online_agent: "ऑनलाइन आरएजी एजेंट",
    welcome_title: "सेवासेतु आरएजी सहायक में आपका स्वागत है",
    welcome_desc: "छत्तीसगढ़ नागरिक सेवाओं, आवश्यक दस्तावेजों की सूची, कियोस्क शुल्क या समय सीमा के बारे में कुछ भी पूछें। विवरण देखने के लिए बाईं ओर किसी भी सेवा पर क्लिक करें।",
    input_placeholder: "दस्तावेजों, शुल्कों, नियमों के बारे में पूछें...",
    send: "भेजें",
    service_details: "सेवा का विवरण",
    service_name: "सेवा का नाम",
    department: "विभाग",
    time_limit: "समय सीमा (SLA)",
    contact_authority: "संपर्क प्राधिकारी",
    fee_info: "शुल्क की जानकारी",
    online_fee: "ऑनलाइन पोर्टल शुल्क",
    kiosk_fee: "कियोस्क केंद्र शुल्क",
    apply_link: "आवेदन लिंक",
    apply_desc: "यह एक आंतरिक सेवा है। आप लॉग इन करके सेवा सेतु पोर्टल पर आवेदन कर सकते हैं।",
    apply_btn: "सेवा सेतु पोर्टल पर जाएं",
    required_docs: "आवश्यक दस्तावेज़",
    form_fields: "आवेदन पत्र के फ़ील्ड",
    mandatory: "अनिवार्य",
    optional: "वैकल्पिक",
    internal: "आंतरिक",
    external: "बाहरी",
    error_fetch: "सेवा सूची लोड करने में त्रुटि।",
    error_chat: "स्थानीय एलएलएम से उत्तर प्राप्त करने में त्रुटि। कृपया सुनिश्चित करें कि ओलामा चल रहा है।",
    error_details: "सेवा विवरण लोड करने में त्रुटि।"
  }
};

function parseMarkdown(text) {
  if (!text) return null;
  const lines = text.split('\n');
  let inList = false;
  let listItems = [];
  const elements = [];

  const parseInline = (str) => {
    if (!str) return str;
    // Split by markdown links [Text](URL)
    const linkParts = str.split(/(\[.*?\]\(.*?\))/g);
    return linkParts.map((part, index) => {
      if (index % 2 === 1) {
        const match = part.match(/\[(.*?)\]\((.*?)\)/);
        if (match) {
          const btnText = match[1];
          const btnUrl = match[2];
          return (
            <a 
              key={`link-${index}`} 
              href={btnUrl} 
              target="_blank" 
              rel="noreferrer" 
              className="chat-apply-btn"
              style={{
                display: 'inline-flex',
                alignItems: 'center',
                justifyContent: 'center',
                padding: '6px 14px',
                backgroundColor: 'var(--primary-green, #10b981)',
                color: '#ffffff',
                borderRadius: '4px',
                fontSize: '13px',
                fontWeight: '600',
                textDecoration: 'none',
                marginTop: '8px',
                marginBottom: '4px',
                boxShadow: 'var(--shadow-sm)',
                transition: 'all 0.2s ease',
                cursor: 'pointer'
              }}
            >
              {btnText}
            </a>
          );
        }
      }
      
      // Parse bold text **Text**
      const boldParts = part.split(/\*\*(.*?)\*\*/g);
      return boldParts.map((bPart, bIndex) => {
        if (bIndex % 2 === 1) {
          return <strong key={`bold-${bIndex}`}>{bPart}</strong>;
        }
        return bPart;
      });
    });
  };

  lines.forEach((line, index) => {
    const trimmed = line.trim();
    if (trimmed.startsWith('- ') || trimmed.startsWith('* ')) {
      if (!inList) {
        inList = true;
        listItems = [];
      }
      listItems.push(<li key={`li-${index}`} style={{ marginLeft: '12px' }}>{parseInline(trimmed.substring(2))}</li>);
    } else if (trimmed.match(/^\d+\.\s/)) {
      if (!inList) {
        inList = true;
        listItems = [];
      }
      const itemText = trimmed.replace(/^\d+\.\s/, '');
      listItems.push(<li key={`li-${index}`} style={{ marginLeft: '12px' }}>{parseInline(itemText)}</li>);
    } else {
      if (inList) {
        elements.push(
          <ul key={`ul-${index}`} style={{ margin: '8px 0 12px 16px', paddingLeft: '12px', listStyleType: 'disc' }}>
            {listItems}
          </ul>
        );
        inList = false;
        listItems = [];
      }

      if (trimmed.startsWith('### ')) {
        elements.push(<h4 key={index} style={{ margin: '14px 0 6px', fontSize: '15px', fontWeight: 700 }}>{parseInline(trimmed.substring(4))}</h4>);
      } else if (trimmed.startsWith('## ')) {
        elements.push(<h3 key={index} style={{ margin: '16px 0 8px', fontSize: '16px', fontWeight: 700 }}>{parseInline(trimmed.substring(3))}</h3>);
      } else if (trimmed.startsWith('# ')) {
        elements.push(<h2 key={index} style={{ margin: '18px 0 10px', fontSize: '18px', fontWeight: 700 }}>{parseInline(trimmed.substring(2))}</h2>);
      } else if (trimmed) {
        elements.push(<p key={index} style={{ marginBottom: '8px' }}>{parseInline(line)}</p>);
      } else {
        elements.push(<div key={index} style={{ height: '8px' }}></div>);
      }
    }
  });

  if (inList) {
    elements.push(
      <ul key="ul-end" style={{ margin: '8px 0 12px 16px', paddingLeft: '12px', listStyleType: 'disc' }}>
        {listItems}
      </ul>
    );
  }

  return elements;
}

function App() {
  // Translation & Language
  const [lang, setLang] = useState('en');
  const t = translations[lang];

  // RAG / Portal States
  const [services, setServices] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedSno, setSelectedSno] = useState(null);
  const [details, setDetails] = useState(null);
  const [isDetailsLoading, setIsDetailsLoading] = useState(false);
  const [detailsPanelOpen, setDetailsPanelOpen] = useState(false);

  // Chatbot States
  const [chatMessages, setChatMessages] = useState([]);
  const [inputText, setInputText] = useState('');
  const [isChatLoading, setIsChatLoading] = useState(false);
  const [locationFlow, setLocationFlow] = useState(null);
  const [originalQuery, setOriginalQuery] = useState(null);
  const [activeServiceId, setActiveServiceId] = useState(null);
  const [locationName, setLocationName] = useState('');
  const [awaitingVenueInput, setAwaitingVenueInput] = useState(false);

  // References
  const messagesEndRef = useRef(null);

  // Load service catalog on mount
  useEffect(() => {
    fetch('/api/services')
      .then(res => res.json())
      .then(data => setServices(data))
      .catch(err => console.error(err));
  }, []);

  // Fetch service details on selectedSno change
  useEffect(() => {
    if (!selectedSno) {
      setDetails(null);
      return;
    }
    setIsDetailsLoading(true);
    fetch(`/api/services/${selectedSno}?lang=${lang}`)
      .then(res => res.json())
      .then(data => {
        setDetails(data);
        setDetailsPanelOpen(true);
      })
      .catch(err => console.error(err))
      .finally(() => setIsDetailsLoading(false));
  }, [selectedSno, lang]);

  // Scroll to bottom of chat
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [chatMessages, isChatLoading]);

  // Chat message submission
  const handleSendMessage = async (e) => {
    if (e) e.preventDefault();
    if (!inputText.trim() || isChatLoading) return;

    const query = inputText.trim();
    setInputText('');
    const newMessages = [...chatMessages, { role: 'user', content: query }];
    setChatMessages(newMessages);
    setIsChatLoading(true);

    let activeSno = selectedSno || activeServiceId;

    // Call search API only if not in location flow
    if (!locationFlow) {
      try {
        const searchRes = await fetch('/api/search', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ query, language: lang })
        });
        if (searchRes.ok) {
          const mapData = await searchRes.json();
          if (mapData.sno) {
            setSelectedSno(mapData.sno);
            activeSno = mapData.sno;
            setActiveServiceId(mapData.service_id);
          }
        }
      } catch (err) {
        console.warn(err);
      }
    }

    // Call chatbot endpoint
    try {
      const chatHeaders = { 'Content-Type': 'application/json' };

      const bodyPayload = {
        messages: newMessages,
        selected_sno: activeSno,
        language: lang
      };

      if (locationFlow) {
        bodyPayload.location_flow = locationFlow;
        bodyPayload.original_query = originalQuery;
      }

      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: chatHeaders,
        body: JSON.stringify(bodyPayload)
      });

      if (res.ok) {
        const data = await res.json();
        
        // Reset location flow state after text submit
        setLocationFlow(null);

        // Update active states
        if (data.original_query) {
          setOriginalQuery(data.original_query);
        }
        if (data.service_id) {
          setActiveServiceId(data.service_id);
        }

        const newMsg = { role: 'assistant', content: data.response || data.reply };
        if (data.options) {
          newMsg.options = data.options;
          newMsg.original_query = data.original_query;
          newMsg.service_id = data.service_id;
        }
        setChatMessages(prev => [...prev, newMsg]);
      } else {
        setChatMessages(prev => [...prev, { role: 'assistant', content: t.error_chat }]);
        setLocationFlow(null);
      }
    } catch (err) {
      setChatMessages(prev => [...prev, { role: 'assistant', content: t.error_chat }]);
      setLocationFlow(null);
    } finally {
      setIsChatLoading(false);
    }
  };

  const handleVenueSubmit = async () => {
    if (!locationName.trim() || isChatLoading) return;

    const typedLocation = locationName.trim();
    setLocationName('');
    setAwaitingVenueInput(false);

    const nextMessages = [...chatMessages, { role: 'user', content: typedLocation }];
    setChatMessages(nextMessages);
    setIsChatLoading(true);

    const activeSno = selectedSno || activeServiceId;

    try {
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          query: typedLocation,
          location_name: typedLocation,
          messages: nextMessages,
          selected_sno: activeSno,
          language: lang,
          location_flow: 'flow_location',
          original_query: originalQuery
        })
      });

      if (res.ok) {
        const data = await res.json();
        setLocationFlow(null);

        if (data.original_query) {
          setOriginalQuery(data.original_query);
        }
        if (data.service_id) {
          setActiveServiceId(data.service_id);
        }

        const newMsgObj = { role: 'assistant', content: data.response || data.reply };
        if (data.options) {
          newMsgObj.options = data.options;
          newMsgObj.original_query = data.original_query;
          newMsgObj.service_id = data.service_id;
        }

        setChatMessages(prev => [...prev, newMsgObj]);
      } else {
        setChatMessages(prev => [...prev, { role: 'assistant', content: t.error_chat }]);
        setLocationFlow(null);
      }
    } catch (err) {
      setChatMessages(prev => [...prev, { role: 'assistant', content: t.error_chat }]);
      setLocationFlow(null);
    } finally {
      setIsChatLoading(false);
    }
  };

  const handleOptionClick = async (option, messageIndex) => {
    // Disable option buttons
    setChatMessages(prev => prev.map((msg, idx) => {
      if (idx === messageIndex) {
        return { ...msg, disabled: true };
      }
      return msg;
    }));

    const userQuery = option.label;
    const flowValue = option.value;

    if (flowValue === 'flow_location') {
      const promptMsg = lang === 'hi'
        ? "कृपया अपने विवाह स्थल या क्षेत्र का नाम दर्ज करें (जैसे, ग्राम का नाम, रिज़ॉर्ट का नाम, क्षेत्र):"
        : "Please enter the name of your marriage venue or locality (e.g., village name, resort name, area):";

      setChatMessages(prev => [
        ...prev,
        { role: 'user', content: userQuery },
        { role: 'assistant', content: promptMsg }
      ]);
      setLocationFlow('flow_location');
      setAwaitingVenueInput(true);
      return;
    }

    const nextMessages = [...chatMessages, { role: 'user', content: userQuery }];
    setChatMessages(nextMessages);
    setIsChatLoading(true);

    const activeSno = selectedSno || activeServiceId;

    try {
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          query: userQuery,
          messages: nextMessages,
          selected_sno: activeSno,
          language: lang,
          location_flow: flowValue,
          original_query: originalQuery
        })
      });

      if (res.ok) {
        const data = await res.json();

        // Update active states
        if (data.original_query) {
          setOriginalQuery(data.original_query);
        }
        if (data.service_id) {
          setActiveServiceId(data.service_id);
        }

        const newMsgObj = { role: 'assistant', content: data.response || data.reply };
        if (data.options) {
          newMsgObj.options = data.options;
          newMsgObj.original_query = data.original_query;
          newMsgObj.service_id = data.service_id;
        }

        setChatMessages(prev => [...prev, newMsgObj]);
      } else {
        setChatMessages(prev => [...prev, { role: 'assistant', content: t.error_chat }]);
      }
    } catch (err) {
      setChatMessages(prev => [...prev, { role: 'assistant', content: t.error_chat }]);
    } finally {
      setIsChatLoading(false);
    }
  };

  // Filters for directory list
  const filteredServices = services.filter((srv) => {
    const query = searchQuery.toLowerCase().trim();
    if (!query) return true;
    return (
      (srv.name_en || '').toLowerCase().includes(query) ||
      (srv.name_hi || '').toLowerCase().includes(query) ||
      (srv.service_id || '').toString().includes(query)
    );
  });

  return (
    <div className="app-container">
      {/* SIDEBAR */}
      <aside className="sidebar">
        <div className="sidebar-header">
          <div className="brand">
            <h1>{t.brand_title}</h1>
            <div className="brand-subtitle">{t.brand_sub}</div>
          </div>

          <div className="lang-selector">
            <button className={`lang-btn ${lang === 'en' ? 'active' : ''}`} onClick={() => setLang('en')}>English</button>
            <button className={`lang-btn ${lang === 'hi' ? 'active' : ''}`} onClick={() => setLang('hi')}>हिंदी</button>
          </div>

          <div className="search-container">
            <input 
              type="text" 
              className="search-input" 
              placeholder={t.search_placeholder} 
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
            />
          </div>
        </div>

        <div className="services-list-container">
          <h2 className="directory-title">{t.directory_title} ({filteredServices.length})</h2>
          {filteredServices.map((srv) => (
            <div 
              key={srv.sno} 
              className={`service-item ${selectedSno === srv.sno ? 'active' : ''}`}
              onClick={() => setSelectedSno(srv.sno)}
            >
              <div className="service-dept">{lang === 'hi' ? srv.dept_hi : srv.dept_en}</div>
              <div className="service-name">{lang === 'hi' ? srv.name_hi : srv.name_en}</div>
              <div className="service-footer">
                <span className="service-id">ID: {srv.service_id}</span>
                <span className="badge internal">{srv.is_internal ? t.internal : t.external}</span>
              </div>
            </div>
          ))}
        </div>
      </aside>

      {/* CHAT PANEL */}
      <main className="chat-panel">
        <header className="chat-header">
          <div className="chat-header-info">
            <h2>{t.brand_title} {lang === 'hi' ? 'चैट सहायक' : 'Chat Assistant'}</h2>
            <div className="chat-status"><span className="status-dot"></span>{t.online_agent}</div>
          </div>
          {selectedSno && !detailsPanelOpen && (
            <button className="lang-btn" onClick={() => setDetailsPanelOpen(true)} style={{ width: 'auto', padding: '6px 12px' }}>
              {lang === 'hi' ? 'विवरण देखें' : 'View Details'}
            </button>
          )}
        </header>

        <div className="chat-messages">
          {chatMessages.length === 0 ? (
            <div className="welcome-container">
              <div className="welcome-icon-box">⚡</div>
              <h2>{t.welcome_title}</h2>
              <p>{t.welcome_desc}</p>
            </div>
          ) : (
            chatMessages.map((msg, index) => (
              <div key={index} className={`message-row ${msg.role}`}>
                <div className="message-bubble">
                  {msg.role === 'user' ? msg.content : parseMarkdown(msg.content)}
                  {msg.options && msg.options.length > 0 && (
                    <div className="message-options-container">
                      {msg.options.map((opt, oIdx) => (
                        <button
                          key={oIdx}
                          className="option-btn"
                          disabled={msg.disabled}
                          onClick={() => handleOptionClick(opt, index)}
                        >
                          {opt.label}
                        </button>
                      ))}
                    </div>
                  )}
                </div>
              </div>
            ))
          )}
          {isChatLoading && (
            <div className="message-row assistant">
              <div className="message-bubble" style={{ padding: '12px 20px' }}>
                <div className="typing-indicator">
                  <span className="typing-dot"></span>
                  <span className="typing-dot"></span>
                  <span className="typing-dot"></span>
                </div>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        <div className="chat-input-container">
          {awaitingVenueInput ? (
            <div className="venue-input-box" style={{ display: 'flex', gap: '8px', width: '100%', padding: '8px' }}>
              <input 
                type="text"
                className="search-input"
                style={{ flex: 1, margin: 0, padding: '10px 14px' }}
                placeholder={lang === 'hi' ? "विवाह स्थल या क्षेत्र का नाम दर्ज करें (उदा. ग्राम, रिसॉर्ट का नाम)..." : "Enter marriage venue or locality (e.g. resort name, village)..."}
                value={locationName}
                onChange={(e) => setLocationName(e.target.value)}
                onKeyDown={(e) => {
                  if (e.key === 'Enter') {
                    e.preventDefault();
                    handleVenueSubmit();
                  }
                }}
              />
              <button 
                type="button" 
                className="chat-send-btn" 
                style={{ borderRadius: '8px', padding: '0 16px' }}
                disabled={!locationName.trim() || isChatLoading}
                onClick={handleVenueSubmit}
              >
                {lang === 'hi' ? 'खोजें' : 'Search'}
              </button>
            </div>
          ) : (
            <form className="chat-input-form" onSubmit={handleSendMessage}>
              <textarea 
                className="chat-textarea" 
                placeholder={t.input_placeholder} 
                value={inputText}
                onChange={(e) => setInputText(e.target.value)}
                onKeyDown={(e) => {
                  if (e.key === 'Enter' && !e.shiftKey) {
                    e.preventDefault();
                    handleSendMessage();
                  }
                }}
              />
              <button type="submit" className="chat-send-btn" disabled={!inputText.trim() || isChatLoading}>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <line x1="22" y1="2" x2="11" y2="13"></line>
                  <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
                </svg>
              </button>
            </form>
          )}
        </div>
      </main>

      {/* RIGHT PANEL: SERVICE DETAILS */}
      {detailsPanelOpen && (
        <aside className="details-panel">
          <div className="details-header">
            <h2>{t.service_details}</h2>
            <button className="close-btn" onClick={() => setDetailsPanelOpen(false)}>✕</button>
          </div>

          <div className="details-content">
            {isDetailsLoading ? (
              <div className="spinner-container"><div className="spinner"></div></div>
            ) : details ? (
              <>
                <div className="detail-section">
                  <div className="detail-section-title">{t.service_name}</div>
                  <div className="detail-text-bold">{details.name}</div>
                </div>

                <div className="detail-section">
                  <div className="detail-section-title">{t.department}</div>
                  <div className="detail-text-secondary">{details.department}</div>
                </div>

                <div className="detail-section meta-grid">
                  <div className="meta-box">
                    <div className="meta-label">{t.time_limit}</div>
                    <div className="meta-value">{details.time_limit || details.sla || 'N/A'}</div>
                  </div>
                  <div className="meta-box">
                    <div className="meta-label">{t.contact_authority}</div>
                    <div className="meta-value">{details.contact_details || 'N/A'}</div>
                  </div>
                </div>

                <div className="detail-section">
                  <div className="detail-section-title">{t.fee_info}</div>
                  <div className="fee-cards">
                    <div className="fee-card">
                      <div className="fee-card-label">{t.online_fee}</div>
                      <div className="fee-card-value">{details.fees?.online_fee ? `₹${details.fees.online_fee}` : 'N/A'}</div>
                    </div>
                    <div className="fee-card">
                      <div className="fee-card-label">{t.kiosk_fee}</div>
                      <div className="fee-card-value">{details.fees?.kiosk_fee ? `₹${details.fees.kiosk_fee}` : 'N/A'}</div>
                    </div>
                  </div>
                  {details.fees?.raw_text && (
                    <div className="fee-note"><strong>Note:</strong> {details.fees.raw_text}</div>
                  )}
                </div>

                {details.details_link && (
                  <div className="detail-section">
                    <div className="detail-section-title">{t.apply_link}</div>
                    <div className="apply-box">
                      <p className="apply-text">{t.apply_desc}</p>
                      <a href={details.details_link} target="_blank" rel="noreferrer" className="apply-btn">{t.apply_btn}</a>
                    </div>
                  </div>
                )}

                {((details.required_documents_structured || details.required_documents) && (details.required_documents_structured || details.required_documents).length > 0) && (
                  <div className="detail-section">
                    <div className="detail-section-title">{t.required_docs}</div>
                    <div className="documents-list">
                      {((details.required_documents_structured || details.required_documents) || []).map((doc, idx) => {
                        let docType = "";
                        let isMandatory = false;
                        let supportingDocs = [];
                        if (doc && typeof doc === 'object') {
                          docType = doc.document_type;
                          isMandatory = (doc.mandatory || '').toLowerCase() === 'yes' || (doc.mandatory || '').trim() === 'हाँ';
                          supportingDocs = doc.supporting_documents || [];
                        } else if (typeof doc === 'string') {
                          const match = doc.match(/(.*?)\s*\(Mandatory:\s*(.*?)\)/);
                          if (match) {
                            docType = match[1].trim();
                            isMandatory = match[2].toLowerCase() === 'yes' || match[2].trim() === 'हाँ';
                          } else {
                            docType = doc.trim();
                            isMandatory = true;
                          }
                        }
                        return (
                          <div key={idx} className="document-card" style={{ display: 'flex', flexDirection: 'column', alignItems: 'stretch', gap: '8px' }}>
                            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', width: '100%' }}>
                              <div className="document-info">
                                <span className="document-bullet"></span>
                                <span className="document-name" style={{ fontWeight: 600 }}>{docType}</span>
                              </div>
                              <span className={`document-badge ${isMandatory ? 'mandatory' : 'optional'}`}>
                                {isMandatory ? t.mandatory : t.optional}
                              </span>
                            </div>
                            {supportingDocs.length > 1 && (
                              <div style={{ paddingLeft: '18px', borderTop: '1px dashed var(--border-color)', paddingTop: '6px', marginTop: '2px', textAlign: 'left' }}>
                                <div style={{ fontSize: '11px', color: 'var(--text-muted)', marginBottom: '4px', fontWeight: 600 }}>
                                  {lang === 'hi' ? 'निम्नलिखित में से कोई एक:' : 'Any one of the following:'}
                                </div>
                                <ul style={{ listStyleType: 'circle', paddingLeft: '14px', fontSize: '12px', color: 'var(--text-secondary)' }}>
                                  {supportingDocs.map((sub, sIdx) => (
                                    <li key={sIdx} style={{ marginBottom: '2px' }}>
                                      {sub.name}
                                    </li>
                                  ))}
                                </ul>
                              </div>
                            )}
                          </div>
                        );
                      })}
                    </div>
                  </div>
                )}

                {details.form_fields && details.form_fields.length > 0 && (
                  <div className="detail-section">
                    <div className="detail-section-title">{t.form_fields}</div>
                    <div className="fields-grid">
                      {details.form_fields.map((field, idx) => (
                        <div key={idx} className="field-row">
                          <div className="field-label">{field.label}</div>
                          <div className="field-type">
                            {field.input_type || 'text'} {field.data_type ? `(${field.data_type})` : ''}
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </>
            ) : (
              <div className="detail-text-secondary" style={{ textAlign: 'center', marginTop: '40px' }}>Select a service to view details.</div>
            )}
          </div>
        </aside>
      )}
    </div>
  );
}

export default App;
