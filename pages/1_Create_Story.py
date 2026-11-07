
import streamlit as st
import random

st.title("🎭 Create Your Story")
st.write("Choose a genre, enter your character name and begin!")

if "history" not in st.session_state:
    st.session_state.history = []
    st.session_state.character = ""
    st.session_state.started = False
    st.session_state.events = []
    st.session_state.theme = ""

theme = st.selectbox(
    "Choose Story Genre",
    ["Fantasy", "Horror", "Mystery", "Adventure"]
)

character = st.text_input("Enter Character Name")

if st.button("✨ Start New Story"):
    if character.strip():
        st.session_state.character = character.strip()
        st.session_state.theme = theme
        st.session_state.history = []
        st.session_state.events = []
        st.session_state.started = True

        openings = {
            "Fantasy": f"{character} discovered a magical kingdom hidden behind an ancient forest.",
            "Horror": f"{character} heard strange footsteps outside a locked room.",
            "Mystery": f"{character} received a mysterious letter containing a secret.",
            "Adventure": f"{character} discovered an ancient map leading to an unknown island."
        }

        st.session_state.history.append(openings[theme])
        st.session_state.events.append("Story started")
    else:
        st.warning("Please enter a character name.")

if st.session_state.started:

    st.divider()
    st.header("📚 Your Story")

    for i, part in enumerate(st.session_state.history):
        st.subheader(f"Chapter {i+1}")
        st.write(part)

    st.divider()
    st.header("🤔 What happens next?")

    choices = [
        "Explore the mysterious place",
        "Meet a stranger",
        "Discover a hidden secret"
    ]

    choice = st.radio("Make your decision:", choices)

    if st.button("Continue Story ➡️"):

        name = st.session_state.character

        story_options = {
            "Explore the mysterious place": [
                f"{name} entered the unknown place and discovered a surprising clue.",
                f"{name} moved deeper into the darkness and found something unexpected."
            ],
            "Meet a stranger": [
                f"{name} met a stranger who revealed an important secret.",
                f"A mysterious visitor approached {name} and offered help."
            ],
            "Discover a hidden secret": [
                f"{name} uncovered a secret that changed everything.",
                f"Behind an old door, {name} discovered the truth."
            ]
        }

        new_part = random.choice(story_options[choice])

        st.session_state.history.append(new_part)
        st.session_state.events.append(choice)

        st.rerun()

    if st.button("🔄 Restart Story"):
        st.session_state.history = []
        st.session_state.events = []
        st.session_state.started = False
        st.rerun()
