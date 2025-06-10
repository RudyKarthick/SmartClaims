# SmartClaims

SmartClaims is a lightweight, AI-enhanced insurance triage tool built using .NET Blazor Server and Python Flask. It simulates real-time claim processing using local NLP via TextBlob.

---

## 🧠 Project Summary

In the insurance industry, incoming claim summaries are often unstructured. SmartClaims uses natural language processing to automatically assess:

- Claim Priority (based on sentiment)
- Fraud Risk (based on subjectivity)
- Next Action (based on key phrases)

---

## 🧰 Tech Stack

- Frontend: .NET 8, Blazor Server
- Backend: Python, Flask, TextBlob
- Extras: Bootstrap for styling, CORS for cross-service integration

---

## 🚀 How to Run Locally

### 🔹 1. Start the Flask API
```bash
cd SmartClaimsAI
source venv/bin/activate
python app.py
