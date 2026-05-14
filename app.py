import streamlit as st
import pickle
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Luxury House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
# Uncomment these when your .pkl files are available
# with open("Model_For_House_Price_Prediction.pkl", "rb") as f:
#     model = pickle.load(f)
# with open("scaler.pkl", "rb") as f:
#     scaler = pickle.load(f)

# ---------------- FULL PAGE CSS + NAVBAR + HERO (single block) ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@400;500;600&display=swap');

/* Reset Streamlit padding */
.block-container {
    padding-top: 0 !important;
    padding-left: 0 !important;
    padding-right: 0 !important;
    max-width: 100% !important;
}

section[data-testid="stMain"] > div {
    padding: 0 !important;
}

/* ---- NAVBAR ---- */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 18px 60px;
    background: #ffffff;
    box-shadow: 0 2px 12px rgba(0,0,0,0.08);
    position: sticky;
    top: 0;
    z-index: 999;
}
.logo {
    font-family: 'Playfair Display', serif;
    font-size: 22px;
    font-weight: 700;
    color: #1a1a2e;
    letter-spacing: 1px;
}
.menu {
    display: flex;
    gap: 36px;
}
.menu a {
    text-decoration: none;
    color: #444;
    font-family: 'Inter', sans-serif;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 1.5px;
    transition: color 0.2s;
}
.menu a:hover { color: #c8973a; }

/* ---- HERO ---- */
.hero {
    background-image: linear-gradient(rgba(10,10,20,0.45), rgba(10,10,20,0.55)),
                      url("https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=1600&q=80");
    background-size: cover;
    background-position: center 40%;
    height: 520px;
    display: flex;
    align-items: center;
    padding: 0 80px;
}
.hero-content { max-width: 620px; }
.hero-eyebrow {
    font-family: 'Inter', sans-serif;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 3px;
    color: #c8973a;
    text-transform: uppercase;
    margin-bottom: 16px;
}
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 58px;
    font-weight: 700;
    line-height: 1.1;
    color: #ffffff;
    margin-bottom: 20px;
}
.hero-subtitle {
    font-family: 'Inter', sans-serif;
    font-size: 16px;
    color: rgba(255,255,255,0.8);
    line-height: 1.6;
    margin-bottom: 30px;
}
.hero-badge {
    display: inline-block;
    background: rgba(200,151,58,0.15);
    border: 1px solid #c8973a;
    color: #c8973a;
    font-family: 'Inter', sans-serif;
    font-size: 13px;
    font-weight: 600;
    padding: 8px 20px;
    border-radius: 30px;
    letter-spacing: 0.5px;
}

/* ---- PREDICT SECTION ---- */
.predict-section {
    background: #f8f7f4;
    padding: 60px 80px;
}
.section-label {
    font-family: 'Inter', sans-serif;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 3px;
    color: #c8973a;
    text-transform: uppercase;
    margin-bottom: 8px;
}
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 32px;
    color: #1a1a2e;
    margin-bottom: 6px;
}
.section-desc {
    font-family: 'Inter', sans-serif;
    font-size: 14px;
    color: #888;
    margin-bottom: 32px;
}
.divider {
    width: 48px;
    height: 3px;
    background: #c8973a;
    border-radius: 2px;
    margin-bottom: 32px;
}

/* ---- STREAMLIT WIDGET OVERRIDES ---- */
div[data-testid="stNumberInput"] label,
div[data-testid="stSlider"] label {
    font-family: 'Inter', sans-serif !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    color: #ffff !important;
    letter-spacing: 0.3px !important;
}
div[data-testid="stNumberInput"] input {
    border-radius: 8px !important;
    border: 1.5px solid #e5e0d8 !important;
    font-family: 'Inter', sans-serif !important;
    background: #0000 !important;
}
div[data-testid="stNumberInput"] input:focus {
    border-color: #c8973a !important;
    box-shadow: 0 0 0 2px rgba(200,151,58,0.15) !important;
}

/* ---- BUTTON ---- */
div[data-testid="stButton"] > button {
    background: #1a1a2e !important;
    color: #fff !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 13px !important;
    font-weight: 700 !important;
    letter-spacing: 1.5px !important;
    text-transform: uppercase !important;
    padding: 14px 40px !important;
    border-radius: 6px !important;
    border: none !important;
    transition: background 0.2s !important;
    width: 100% !important;
}
div[data-testid="stButton"] > button:hover {
    background: #c8973a !important;
}

