import streamlit as st
import streamlit.components.v1 as components

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
        text-align: center;
    }
    /* Style for the Streamlit Yes button */
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
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h3 style="text-align: center;">❤️ 💌 ❤️</h3>', unsafe_allow_html=True)
st.title("Hi Monklet!")
st.header("Will you be my Valentine?")

col1, col2 = st.columns(2)

with col1:
    # The actual functional Yes button
    if st.button("YES! 💖"):
        st.balloons()
        st.markdown("### YAY! Best decision ever! 🥰")
        st.markdown("<p style='text-align:center;'>I love you, Monklet! See you on the 14th!</p>", unsafe_allow_html=True)
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHpueGZ3bmZqZzR4eXp3ZzR4eXp3ZzR4eXp3ZzR4eXp3ZzR4eXp3JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/KztT2c4u8mYYUiCiY6/giphy.gif")

with col2:
    # The "Running" No button using JavaScript
    # This creates a small sandbox where the button lives and escapes
    components.html(
        """
        <div id="container" style="height: 300px; width: 100%; position: relative;">
            <button id="noButton" style="
                position: absolute;
                padding: 10px 20px;
                background-color: white;
                color: #ff4d6d;
                border: 2px solid #ff4d6d;
                border-radius: 20px;
                font-weight: bold;
                cursor: pointer;
                transition: all 0.2s ease;
                z-index: 1000;
            ">No</button>
        </div>

        <script>
            const btn = document.getElementById('noButton');
            const container = document.getElementById('container');

            btn.addEventListener('mouseover', function() {
                const containerWidth = container.clientWidth - btn.clientWidth;
                const containerHeight = container.clientHeight - btn.clientHeight;
                
                const newLeft = Math.random() * containerWidth;
                const newTop = Math.random() * containerHeight;
                
                btn.style.left = newLeft + 'px';
                btn.style.top = newTop + 'px';
            });
            
            btn.addEventListener('click', function() {
                alert("Nice try, Monklet! You gotta click Yes!");
            });
        </script>
        """,
        height=350,
    )
