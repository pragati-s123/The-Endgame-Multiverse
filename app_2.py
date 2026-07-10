import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

st.title("THE ENDGAME MULTIVERSE")

personality = st.selectbox("Which hero do you want to summon?", [
    "Tony Stark (Iron Man)",
    "Thor",
    "Steve Rogers (Captain America)",
    "Thanos",
    "Rocket Raccoon",
    "Wanda Maximoff (Scarlet Witch)",
    "Natasha Romanoff (Black Widow)"
])

if "current_personality" not in st.session_state:
    st.session_state.current_personality = personality

if personality != st.session_state.current_personality:
    st.session_state.messages = []
    st.session_state.current_personality = personality

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

with st.form("chat_form", clear_on_submit=True):
    user_message = st.text_input("Say something: ")
    submitted = st.form_submit_button("SEND")

if submitted:
    if user_message:
        st.session_state.messages.append({"role": "user", "content": user_message})

        ai_instructions = f"You are acting as {personality}. Respond to the message sent by the user staying completely in character: {user_message}"

        with st.spinner("Connecting to the multiverse!......"):
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=ai_instructions
                )
                st.session_state.messages.append({"role": "assistant", "content": response.text})
                st.success("Message received!")
            except Exception:
                st.error("Something went wrong connecting to the multiverse. Try again.")

        st.rerun()
    else:
        st.warning("Please type a message first")