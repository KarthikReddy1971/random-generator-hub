import streamlit as st

from random_number import random_number_generator
from dice import dice_roller
from coin_flip import coin_flip


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Random Generator Hub",
    page_icon="🎰",
    layout="centered"
)


# ============================================================
# NOVAMART-STYLE COLOR THEME
# ============================================================

st.markdown(
    """
    <style>

    /* =====================================================
       MAIN BACKGROUND
       ===================================================== */

    .stApp {
        background-color: #F3E7DA !important;
    }

    [data-testid="stAppViewContainer"] {
        background-color: #F3E7DA !important;
    }

    [data-testid="stHeader"] {
        background-color: #F3E7DA !important;
    }


    /* =====================================================
       MAIN CONTENT
       ===================================================== */

    .main .block-container {
        max-width: 850px !important;
        padding-top: 50px !important;
        padding-bottom: 50px !important;
    }


    /* =====================================================
       HEADINGS
       ===================================================== */

    h1 {
        color: #8A5A44 !important;
        font-weight: 800 !important;
        letter-spacing: -1px;
    }

    h2,
    h3,
    h4 {
        color: #8A5A44 !important;
    }


    /* =====================================================
       NORMAL TEXT
       ===================================================== */

    p {
        color: #3E2C23 !important;
    }

    label {
        color: #3E2C23 !important;
    }


    /* =====================================================
       GENERATOR SELECTOR
       ===================================================== */

    div[data-testid="stRadio"] {

        background-color: #FBF4EC !important;

        border: 1px solid #E4D4C3 !important;

        border-radius: 16px !important;

        padding: 18px 22px !important;

        box-shadow:
            0 4px 12px rgba(62, 44, 35, 0.08);
    }


    div[data-testid="stRadio"] label {
        color: #3E2C23 !important;
    }

    div[data-testid="stRadio"] p {
        color: #3E2C23 !important;
    }


    /* =====================================================
       BUTTONS
       ===================================================== */

    div.stButton > button {

        width: 100% !important;

        min-height: 48px !important;

        border-radius: 10px !important;

        border: none !important;

        background-color: #B08968 !important;

        color: #FFFDFB !important;

        font-size: 16px !important;

        font-weight: 700 !important;

        transition: all 0.2s ease !important;

        box-shadow:
            0 4px 10px rgba(62, 44, 35, 0.12);
    }


    div.stButton > button p {

        color: #FFFDFB !important;

    }


    div.stButton > button:hover {

        background-color: #8A5A44 !important;

        transform: translateY(-2px) !important;

        box-shadow:
            0 7px 16px rgba(62, 44, 35, 0.18);
    }


    /* =====================================================
       NUMBER INPUT
       ===================================================== */

    div[data-testid="stNumberInput"] {

        color: #3E2C23 !important;
    }

    div[data-testid="stNumberInput"] label {

        color: #3E2C23 !important;

        font-weight: 600 !important;
    }

    div[data-testid="stNumberInput"] input {

        background-color: #FFFDFB !important;

        color: #3E2C23 !important;

        border: 1px solid #E4D4C3 !important;

        border-radius: 10px !important;
    }


    /* =====================================================
       SECRET NUMBER INPUT
       ===================================================== */

    div[data-testid="stTextInput"] label {

        color: #3E2C23 !important;

        font-weight: 600 !important;
    }

    div[data-testid="stTextInput"] input {

        background-color: #FFFDFB !important;

        color: #3E2C23 !important;

        border: 1px solid #E4D4C3 !important;

        border-radius: 10px !important;
    }

    div[data-testid="stTextInput"] input::placeholder {

        color: #A68A78 !important;
    }


    /* =====================================================
       SELECT BOX
       ===================================================== */

    div[data-baseweb="select"] > div {

        background-color: #FFFDFB !important;

        color: #3E2C23 !important;

        border-color: #E4D4C3 !important;

        border-radius: 10px !important;
    }


    /* =====================================================
       INPUT ICONS / CONTROLS
       ===================================================== */

    button[kind="step-up"],
    button[kind="step-down"] {

        color: #8A5A44 !important;

    }


    /* =====================================================
       ALERTS
       ===================================================== */

    [data-testid="stAlert"] {

        border-radius: 12px !important;

    }


    /* =====================================================
       DIVIDERS
       ===================================================== */

    hr {

        border-color: #E4D4C3 !important;

    }


    /* =====================================================
       CAPTION
       ===================================================== */

    [data-testid="stCaptionContainer"] {

        color: #6B5143 !important;

    }

    [data-testid="stCaptionContainer"] p {

        color: #6B5143 !important;

    }


    /* =====================================================
       FOOTER
       ===================================================== */

    footer {
        visibility: hidden;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.title("🎰 Random Generator Hub")

st.caption(
    "✨ Randomize • Roll • Flip"
)


# ============================================================
# GENERATOR SELECTOR
# ============================================================

option = st.radio(
    "Choose your generator",
    [
        "🔢 Random Number",
        "🎲 Dice Roller",
        "🪙 Coin Flip"
    ],
    horizontal=True
)


st.divider()


# ============================================================
# GENERATOR MODULES
# ============================================================

if option == "🔢 Random Number":

    random_number_generator()

elif option == "🎲 Dice Roller":

    dice_roller()

elif option == "🪙 Coin Flip":

    coin_flip()


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🎰 Random Generator Hub • Built with Streamlit"
)