
import streamlit as st

st.title("🧠 Character Memory")
st.write("View the details remembered by StoryVerse.")

if "history" not in st.session_state:
    st.session_state.history = []
    st.session_state.character = ""
    st.session_state.started = False
    st.session_state.events = []
    st.session_state.theme = ""

if st.session_state.started:

    st.subheader("👤 Main Character")
    st.write(st.session_state.character)

    st.subheader("🎭 Story Genre")
    st.write(st.session_state.theme)

    st.subheader("📊 Story Progress")
    st.metric("Total Story Events", len(st.session_state.events))

    st.subheader("📌 Remembered Events")

    for i, event in enumerate(st.session_state.events):
        st.write(f"{i+1}. {event}")

else:
    st.info("Start a story first to view character memory.")
