import requests
import streamlit as st

# Streamlit UI setup
st.title("Femova.AI 🏥💬")
st.write("Ask me any questions related to PCOD and menstrual health!")

# User input box
user_input = st.text_area("Enter your query:", "")

# API endpoint (Make sure your Flask app is running on port 5047)
API_URL = "http://127.0.0.1:5048/process"

# Submit button
if st.button("Ask AI"):
    if user_input.strip():
        with st.spinner("Thinking... 💭"):
            response = requests.post(API_URL, json={"input": user_input})

            if response.status_code == 200:
                ai_response = response.json().get("response", {}).get("text", "No response received.")
                st.subheader("AI Response:")
                st.write(ai_response)
            else:
                st.error("Failed to process the request. Please check if the backend is running.")
    else:
        st.warning("Please enter a question before submitting.")

# Chat-like Experience
st.write("### Example Questions:")
st.markdown("- What are the symptoms of PCOD?")
st.markdown("- How can I improve my sleep quality?")
st.markdown("- What do i maintain my mentrual cycle?")
