# LLM Security Helper

An AI-powered security auditing tool built for the **Careem Helpbot** ecosystem (and beyond). This application leverages the **Groq API** (Llama-3 models) to perform two critical security functions:

1. **Code Analysis:** Scanning source code for traditional vulnerabilities like SQL Injection and OS Injection.
2. **Threat Modeling:** Mapping Agentic application specifications to the **OWASP Top 10 for LLM** and **MITRE ATLAS** frameworks.

---

## 🚀 Features

* **Part 1: Security Fixer** - Analyzes code snippets and provides secure, patched alternatives focusing only on security-related improvements.
* **Part 2: GenAI Threat Modeler** - Takes application specs (like the Careem Helpbot) and identifies high-level architectural risks.
* **Modern UI** - Built with **Gradio** for a clean, tabbed, and interactive user experience.
* **Secure Secrets Management** - Uses `.env` files to ensure API keys are never hardcoded.

---

## 📁 Project Structure

```text
llm-security-helper/
├── app.py              # Main entry point (Gradio UI)
├── codechecker.py      # Logic for Part 1 (Code Analysis)
├── specschecker.py     # Logic for Part 2 (Specs & Frameworks)
├── .env                # API Keys (Excluded from Git)
├── requirements.txt    # Python dependencies
├── examples.txt        # Examples of the inputs you can enter + their expected results
└── README.md           # Documentation


```

---

## 🛠️ Setup & Installation

Follow these steps to get the project running locally.

### 1. Clone the Project

Open your terminal and navigate to your project folder.

### 2. Create a Virtual Environment

It is recommended to use a virtual environment to avoid library conflicts:

```bash
# Create the environment
python -m venv venv

# Activate it (Windows)
.\venv\Scripts\activate

# Activate it (Mac/Linux)
source venv/bin/activate

```

### 3. Install Dependencies

Install the required libraries using the provided `requirements.txt`:

```bash
pip install -r requirements.txt

```

### 4. Configure Your API Key

1. Create a file named `.env` in the root directory.
2. Add your Groq API key inside:
```text
GROQ_API_KEY=your_groq_api_key_here

```



---

## 🏃 How to Run

1. Ensure your virtual environment is **activated**.
2. Start the application:
```bash
python app.py

```


3. **Access the UI:** The terminal will provide a URL (usually `http://127.0.0.1:7860`). Copy and paste this into your browser.

---

## 🧪 Testing the App

### Part 1: Vulnerable Code Test

Paste a snippet like this into the "Code Analysis" tab:

```python
query = "SELECT * FROM users WHERE name = '" + user_input + "'"

```

*Expected Result:* The app should identify **SQL Injection** and suggest using **parameterized queries**.

### Part 2: Careem Helpbot Test

Paste these specs into the "App Specs" tab:

```text
"Careem Helpbot with access to User GPS, Refund Tools, and Database Read/Write capabilities."

```

*Expected Result:* The app should map risks to **LLM01 (Prompt Injection)** and **AML.T0054 (MITRE ATLAS)**.

for more examples you can check out the examples.txt
---
