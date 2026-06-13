import streamlit as st
from google import genai
import time

# ==========================
# ENTER YOUR API KEY HERE
# ==========================
API_KEY = "YOUR_API_KEY"

client = genai.Client(api_key=API_KEY)

# Page Configuration
st.set_page_config(
    page_title="AI FAQ Chatbot",
    page_icon="🤖"
)

# Title
st.title(" AI FAQ Chatbot")
st.write(
    "Ask questions related to Artificial Intelligence, Machine Learning, NLP, Data Science, and Computer Vision."
)

# User Input
question = st.text_area(
    "Enter your question:",
    placeholder="Ask"
)

# Ask Button
if st.button("Ask AI"):

    if not question.strip():
        st.warning("Please enter a question.")
    else:

        prompt = f"""
You are an AI educational assistant.

Answer the question in the following format:

1. Definition
2. Key Points
3. Real World Applications

Question:
{question}
"""

        success = False

        for attempt in range(3):

            try:

                response = client.models.generate_content(
                    model="gemini-2.5-flash-lite",
                    contents=prompt
                )

                st.success("Answer")

                st.write(response.text)

                success = True
                break

            except Exception as e:

                if attempt < 2:
                    st.warning(
                        f"Server busy. Retrying... ({attempt + 1}/3)"
                    )
                    time.sleep(3)

                else:
                    st.error(
                        "Gemini servers are currently busy. Please try again after a few minutes."
                    )
                    st.info(
                        "Tip: Refresh the page and retry your question."
                    )

# Footer
st.markdown("---")
st.caption("Developed using Python, Streamlit and Google Gemini API")