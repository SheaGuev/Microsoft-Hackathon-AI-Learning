# import streamlit as st
from openai import AzureOpenAI
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Access the variables
endpoint = os.getenv("ENDPOINT")
api_key = os.getenv("API_KEY")
api_version = os.getenv("API_VERSION")
model_name = os.getenv("MODEL_NAME")

# Initialize Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint=ENDPOINT,
    api_key=API_KEY,
    api_version=API_VERSION,
)

content = '''You are a helpful assistant used to convert questionaire answers into a short summary on how to best explain learning content to the use 
Here is a guide to understand the results Scoring Guide
Diagnosis Question 1 answers:
Dyslexia: struggles with written instructions (may prefer diagrams)
Dysgraphia: struggles with writing and organising thoughts (may benefit from bullet points)
Dyscalculia: Trouble with Numbers, (maths may need to be explained in other ways)
APD: Difficult with verbal explanation(avoid text to speech)
VPD: Trouble with visual understanding (avoid diagrams etc.)
ADHD: Prefers simple explanations, engaging content
None: Ignore this question

Count your answers:
Mostly A's: Visual Learner
Mostly B's: Auditory Learner
Mostly C's: Read/Write Learner
Mostly D's: Kinesthetic Learner
Visual Learners prefer diagrams, charts, and visual representations.
Auditory Learners learn best through listening and discussion.
Read/Write Learners prefer written information and note-taking.
Kinesthetic Learners learn best through hands-on experience and practice.

Please output a summary of the best way to explain learning content to the user based on their answers to the questionnaire provide in the prompt.'''


prompt1 = "Auditory Processing Disorder (APD), ADHD	c) Read a detailed written analysis	b) Talk to people who've been there	a) Watch video tutorials	d) Figure it out by experimenting	a) Follow the diagram illustrations	c) Reading about techniques	c) Reading materials and notes	c) Write detailed instructions	a) Create diagrams or mind maps	c) Remember written words"

prompt2 = "None,	d) Review practical examples from my work	d) Explore virtual tours or simulations	d) Try it hands-on through trial and error	d) Figure it out by experimenting	d) Try putting pieces together intuitively	b) Listening to explanations	d) Hands-on experiments	d) Walk with the person		d) Remember actions and movements"



# Function to get response from Azure OpenAI
def get_response(prompt):
    try:
        messages = [
            {"role": "system", "content": content},
            {"role": "user", "content": prompt}
        ]
        
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# # Initialize session state for chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Streamlit interface
# st.title("Azure OpenAI Chat App")
# st.subheader("Ask me anything!")

# # Input box for user query
# user_input = st.text_input("Enter your prompt:")

# if st.button("Send"):
#     if user_input.strip():
#         # Add user message to chat history
#         st.session_state.messages.append({"role": "user", "content": user_input})
        
#         with st.spinner("Generating response..."):
#             llm_response = get_response(user_input)
#             # Add assistant response to chat history
#             st.session_state.messages.append({"role": "assistant", "content": llm_response})

# # Display chat history
# for message in st.session_state.messages:
#     if message["role"] == "user":
#         st.markdown("### You")
#         st.write(message["content"])
#     else:
#         st.markdown("### Assistant")
#         st.write(message["content"])

def p1():
    return get_response(prompt1)

def p2():
    return get_response(prompt2)


    # p2()
    
