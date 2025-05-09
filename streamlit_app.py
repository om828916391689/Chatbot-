import streamlit as st
import json
import random
import re

# Load intents
with open("intents.json", "r") as file:
    intents = json.load(file)

# Function to find best matching intent
def get_intent(user_input):
    user_input = user_input.lower()
    for intent in intents["intents"]:
        for pattern in intent["text"]:  # ← fixed here
            if re.search(r'\b' + re.escape(pattern.lower()) + r'\b', user_input):
                return intent
    return None


# Get response based on intent
def get_response(user_input):
    intent = get_intent(user_input)
    if intent:
        return random.choice(intent["responses"])
    else:
        return "I'm sorry, I didn't understand that."

# Streamlit app
st.title("🤖 MIT Chatbot")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.chat_input("Ask me anything...")

if user_input:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = get_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
