import streamlit as st
from google import genai

# Configure Gemini API

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
# Debug: list available models
for m in client.models.list():
    st.write(m.name)

# Page Configuration

st.set_page_config(
    page_title="AskSejal AI",
    page_icon="🤖"
)

st.title("🤖 AskSejal AI")
st.subheader("Your Personal AI Learning Buddy")
st.write("Learn any topic in a simple and interactive way.")
st.divider()

# User Input

topic = st.text_input("📚 Enter a Topic", placeholder="Example: AI Agents")

activity = st.selectbox(
    "🎯 Choose an Activity",
    [
        "Explain Topic",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)

# Generate Button

if st.button("✨ Generate Response"):

    if topic == "":
        st.warning("Please enter a topic first.")
    else:
        if activity == "Explain Topic":
            prompt = f"Explain {topic} in simple language for a beginner. End with 3 key takeaways."
        elif activity == "Real-Life Example":
            prompt = f"Give one simple real-life example of {topic} in beginner-friendly language."
        elif activity == "Generate Quiz":
            prompt = f"Create 5 multiple-choice questions on {topic} with four options each and provide the correct answer."
        else:
            prompt = f"Answer this question in simple language: {topic}"

        with st.spinner("Generating response..."):
            response = client.models.generate_content(
                model="gemini-1.5-flash",
                contents=prompt
            )

        st.success("Response Generated!")
        st.write(response.text)

st.divider()
st.caption("Made with ❤️ by Sejal Singh | Powered by Gemini AI")

