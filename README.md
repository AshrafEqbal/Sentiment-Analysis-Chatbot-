# **Chatbot With Sentiment Analysis**

## **Project Overview**

This project implements an interactive **Chatbot with Sentiment Analysis** using a FastAPI backend and a browser-based frontend.
It fulfills **Tier 1 (mandatory)** and **Tier 2 (additional credit)** requirements of the assignment, including conversation tracking, per-message sentiment evaluation, and an overall sentiment assessment.

The system supports natural conversation, analyzes emotional tone, displays message-level emotions, and visualizes mood trends over time.

---

# **How to Run the Project**

## **1. Install Dependencies**

Make sure Python 3.9+ is installed.

Run:

```bash
pip install fastapi uvicorn google-generativeai pydantic
```

## **2. Add Your Gemini API Key**

In your backend file, update:

```python
genai.configure(api_key="YOUR_API_KEY_HERE")
```
(Note:A temporary API Key is put in code)

## **3. Start the Backend**

```bash
uvicorn main:app --reload
```

API will run at:

```
http://localhost:8000/gemini
```

## **4. Run the Frontend**

Open the `index.html` file directly in any browser.

No build tools required.

---

# **Technologies Used**

### **Backend**

* **Python**
* **FastAPI** – API server
* **Uvicorn** – ASGI server
* **Google Gemini API** – chat + sentiment generation
* **Pydantic** – request validation
* **CORS middleware** – allow frontend communication

### **Frontend**

* **HTML, CSS, JavaScript**
* **Chart.js** – visualization of mood trend

---

# **Sentiment Analysis Logic**

### **1. Statement-Level Sentiment (Tier 2)**

Each user message is analyzed individually using a structured Gemini prompt that returns only JSON:

* `"sentiment"` → positive / negative / neutral
* `"score"` → +1 / 0 / –1
* `"emotion"` → dominant feeling
* `"explanation"` → short reason

These details are displayed next to each user message and used to update:

* Mood chart
* Emotion tags
* Sentiment log

### **2. Conversation-Level Sentiment (Tier 1)**

For the entire session:

* Each message’s score is added to `overallScore`
* Positive score → overall positive
* Zero score → overall neutral
* Negative score → overall negative

Displayed as:

* **Mostly Positive**
* **Mostly Negative**
* **Neutral**

This satisfies Tier 1’s requirement for whole-conversation emotional direction.

---

# **Status of Tier Requirements**

### **Tier 1 — Conversation-Level Sentiment**

**Fully Implemented**

* Full conversation history maintained
* Final emotional direction calculated and displayed

### **Tier 2 — Statement-Level Sentiment**

**Fully Implemented**

* Each message analyzed individually
* Sentiment shown next to each user message
* Mood trend chart (enhancement)
* Emotion tags (enhancement)

---

# **Enhancements Beyond Requirements**

This project includes several optional improvements:

**Real-time mood trend graph** (Chart.js)
**Emotion tags for recent messages**
**Clean, modern chat UI**
**Reason explanations for each sentiment**
**On-screen mood summary**
**Modular backend structure**
**Conversation memory with dynamic bot replies**

These enhancements exceed the Tier 2 bonus expectations.

---

# **Repository Structure**

```
main.py (backend script)
index.html (frontend script)
README.md
```

---

# **Tests**

** All features were manually tested and verified to work correctly:**
* Chatbot response generation
* Statement-level sentiment analysis for each message
* Conversation-level sentiment summary
* Mood chart and emotion tags updates
* Error handling for invalid input or API issues

** No automated tests are included, but manual testing confirms full functionality.**

---

# **Final Notes**

* The chatbot is fully functional once an API key is added.
* Architecture is modular and production-minded.
* All assignment requirements (Tier 1 + Tier 2) are completed.