/* ---- RESULT BOX ---- */
.result-box {
    background: linear-gradient(135deg, #1a1a2e 0%, #2d2d4e 100%);
    border-left: 5px solid #c8973a;
    border-radius: 12px;
    padding: 28px 36px;
    margin-top: 24px;
    color: white;
}
.result-label {
    font-family: 'Inter', sans-serif;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 3px;
    color: #c8973a;
    text-transform: uppercase;
    margin-bottom: 8px;
}
.result-price {
    font-family: 'Playfair Display', serif;
    font-size: 42px;
    color: #ffffff;
    margin: 0;
}

/* ---- FOOTER ---- */
.footer {
    background: #1a1a2e;
    padding: 28px 80px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.footer-logo {
    font-family: 'Playfair Display', serif;
    font-size: 18px;
    color: #fff;
}
.footer-copy {
    font-family: 'Inter', sans-serif;
    font-size: 12px;
    color: rgba(255,255,255,0.4);
}
</style>

<!-- NAVBAR -->
<div class="navbar">
    <div class="logo">LUXURY PROPERTIES</div>
    <div class="menu">
        <a href="#">HOME</a>
        <a href="#">SALES</a>
        <a href="#">RENTALS</a>
        <a href="#">AGENTS</a>
        <a href="#">CONTACT</a>
    </div>
</div>

<!-- HERO -->
<div class="hero">
    <div class="hero-content">
        <div class="hero-eyebrow">California Real Estate</div>
        <div class="hero-title">Luxury Villa<br>Near the Bay</div>
        <div class="hero-subtitle">
            Predict California house prices with
            Machine Learning. Get accurate valuations in seconds.
        </div>
        <span class="hero-badge">✦ Smart Price Prediction</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------- PREDICT SECTION HEADER ----------------
st.markdown("""
<div class="predict-section">
    <div class="section-label">AI Valuation Tool</div>
    <div class="section-title">Enter Property Details</div>
    <div class="section-desc">Fill in the details below to get an instant price estimate powered by machine learning.</div>
    <div class="divider"></div>
</div>
""", unsafe_allow_html=True)

# ---------------- INPUT FORM (native Streamlit) ----------------
with st.container():
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        MedInc    = st.number_input("Median Income", value=3.0, step=0.1)
        HouseAge  = st.number_input("House Age (years)", value=30.0, step=1.0)

    with col2:
        AveRooms  = st.number_input("Average Rooms", value=5.0, step=0.5)
        AveBedrms = st.number_input("Average Bedrooms", value=1.0, step=0.5)

    with col3:
        Population = st.number_input("Population", value=1000.0, step=100.0)
        AveOccup   = st.number_input("Average Occupancy", value=3.0, step=0.1)

    with col4:
        Latitude   = st.number_input("Latitude", value=34.0, step=0.01)
        st.markdown("<br>", unsafe_allow_html=True)
        predict_btn = st.button("Predict House Price")

# ---------------- PREDICTION LOGIC ----------------
if predict_btn:
    input_df = pd.DataFrame({
        'MedInc':     [MedInc],
        'HouseAge':   [HouseAge],
        'AveRooms':   [AveRooms],
        'AveBedrms':  [AveBedrms],
        'Population': [Population],
        'AveOccup':   [AveOccup],
        'Latitude':   [Latitude],
    })

    try:
        input_scaled = scaler.transform(input_df)
        prediction   = model.predict(input_scaled)
        price        = round(prediction[0] * 100000, 2)

        st.markdown(f"""
        <div class="result-box">
            <div class="result-label">Estimated Market Value</div>
            <div class="result-price">${price:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)

    except NameError:
        # Model not loaded — demo output
        st.markdown("""
        <div class="result-box">
            <div class="result-label">Demo Mode — Load your .pkl files to activate</div>
            <div class="result-price">$485,000</div>
        </div>
        """, unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    <div class="footer-logo">LUXURY PROPERTIES</div>
    <div class="footer-copy">© 2025 Luxury Properties</div>
</div>
""", unsafe_allow_html=True)