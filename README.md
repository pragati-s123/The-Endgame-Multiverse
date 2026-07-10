# The Endgame Multiverse

An AI-powered chatbot built with Streamlit and the Gemini API, where you can talk to different
Marvel personalities and each one responds while staying in character.

## What it does
Pick a hero from the dropdown, type a message, and the AI responds as that character — powered
by Google's Gemini model. Built during a live session with sir as a tutorial project, then
independently upgraded afterward (see below).

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
   Q&A.

2. **Chat UI with `st.chat_message()`** — replaced plain `st.write()` output with proper chat
   bubbles that distinguish user messages from AI responses.

3. **Auto-clear on personality switch** — when switching to a different hero, the chat history
   resets automatically, so conversations don't carry over between characters.

4. **Error handling** — wrapped the Gemini API call in a try/except block, so a failed request
   shows a clean error message instead of crashing with a raw traceback.

5. **Form-based input with auto-clear (`st.form`, `clear_on_submit=True`)** — the text box now
   clears itself automatically after sending a message, instead of retaining old text.

6. **Marvel Endgame theme** — reworked the personality list into Avengers characters (Tony Stark,
   Thor, Steve Rogers, Thanos, Rocket Raccoon, Wanda Maximoff, Natasha Romanoff) for a more
   cohesive, thematic experience.

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
