import streamlit as st
import random
import string
import math

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Password Generator",
    page_icon="🔐",
    layout="centered"
)

# ---------------- Styling ----------------
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        font-size: 18px;
        padding: 0.6rem;
        border-radius: 10px;
    }
    .password-box {
        font-size: 20px;
        font-weight: bold;
        padding: 10px;
        border-radius: 8px;
        background-color: #0e1117;
        border: 1px solid #30363d;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- Functions ----------------
def generate_password(length, upper, lower, digits, symbols, exclude_similar):
    characters = ""

    if upper:
        characters += string.ascii_uppercase
    if lower:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if symbols:
        characters += "!@#$%^&*()_+{}[]<>?"

    if exclude_similar:
        for ch in "O0l1I":
            characters = characters.replace(ch, "")

    if not characters:
        return ""

    return "".join(random.choice(characters) for _ in range(length))


def password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    return score


def calculate_entropy(password):
    pool = len(set(password))
    if pool == 0:
        return 0
    return round(len(password) * math.log2(pool), 2)

# ---------------- UI ----------------
st.title("🔐 Password Generator")
st.write("Generate **secure, customizable passwords** using Python & Streamlit.")

st.divider()

# Length
length = st.slider("Password Length", min_value=6, max_value=32, value=12)

# Options
st.subheader("Password Options")
col1, col2 = st.columns(2)

with col1:
    upper = st.checkbox("Uppercase (A-Z)", True)
    lower = st.checkbox("Lowercase (a-z)", True)
    digits = st.checkbox("Numbers (0-9)", True)

with col2:
    symbols = st.checkbox("Symbols (!@#$%)")
    exclude_similar = st.checkbox("Exclude similar characters (O,0,l,1)")

st.divider()

# Generate
if st.button("Generate Password"):
    password = generate_password(
        length, upper, lower, digits, symbols, exclude_similar
    )

    if password == "":
        st.error("Please select at least one character type.")
    else:
        st.markdown(
            f"<div class='password-box'>{password}</div>",
            unsafe_allow_html=True
        )

        # Copy
        st.code(password, language="text")

        # Strength
        strength = password_strength(password)
        entropy = calculate_entropy(password)

        if strength <= 1:
            st.error("Strength: Weak")
        elif strength == 2:
            st.warning("Strength: Medium")
        else:
            st.success("Strength: Strong")

        st.info(f"Password Entropy: **{entropy} bits**")

st.divider()
st.caption("🔒 Passwords are generated locally. Nothing is stored or logged.")
