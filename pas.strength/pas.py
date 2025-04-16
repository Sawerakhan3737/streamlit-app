import streamlit as st
import random
import string
import re

st.set_page_config(page_title="💡 Stylish Password Meter", layout="centered")

st.markdown("""
    <style>
    /* Animated gradient background */
    body, .stApp {
        background: linear-gradient(-45deg, #1e3c72, #2a5298, #a1c4fd, #c2e9fb);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        color: white;
    }

    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    /* Glass container effect */
    .glass {
        background: rgba(255, 255, 255, 0.08);
        padding: 2rem;
        border-radius: 20px;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.2);
    }

    .title {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        color: #fff;
        margin-bottom: 20px;
    }

    .section {
        margin-top: 30px;
        font-size: 1.3em;
        font-weight: 600;
        color: #f1f1f1;
    }

    .custom-button {
        background-color: #6a11cb;
        background-image: linear-gradient(315deg, #6a11cb 0%, #2575fc 74%);
        border: none;
        padding: 10px 20px;
        color: white;
        border-radius: 10px;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    .custom-button:hover {
        box-shadow: 0 0 15px rgba(255, 255, 255, 0.3);
        transform: scale(1.05);
    }

    .strength-bar-container {
        background-color: #ccc;
        border-radius: 8px;
        width: 100%;
        height: 20px;
        margin: 10px 0;
        overflow: hidden;
    }

    .strength-bar {
        height: 100%;
        transition: width 0.3s ease-in-out;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

def evaluate_strength(pw):
    length_criteria = len(pw) >= 8
    upper = re.search(r"[A-Z]", pw)
    lower = re.search(r"[a-z]", pw)
    digit = re.search(r"\d", pw)
    special = re.search(r"[^A-Za-z0-9]", pw)

    score = sum([bool(x) for x in [length_criteria, upper, lower, digit, special]])

    if score <= 2:
        return "Weak", 0.3, "#e74c3c", "Use more characters, uppercase, numbers, and symbols."
    elif score == 3 or score == 4:
        return "Medium", 0.6, "#f39c12", "Getting there! Add more variety and length."
    else:
        return "Strong", 1.0, "#2ecc71", "Great! This is a strong password."

def generate_password(length=14, use_upper=True, use_digits=True, use_symbols=True):
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))


st.markdown('<div class="title">🔐 Stylish Password Strength Meter</div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="glass">', unsafe_allow_html=True)

    st.markdown('<div class="section">🔎 Check Your Password</div>', unsafe_allow_html=True)
    password = st.text_input("Enter your password", type="password")

    if password:
        strength, progress, color, suggestion = evaluate_strength(password)

        st.markdown(f"**Strength:** :blue[{strength}]")
        st.markdown(f"""
            <div class="strength-bar-container">
                <div class="strength-bar" style="width: {progress*100}%; background-color: {color};"></div>
            </div>
        """, unsafe_allow_html=True)
        st.info(suggestion)

    st.markdown('<div class="section">⚙️ Generate Password</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        length = st.slider("Length", 8, 24, 12)
    with col2:
        upper = st.checkbox("Include Uppercase", True)
        digits = st.checkbox("Include Numbers", True)
        symbols = st.checkbox("Include Symbols", True)

    if st.button("🔁 Generate", key="gen"):
        generated_pw = generate_password(length, upper, digits, symbols)
        st.success("Generated Password:")
        st.code(generated_pw, language="text")
        st.session_state["generated"] = generated_pw

    

    st.markdown('<div class="section">✅ Submit Password</div>', unsafe_allow_html=True)
    final_password = password or st.session_state.get("generated", "")

    if st.button("🚀 Submit", key="submit"):
        if final_password:
            strength, _, _, _ = evaluate_strength(final_password)
            if strength == "Strong":
                st.success("🎉 Success! Your password is strong and accepted.")
            else:
                st.warning(f"⚠️ Your password is {strength}. Please improve it before submission.")
        else:
            st.error("❌ Please enter or generate a password.")

    st.markdown('</div>', unsafe_allow_html=True)
