import streamlit as st
import os
from dotenv import load_dotenv
from google import genai
import time

st.set_page_config(
    page_title="Explore with AI",
    page_icon="🌎",
    layout="wide"
)

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)


def generate_itinerary(destination, days, nights):
    prompt = f"""
    Create a detailed {days}-day and {nights}-night travel itinerary for {destination}.

    Include:
    - Day-wise breakdown
    - Major attractions
    - Food recommendations
    - Travel tips
    - Best time to visit
    - Transportation suggestions

    Format clearly with headings and bullet points.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text


st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #1f4037, #99f2c8);
}

/* Hero Section */
.hero {
    text-align: center;
    padding: 40px 20px;
}

.hero-title {
    font-size: 55px;
    font-weight: 800;
    color: white;
}

.hero-subtitle {
    font-size: 20px;
    color: white;
    opacity: 0.9;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #0f2027;
    color: white;
}

/* Card Style */
.result-card {
    background: white;
    padding: 35px;
    border-radius: 20px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.3);
    margin-top: 20px;
}

/* Button */
.stButton>button {
    background: linear-gradient(45deg, #ff512f, #dd2476);
    color: white;
    font-size: 18px;
    border-radius: 10px;
    padding: 12px 20px;
    border: none;
}

.stButton>button:hover {
    background: linear-gradient(45deg, #dd2476, #ff512f);
}

</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="hero">
    <div class="hero-title">🌎 Explore with AI</div>
    <div class="hero-subtitle">Your Smart AI Travel Companion</div>
</div>
""", unsafe_allow_html=True)


st.sidebar.header("✈️ Plan Your Trip")

destination = st.sidebar.text_input("Enter Destination")
days = st.sidebar.number_input("Number of Days", min_value=1, value=3)
nights = st.sidebar.number_input("Number of Nights", min_value=1, value=2)

generate = st.sidebar.button("🚀 Generate Travel Plan")


if generate:
    if destination.strip() == "":
        st.warning("Please enter a destination.")
    else:
        with st.spinner("Generating your personalized travel experience..."):
            time.sleep(1)
            itinerary = generate_itinerary(destination, days, nights)

        st.markdown(f"""
        <div class="result-card">
            <h2>{destination} – {days} Days & {nights} Nights</h2>
            <hr>
            {itinerary}
        </div>
        """, unsafe_allow_html=True)

else:
    st.markdown("""
    ### 🌍 How It Works
    1. Enter your dream destination  
    2. Select number of days & nights  
    3. Click Generate  
    4. Get a complete AI-powered itinerary  

    ---
    💡 Perfect for vacations, weekend trips, and adventure planning!
    """)
