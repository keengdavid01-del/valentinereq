import streamlit as st
import random

# Page config
st.set_page_config(page_title="For Monklet ❤️", page_icon="💖")

# Corrected CSS logic
st.markdown("""
    <style>
    .stApp {
        background-color: #fff0f3;
    }
    h1, h2, h3 {
        color: #ff4d6d !important;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        text-align: center;
    }
    .stButton>button {
        border-radius: 20px;
        border: 2px solid #ff4d6d;
        background-color: white;
        color: #ff4d6d;
        font-weight: bold;
        height: 3em;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #ff4d6d;
        color: white;
    }
    .heart-deco {
        text-align: center;
        font-size: 30px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True) # FIXED: changed status to html

# Initializing state
if 'no_count' not in st.session_state:
    st.session_state.no_count = 0

def increase_no():
    st.session_state.no_count += 1

# Content
st.markdown('<div class="heart-deco">❤️ 💌 ❤️</div>', unsafe_allow_html=True)
st.title(f"Hi Monklet!")
st.header("Will you be my Valentine?")

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
    if st.button("YES! 💖"):
        st.balloons()
        st.write("### YAY! Best decision ever! 🥰")
        st.write("I love you, Monklet! See you on the 14th!")
        st.image("https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3dWtiNjVyYjhmcWViaDJ2dm1xdG9nbnZwaGd4NDVrcHlmbWhjNzNkNiZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/K64TYvCquNClUtF0dK/giphy.gif")

with col2:
    if st.session_state.no_count < 7:
        st.button(no_messages[msg_index], on_click=increase_no)
    else:
        st.write("💔 Oops! Button's broken.")


