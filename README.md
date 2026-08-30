# ✨ AI Text Summarizer & Rewriter

A simple Generative AI application for Task 7 of the EdQuest Applied AI Engineering certification course.

## Features
- Summarize text
- Rewrite text
- Select output length
- Select rewriting tone
- Download generated output

## Assignment Requirements Covered

| Requirement | Implementation |
|---|---|
| Generative AI | GPT-based text generation |
| Specific model | GPT-5.6 Luna |
| Use cases | Summarization and rewriting |
| Python | `app.py` |
| Prompt engineering | Task-specific instructions |
| API usage | OpenAI Responses API |
| Practical application | Streamlit web app |
| GitHub submission | Repository-ready project |

## Architecture

```text
User Input
   ↓
Task + Settings
   ↓
Prompt / Instruction
   ↓
OpenAI API
   ↓
GPT-5.6 Luna
   ↓
Generated Output
   ↓
Display / Download
```

## Run Locally

```bash
git clone https://github.com/YOUR_USERNAME/generative-ai-task-7.git
cd generative-ai-task-7
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create `.streamlit/secrets.toml`:

```toml
OPENAI_API_KEY = "your-api-key"
```

Then run:

```bash
streamlit run app.py
```

**Never commit the real `secrets.toml` or an API key to GitHub.**

## Prompt Engineering

The app uses separate instructions for summarization and rewriting. They specify the task, output length, preservation of facts/meaning, and a no-invention constraint. Rewriting also specifies the desired tone.

## Example

**Input:**  
Artificial intelligence is increasingly being used in education to support personalized learning. AI systems can analyze student performance, recommend learning materials and provide immediate feedback. However, educators still need to monitor these systems because AI-generated information can contain errors.

**Summary:**  
AI is increasingly supporting personalized education through performance analysis, recommendations and feedback, but teacher oversight remains necessary because AI can make errors.

**Professional rewrite:**  
Artificial intelligence is increasingly supporting personalized learning by analyzing student performance, recommending appropriate resources and providing immediate feedback. Nevertheless, educator oversight remains essential due to the possibility of AI-generated errors.

## Limitations
- Requires an API key.
- Output should be reviewed before important use.
- API usage can incur costs.
- This is intentionally a simple application; it does not use RAG or multi-agent orchestration.

## Future Improvements
- PDF/document upload
- Multilingual support
- Generation history
- Citation-aware summarization
- Evaluation metrics
- RAG
- Authentication and usage limits

## References
- OpenAI API: https://platform.openai.com/docs/
- Streamlit: https://docs.streamlit.io/
