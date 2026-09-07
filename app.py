import streamlit as st
import google.genai as genai

# Configure Gemini API

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Page Configuration

st.set_page_config(
    page_title="AskSejal AI",
    page_icon="🤖"
)

# Header

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
            prompt = f"""
            You are AskSejal AI.
            Explain {topic} in simple language for a beginner.
            Keep the explanation short and easy to understand.
            End with 3 key takeaways.
            """
        elif activity == "Real-Life Example":
            prompt = f"""
            You are AskSejal AI.
            Give one simple real-life example of {topic}.
            Explain it in beginner-friendly language.
            """
        elif activity == "Generate Quiz":
            prompt = f"""
            You are AskSejal AI.
            Create 5 multiple-choice questions on {topic}.
            Give four options for each question.
            Provide the correct answer after every question.
            """
        else:
            prompt = f"""
            You are AskSejal AI.
            Answer this question in simple language:
            {topic}
            """

        with st.spinner("Generating response..."):
            response = model.generate_content(prompt)

        st.success("Response Generated!")
        st.write(response.text)

st.divider()
st.caption("Made with ❤️ by Sejal Singh | Powered by Gemini AI")
