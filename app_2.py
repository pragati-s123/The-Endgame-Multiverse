import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

st.title("THE ENDGAME MULTIVERSE")

st.sidebar.title("App Settings")

personality = st.sidebar.selectbox("Which hero do you want to summon?", [
    "Tony Stark (Iron Man)",
    "Thor",
    "Steve Rogers (Captain America)",
    "Thanos",
    "Rocket Raccoon",
    "Wanda Maximoff (Scarlet Witch)",
    "Natasha Romanoff (Black Widow)",
    "Nick Fury",
    "Star-Lord",
    "Loki"
])

intensity = st.sidebar.slider("Intensity Level", 1, 10)

if personality == "Tony Stark (Iron Man)":
    bot_avatar = "🦾"
elif personality == "Thor":
    bot_avatar = "⚡"
elif personality == "Steve Rogers (Captain America)":
    bot_avatar = "🛡️"
elif personality == "Thanos":
    bot_avatar = "🧤"
elif personality == "Rocket Raccoon":
    bot_avatar = "🦝"
elif personality == "Wanda Maximoff (Scarlet Witch)":
    bot_avatar = "🔮"
elif personality == "Natasha Romanoff (Black Widow)":
    bot_avatar = "🕷️"
elif personality == "Nick Fury":
    bot_avatar = "🕶️"
elif personality == "Star-Lord":
    bot_avatar = "🎧"
elif personality == "Loki":
    bot_avatar = "🐍"
else:
    bot_avatar = "🤖"

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.write(msg["content"])
    else:
        with st.chat_message("assistant", avatar=bot_avatar):
            st.write(msg["content"])

if user_message := st.chat_input("Say something..."):
    st.session_state.messages.append({"role": "user", "content": user_message})

    with st.chat_message("user"):
        st.write(user_message)

    ai_instructions = f"You are acting as {personality}. Act out this personality with an intensity level of {intensity} out of 10 — the higher the number, the more exaggerated and in-character your response should be. Respond to the message sent by the user staying completely in character: {user_message}"

    with st.spinner("Connecting to the multiverse!......"):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=ai_instructions
            )
            with st.chat_message("assistant", avatar=bot_avatar):
                st.write(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception:
            st.error("Something went wrong connecting to the multiverse. Try again.")
