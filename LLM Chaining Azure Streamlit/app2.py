import streamlit as st
from openai import AzureOpenAI
import app

# Azure OpenAI Configuration
ENDPOINT = "https://mango-bush-0a9e12903.5.azurestaticapps.net/api/v1"
API_KEY = "581cdf93-397a-442a-86f1-ed82cdc4185d"
API_VERSION = "2024-02-01"
MODEL_NAME = "gpt-4o"

# Initialize Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint=ENDPOINT,
    api_key=API_KEY,
    api_version=API_VERSION,
)

# summary = app.p1()
summary = app.p2()

# Function to get response from Azure OpenAI
def get_response(prompt):
    try:
        messages = [
            {"role": "system", "content": "Please present the learning material in a way the user can understand using the following summary of them: " + summary},
            {"role": "user", "content": prompt}
        ]
        
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=0.7,
        )
        print(summary)
        return response.choices[0].message.content + "\n" + "Here is the relevant summary from the previous LLM Chain: " + summary
    except Exception as e:
        return f"Error: {str(e)}"

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Streamlit interface
st.title("Azure OpenAI Chat App")
st.subheader("Ask me anything!")

option = st.selectbox(
    label="Choose an option",
    options=["Questionaire1", "Questionaire2"]
)

if option == "Questionaire1":
    summary = app.p1()
elif option == "Questionaire2":
    summary = app.p2()
    
# Input box for user query
user_input = st.text_input("Enter your prompt:")

if st.button("Send"):
    if user_input.strip():
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        with st.spinner("Generating response..."):
            llm_response = get_response(user_input)
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": llm_response})

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown("### You")
        st.write(message["content"])
    else:
        st.markdown("### Assistant")
        st.write(message["content"])