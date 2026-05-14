# Web UI Setup Guide

This guide explains how to use the web-based Career Assistant.

---

# 🚀 Live Deployment (Recommended)

You can use the application directly online:

👉 **https://multi-agent-career-assistant.onrender.com/**

No installation required.

---

# 🛠️ Local Development (Optional)

(… reszta pliku pozostaje taka sama …)

---

# 🔧 API Endpoints

Production base URL:

```
https://multi-agent-career-assistant.onrender.com
```

Endpoints:

- `POST /api/analyze`
- `GET /health`

---

# 💡 Usage Examples

### Web UI
Open:

```
https://multi-agent-career-assistant.onrender.com
```

### cURL

```bash
curl -X POST https://multi-agent-career-assistant.onrender.com/api/analyze \
  -F "job_url=https://example.com/job"
```

### Python

```python
import requests

response = requests.post(
    "https://multi-agent-career-assistant.onrender.com/api/analyze",
    data={"job_url": "https://example.com/job"}
)

print(response.json())
```

---

# 📦 Deployment Notes

Render free tier may introduce cold starts.

Ollama must run locally or on a separate machine.

---

---

## 📝 Next Steps

1. **Add Authentication**: Implement user login/registration
2. **Database**: Store analysis history for users
3. **Export Formats**: Add PDF, DOCX export options
4. **Real-time Updates**: Use WebSockets for live processing updates
5. **Advanced Filtering**: Allow users to filter and customize agent behavior
