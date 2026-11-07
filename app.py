
import streamlit as st

st.set_page_config(
    page_title="StoryVerse",
    page_icon="📖",
    layout="wide"
)

# Initialize shared story data
if "history" not in st.session_state:
    st.session_state.history = []

if "character" not in st.session_state:
    st.session_state.character = ""

if "started" not in st.session_state:
    st.session_state.started = False

if "events" not in st.session_state:
    st.session_state.events = []

if "theme" not in st.session_state:
    st.session_state.theme = ""

# Custom design
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #101020, #211638);
    color: #ffffff;
}

[data-testid="stSidebar"] {
    background-color: #171326;
}

[data-testid="stSidebar"] * {
    color: #ffffff !important;
}

h1, h2, h3, h4, p, label, .stMarkdown {
    color: #ffffff !important;
}

.stButton button {
    background-color: #7c3aed;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: bold;
}

.stButton button:hover {
    background-color: #6d28d9;
    color: white;
}

.stAlert {
    border-radius: 12px;
}

[data-testid="stMetricValue"] {
    color: #d8b4fe;
}

</style>
""", unsafe_allow_html=True)

# Home page content
st.title("📖 Welcome to StoryVerse")

st.subheader("Your imagination. Your choices. Your story.")

st.divider()

st.header("✨ Create Your Own Adventure")

st.write("""
StoryVerse is an interactive storytelling application
where users can create personalized stories, explore
different genres and decide how their stories continue
through their own choices.
""")

col1, col2 = st.columns(2)

with col1:
    st.info(
        "🎭 Explore Fantasy, Horror, Mystery and Adventure stories."
    )

with col2:
    st.info(
        "🧠 Track characters, remember events and save your stories."
    )

st.divider()

st.header("🚀 How to Use StoryVerse")

st.write("1. Open the Create Story page from the sidebar.")
st.write("2. Choose your favourite genre.")
st.write("3. Enter your character's name.")
st.write("4. Start your story and make decisions.")
st.write("5. View your story history and download it.")

st.divider()

st.header("🌟 Your Story Begins Here")

st.success(
    "Select Create Story from the left sidebar and start your adventure!"
)

st.caption("StoryVerse | Interactive Storytelling Application")
