# 🚀 Job Application Booster (CrewAI)

An AI-powered multi-agent system that helps improve resumes, find relevant job opportunities, and generate tailored job applications using **CrewAI**,**ChatGPT** (or **Gemini (via LiteLLM)**), and **Serper Search API**.

---

## 📌 Features

* 🔍 **Job Search Automation**
  Uses Serper API to find relevant job listings based on your resume.

* 📄 **Resume Analysis**
  Analyzes your resume and suggests improvements for ATS optimization.

* ✍️ **Application Generation**
  Generates a **tailored resume + cover letter** for job applications.

* 🧠 **Multi-Agent Workflow**
  Uses specialized AI agents:

  * Resume Analyst
  * Job Researcher
  * Application Writer

* 💾 **Output Storage**
  Final result is automatically saved as:

  ```
  tailored_resume.md
  ```

---

## 🏗️ Project Structure

```
job_booster/
│
├── main.py              # Entry point
├── agents.py            # Agent definitions
├── tasks.py             # Task definitions
├── tools.py             # Serper search tool
├── config.py            # API keys & LLM config
├─  fake_resume.txt          # Input resume
├── tailored_resume.md   # Final output (generated)
├── .env                 # API keys
└── requirements.txt
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/lakshyasahu111/Reboost.git
cd Reboost
```

---

### 2. Create virtual environment (recommended)

```bash
python -m venv .venv
source .venv/bin/activate   # Linux / Mac
# OR
.venv\Scripts\activate      # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add API keys

Create a `.env` file if not automatically created:

```env
GEMINI_API_KEY=your_gemini_api_key
SERPER_API_KEY=your_serper_api_key
```

---

### 5. Add your resume

Edit:

```
fake_resume.txt
```

Replace with your own resume content.

---

## 🚀 Run the Project

```bash
python main.py
```

---

## 📄 Output

After execution, the system will generate:

```
tailored_resume.md
```

This file contains:

* Improved Resume
* Tailored Cover Letter

---

## 🧠 How It Works

1. **Resume Analyst Agent**

   * Reviews resume
   * Suggests improvements

2. **Job Researcher Agent**

   * Uses Serper search tool
   * Finds relevant jobs

3. **Application Writer Agent**

   * Generates optimized resume
   * Creates tailored cover letter

---

## 🔧 Tech Stack

* **CrewAI** – Multi-agent orchestration
* **Gemini (via LiteLLM)** – LLM backend(Or any other LLM )
* **Serper API** – Job search
* **Python** – Core implementation

---

## ⚠️ Notes

* Ensure API keys are valid
* Do not commit `.env` to GitHub
* Avoid multiple async tasks in CrewAI (can cause validation errors)

---

## 🚀 Future Improvements

* 📄 PDF resume parsing
* 🌐 Web UI (Streamlit / React)
* 📊 Job ranking system
* 🔁 Iterative resume optimization
* 🧾 Export to PDF/DOCX

---

## 👨‍💻 Author

Lakshya Sahu

---

## 📜 License

This project is open-source and available under the MIT License.
