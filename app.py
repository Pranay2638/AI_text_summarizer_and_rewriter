import os
import streamlit as st
from google import genai

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Text Summarizer & Rewriter",
    page_icon="✨",
    layout="wide"
)

# --------------------------------------------------
# Configuration
# --------------------------------------------------

MODEL = "gemini-3.5-flash-lite"


# --------------------------------------------------
# Get Gemini API Key
# --------------------------------------------------

def get_api_key():
    try:
        if "GEMINI_API_KEY" in st.secrets:
            return st.secrets["GEMINI_API_KEY"]
    except Exception:
        pass

    return os.getenv("GEMINI_API_KEY")


# --------------------------------------------------
# Generate Text
# --------------------------------------------------

def generate_text(text, task, tone, length):

    api_key = get_api_key()

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY was not found. "
            "Add it to .streamlit/secrets.toml "
            "or set it as an environment variable."
        )

    client = genai.Client(api_key=api_key)

    # Summarization prompt
    if task == "Summarize":

        prompt = f"""
You are an AI text summarization assistant.

Summarize the following text.

Output length: {length}

Requirements:
- Keep the important facts.
- Preserve the original meaning.
- Do not add information that is not present.
- Make the summary clear and easy to understand.

Text:
{text}
"""

    # Rewriting prompt
    else:

        prompt = f"""
You are an AI writing assistant.

Rewrite the following text.

Tone: {tone}
Output length: {length}

Requirements:
- Preserve the original meaning.
- Keep all important information.
- Improve clarity and readability.
- Do not invent information.
- Return only the rewritten text.

Text:
{text}
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text


# --------------------------------------------------
# Application UI
# --------------------------------------------------

st.title("✨ AI Text Summarizer & Rewriter")

st.caption(
    "A simple Generative AI application built with "
    "Python, Streamlit and the Gemini API."
)


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.header("⚙️ Settings")

    task = st.radio(
        "Choose a task",
        ["Summarize", "Rewrite"]
    )

    length = st.selectbox(
        "Output length",
        ["Short", "Medium", "Detailed"],
        index=1
    )

    tone = st.selectbox(
        "Rewrite tone",
        [
            "Professional",
            "Simple",
            "Friendly",
            "Academic",
            "Concise"
        ],
        disabled=(task == "Summarize")
    )

    st.divider()

    st.markdown(f"**Model:** {MODEL}")
    st.markdown("**Framework:** Streamlit")
    st.markdown("**API:** Google Gemini")


# --------------------------------------------------
# Text Input
# --------------------------------------------------

text = st.text_area(
    "Enter your text",
    height=280,
    placeholder=(
        "Paste an article, paragraph, email, "
        "notes, or any other text here..."
    )
)


# --------------------------------------------------
# Generate Button
# --------------------------------------------------

if st.button(
    "✨ Generate",
    type="primary",
    use_container_width=True
):

    if not text.strip():

        st.warning(
            "Please enter some text first."
        )

    else:

        with st.spinner("Generating..."):

            try:

                result = generate_text(
                    text.strip(),
                    task,
                    tone,
                    length
                )

                st.subheader("📄 Result")

                st.write(result)

                st.download_button(
                    "⬇️ Download result",
                    data=result,
                    file_name="ai_result.txt",
                    mime="text/plain"
                )

            except Exception as e:

                st.error(
                    f"Something went wrong: {str(e)}"
                )


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "Educational project for the EdQuest "
    "Applied AI Engineering certification course."
)

