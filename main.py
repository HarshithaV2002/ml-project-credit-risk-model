import streamlit as st
from prediction_helper import predict  # Ensure this is correctly linked to your prediction_helper.py

# --- Page Setup ---
st.set_page_config(page_title="Lauki Finance: Credit Risk Modelling", page_icon="📊", layout="wide")

# --- Custom CSS ---
st.markdown("""
    <style>
    /* Remove dark top padding and bar */
    header[data-testid="stHeader"] {
        background-color: white !important;
    }

    /* Make sidebar, main area, and full app white */
    .stApp, .stMainBlockContainer, section[data-testid="stSidebar"], div[data-testid="stToolbar"] {
        background-color: white !important;
        color: black !important;
    }

    /* Title styling */
    h1 {
        color: #FFD700 !important; /* Yellow title */
        font-weight: 800;
        text-align: center;
        margin-bottom: 30px !important;
    }

    /* Add padding and spacing between columns */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        padding-left: 5rem !important;
        padding-right: 5rem !important;
    }

    /* Add margin between columns */
    div[data-testid="column"] {
        padding-right: 1.5rem !important;
        padding-left: 1.5rem !important;
    }

    /* Input fields (white with yellow border) */
    .stNumberInput input,
    .stSelectbox div[data-baseweb="select"] > div {
        background-color: white !important;
        color: black !important;
        border: 2px solid #FFD700 !important;
        border-radius: 6px;
    }

    /* Label color to yellow */
    label {
        color: #FFD700 !important; /* Yellow label text */
        font-weight: 600 !important;
    }

    /* Normal paragraph and span text stays black */
    p, span, .stText, .stMarkdown, .css-17eq0hr, .st-emotion-cache {
        color: black !important;
        font-weight: 500;
    }

    /* Button styling */
    div.stButton > button {
        background-color: #FFD700 !important;
        color: black !important;
        border: none !important;
        border-radius: 6px !important;
        font-weight: 700 !important;
        padding: 10px 20px !important;
        margin-top: 20px !important;
    }
    div.stButton > button:hover {
        background-color: #FFC300 !important;
        color: black !important;
    }

    /* Output text bold */
    .stWrite, .stMarkdown p {
        font-weight: bold;
        color: black !important;
    }

    /* Ensure ratio text visible */
    div[data-testid="stText"] {
        color: black !important;
        font-weight: 600;
    }

    /* Space below output */
    .stMarkdown {
        margin-bottom: 15px !important;
    }
     * {
        cursor: default !important; /* makes cursor normal instead of text select */
    }
    input, select, textarea {
        color: black !important;
        caret-color: black !important; /* makes blinking cursor black */
    }
    
    </style>
""", unsafe_allow_html=True)

# --- App Title ---
st.title("Lauki Finance: Credit Risk Modelling")

# --- Layout ---
row1 = st.columns([1, 1, 1])
row2 = st.columns([1, 1, 1])
row3 = st.columns([1, 1, 1])
row4 = st.columns([1, 1, 1])

with row1[0]:
    age = st.number_input('Age', min_value=18, step=1, max_value=100, value=28)
with row1[1]:
    income = st.number_input('Income', min_value=0, value=1200000)
with row1[2]:
    loan_amount = st.number_input('Loan Amount', min_value=0, value=2560000)

loan_to_income_ratio = loan_amount / income if income > 0 else 0
with row2[0]:
    st.markdown("<p style='color:black; font-weight:600;'>Loan to Income Ratio:</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:black; font-weight:600;'>{loan_to_income_ratio:.2f}</p>", unsafe_allow_html=True)

with row2[1]:
    loan_tenure_months = st.number_input('Loan Tenure (months)', min_value=0, step=1, value=36)
with row2[2]:
    avg_dpd_per_delinquency = st.number_input('Avg DPD', min_value=0, value=20)

with row3[0]:
    delinquency_ratio = st.number_input('Delinquency Ratio', min_value=0, max_value=100, step=1, value=30)
with row3[1]:
    credit_utilization_ratio = st.number_input('Credit Utilization Ratio', min_value=0, max_value=100, step=1, value=30)
with row3[2]:
    num_open_accounts = st.number_input('Open Loan Accounts', min_value=1, max_value=4, step=1, value=2)

with row4[0]:
    residence_type = st.selectbox('Residence Type', ['Owned', 'Rented', 'Mortgage'])
with row4[1]:
    loan_purpose = st.selectbox('Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])
with row4[2]:
    loan_type = st.selectbox('Loan Type', ['Unsecured', 'Secured'])

# --- Button and Prediction ---
st.markdown("<br>", unsafe_allow_html=True)
if st.button('Calculate Risk'):
    probability, credit_score, rating = predict(age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
                                                delinquency_ratio, credit_utilization_ratio, num_open_accounts,
                                                residence_type, loan_purpose, loan_type)

    st.markdown(f"<p style='color:black; font-weight:700;'>Default Probability: {probability:.2%}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:black; font-weight:700;'>Credit Score: {credit_score}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:black; font-weight:700;'>Rating: {rating}</p>", unsafe_allow_html=True)
