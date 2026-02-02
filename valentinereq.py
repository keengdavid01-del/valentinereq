import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(page_title="For My Monklet ❤️", page_icon="💖")


# Removed the trailing '?' to ensure the URL loads correctly
spotify_src = "https://open.spotify.com/embed/playlist/6wZprQFnnKG8rQO0mhiW7M?"


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
        background-color: #ff4d6d !important;
        color: white !important;
    }
    .poem-box {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        border: 2px dashed #ffccd5;
        text-align: center;
        margin-top: 20px;
        color: #444;
        font-size: 1.2em;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)


with st.sidebar:
    st.markdown("### 🎵 For Monklet")
    # Change height from 80 to 152 to reveal the Play button
    components.iframe(spotify_src, height=152, scrolling=False)
    st.write("---")
    st.write("Click play for the vibes! ✨")


st.markdown('<h3 style="text-align: center;">❤️ 💌 ❤️</h3>', unsafe_allow_html=True)
st.title("Hi Monklet!")
st.header("Will you be my Valentine?")

col1, col2 = st.columns(2)

with col1:
    if st.button("YES! 💖"):
        st.balloons()
        st.markdown("### YAY! Best decision ever! 🥰")
        
        # Your custom "Human" poem
        st.markdown("""
            <div class="poem-box">
                Roses are red,<br>
                Violets are blue,<br>
                I don't know what else to rhyme...<br>
                But I love you. ❤️
            </div>
        """, unsafe_allow_html=True)
        
        st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGVlNDIyajN4N24ydGF1enpjamJwb2N2MDF2MmM3cWN4dzRyMGM5cCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/yZ7Xya4covzN1WhOAa/giphy.gif")

with col2:
    # The "Running" No button
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
                transition: all 0.15s ease;
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
                alert("Nice try Baby! You gotta click Yes!");
            });
        </script>
        """,
        height=350,
    )


