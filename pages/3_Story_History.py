
import streamlit as st

st.title("📜 Story History")
st.write("View and download your complete story.")

if "history" not in st.session_state:
    st.session_state.history = []
    st.session_state.character = ""
    st.session_state.started = False
    st.session_state.events = []
    st.session_state.theme = ""

if st.session_state.history:

    st.subheader("👤 Character: " + st.session_state.character)
    st.subheader("🎭 Genre: " + st.session_state.theme)

    complete_story = ""

    for i, part in enumerate(st.session_state.history):
        st.markdown(f"### Chapter {i+1}")
        st.write(part)
        complete_story += f"Chapter {i+1}\n{part}\n\n"

    st.download_button(
        label="📥 Download Your Story",
        data=complete_story,
        file_name="StoryVerse_Story.txt",
        mime="text/plain"
    )

else:
    st.info("No story available. Go to Create Story and start an adventure!")
