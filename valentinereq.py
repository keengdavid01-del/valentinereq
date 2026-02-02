import streamlit as st
import random

# Page config
st.set_page_config(page_title="For Monklet ❤️", page_icon="💖")

# Custom CSS for the "Valentine" vibe
st.markdown("""
    <style>
    .stApp {
        background-color: #fff0f3;
    }
    h1, h2, h3 {
        color: #ff4d6d !important;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .stButton>button {
        border-radius: 20px;
        border: 2px solid #ff4d6d;
        background-color: white;
        color: #ff4d6d;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #ff4d6d;
        color: white;
    }
    </style>
    """, unsafe_allow_status=True)

# Initializing state
if 'no_count' not in st.session_state:
    st.session_state.no_count = 0

def increase_no():
    st.session_state.no_count += 1

# Content
st.write("### ❤️ 💌 ❤️")
st.title(f"Hi Monklet!")
st.header("Will you be my Valentine?")

# Animated Hearts (Visual flair)
st.write("💕 ✨ 🌸 ✨ 💕")

# The "No" responses
no_messages = [
    "No",
    "Wait... really?",
    "Monklet, please? 🥺",
    "Don't do this to me!",
    "Think of the chocolate!",
    "Is that your final answer?",
    "Okay, I'm hiding the button now."
]

msg_index = min(st.session_state.no_count, len(no_messages) - 1)

col1, col2 = st.columns(2)

with col1:
    if st.button("YES! 💖", use_container_width=True):
        st.balloons()
        st.write("### YAY! Best decision ever! 🥰")
        st.write("I love you, Monklet! See you on the 14th!")
        # A cute celebratory cat/heart GIF
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHpueGZ3bmZqZzR4eXp3ZzR4eXp3ZzR4eXp3ZzR4eXp3ZzR4eXp3JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/KztT2c4u8mYYUiCiY6/giphy.gif")

with col2:
    if st.session_state.no_count < 7:
        st.button(no_messages[msg_index], on_click=increase_no, use_container_width=True)
    else:
        st.write("💔 Interaction disabled. Try the other button!")