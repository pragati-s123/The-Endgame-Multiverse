# The Endgame Multiverse

An AI-powered chatbot built with Streamlit and the Gemini API, where you can talk to different
Marvel personalities and each one responds while staying in character.

## What it does
Pick a hero from the sidebar, adjust how intensely they act out their personality, and chat with
them in a real chat interface — powered by Google's Gemini model. Built during a live session
with sir as a tutorial project, then independently upgraded afterward (see below).

## Base Features (from tutorial session)
- Personality selection via dropdown (`st.selectbox`)
- Text input for user messages
- Gemini API call with a personality-driven prompt
- Success/warning states for valid and empty submissions

## My Upgrades
After the session, I extended the base project with the following:

1. **Conversation memory (`st.session_state`)** — the original version treated every message as
   a one-off, stateless call with no memory of past exchanges. I added `session_state` to store
   the full chat history so the app now behaves like an actual conversation instead of isolated
   Q&A. History now persists even when switching personalities mid-conversation.

2. **Chat UI with `st.chat_message()`** — replaced plain `st.write()` output with proper chat
   bubbles that distinguish user messages from AI responses.

3. **Native chat input (`st.chat_input`)** — replaced the original text box and "SEND" button
   with Streamlit's dedicated chat input component, which auto-clears after each message and
   integrates directly with the chat UI.

4. **Error handling** — wrapped the Gemini API call in a try/except block, so a failed request
   shows a clean error message instead of crashing with a raw traceback.

5. **Sidebar layout** — moved the personality selector into a sidebar (`st.sidebar.selectbox`)
   so the main screen is reserved purely for the conversation.

6. **Intensity slider** — added `st.sidebar.slider("Intensity Level", 1, 10)`, which feeds
   directly into the prompt so the AI scales how exaggerated its in-character response is.

7. **Dynamic avatars** — an if/elif chain assigns a unique emoji avatar per personality, passed
   into `st.chat_message("assistant", avatar=bot_avatar)` for a more visually distinct chat.

8. **Marvel Endgame theme with expanded roster** — reworked the personality list into Avengers
   characters (Tony Stark, Thor, Steve Rogers, Thanos, Rocket Raccoon, Wanda Maximoff, Natasha
   Romanoff, Nick Fury, Star-Lord, Loki) for a cohesive, thematic experience.

## Tech
- Python
- Streamlit
- Google Gemini API (`google-genai`)
- `python-dotenv` for API key management

## Run locally
```bash
pip install streamlit google-genai python-dotenv
streamlit run app2.py
```

**Note:** requires a `.env` file with your own `GEMINI_API_KEY` — not included in this repo for
security reasons.
