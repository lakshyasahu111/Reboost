# 🤖 AI Resume Agent Crew

> **A multi-agent AI system that analyzes your resume, hunts for jobs, and crafts tailored applications — fully automated.**

Built with [CrewAI](https://github.com/joaomdmoura/crewAI) and powered by **Google Gemini 2.5 Flash**, this project orchestrates a team of specialized AI agents to supercharge your job search from start to finish.

---

## ✨ What It Does

1. 🔍 **Analyzes** your resume for ATS optimization and improvement areas
2. 🌐 **Searches** the web for relevant job openings matching your profile
3. ✍️ **Generates** a tailored resume and cover letter for a target role

All three steps run sequentially as a coordinated crew — no manual intervention needed.

---

## 🏗️ Project Structure

```
├── main.py            # Entry point — assembles and runs the crew
├── agents.py          # Defines the three AI agents and their roles
├── tasks.py           # Defines the tasks assigned to each agent
├── tools.py           # Sets up the Serper web search tool
├── config.py          # API keys and LLM model configuration
├── requirements.txt   # All Python dependencies
└── fake_resume.md     # Your resume input (add this file)
```

---

## 🧠 The Agent Team

| Agent | Role | Responsibility |
|---|---|---|
| 📋 **Resume Analyst** | ATS & Resume Expert | Reviews your resume and suggests targeted improvements |
| 🔎 **Job Researcher** | Market Intelligence | Searches the web for relevant job openings using live data |
| ✍️ **Application Writer** | Career Copywriter | Crafts a tailored resume and cover letter for the best match |

---

## ⚙️ Tech Stack

| Component | Technology |
|---|---|
| Agent Framework | [CrewAI](https://github.com/joaomdmoura/crewAI) `v0.30.11` |
| LLM | Google Gemini 2.5 Flash (via LiteLLM) |
| Web Search | [SerperDev](https://serper.dev/) |
| Language | Python 3.10+ |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
SERPER_API_KEY=your_serper_api_key_here
```

> 🔑 Get your **Gemini API key** at [Google AI Studio](https://aistudio.google.com/)
> 🔑 Get your **Serper API key** at [serper.dev](https://serper.dev/)

### 4. Add Your Resume

Create a `fake_resume.md` file in the project root with your resume content in Markdown format:

```markdown
# Jane Doe
jane@example.com | linkedin.com/in/janedoe | github.com/janedoe

## Summary
...

## Experience
...

## Skills
...
```

### 5. Run the Crew

```bash
python main.py
```

---

## 📤 Output

After the crew finishes, you'll find:

- **Console output** — Live logs from each agent as they work through their tasks
- **`tailored_resume.md`** — A freshly generated, job-specific resume and cover letter saved to your project root

---

## 🔧 Configuration

To change the LLM model, update `config.py`:

```python
LLM_MODEL = "gemini/gemini-2.5-flash"  # Swap with any LiteLLM-supported model
```

CrewAI supports any model accessible via LiteLLM, including OpenAI, Anthropic, Mistral, and more.

---

## 📋 How It Works

```
Your Resume (fake_resume.md)
        │
        ▼
┌─────────────────────┐
│   Resume Analyst    │  ── Analyzes & suggests improvements
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│   Job Researcher    │  ── Searches for matching jobs online
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ Application Writer  │  ── Writes tailored resume + cover letter
└─────────┬───────────┘
          │
          ▼
  tailored_resume.md
```

Tasks run **sequentially** — each agent builds on the previous one's output for a coherent, context-aware result.

---

## 🐛 Troubleshooting

**`fake_resume.md` not found**
Make sure you've created the file in the project root before running `main.py`.

**API errors / rate limits**
Double-check your `.env` file has valid API keys. Gemini Flash has generous free-tier limits but may throttle on heavy use.

**Dependency conflicts**
It's recommended to use a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for:
- New agent types (e.g., Interview Prep Agent)
- Additional tools (LinkedIn scraping, job board APIs)
- Support for more resume formats (PDF, DOCX)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">

Built with ❤️ using [CrewAI](https://github.com/joaomdmoura/crewAI) · Powered by Google Gemini

</div>
