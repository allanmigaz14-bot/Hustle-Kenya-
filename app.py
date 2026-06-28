import streamlit as st

st.set_page_config(page_title="Side Hustle Finder", page_icon="💰")

st.title("💰 Side Hustle Finder for Kenya")
st.subheader("Answer 3 questions. Get your personalized money plan.")

skills = st.multiselect("What skills do you have?", 
    ["writing", "design", "sales", "canva", "research", "english", "blogging", "negotiating", "fixing stuff"])

hours = st.slider("How many hours/week can you work?", 5, 40, 10)

budget = st.number_input("What's your budget in KSh?", min_value=0, max_value=50000, value=1000)

hustles = [
    {
        "name": "Etsy Digital Printables",
        "skills": ["design", "writing", "canva"],
        "min_hours": 5, "max_hours": 20,
        "min_budget": 0, "max_budget": 50,
        "free_tip": "Use free Canva to make wall art. Sell on Etsy for $3-10 each.",
        "paid_plan": "9", "link": "https://connectorlink.online/a/31nR6UmLVHQR9Z"
    },
    {
        "name": "AI-Assisted Freelance Writing",
        "skills": ["writing", "research", "english", "blogging"],
        "min_hours": 10, "max_hours": 40,
        "min_budget": 0, "max_budget": 0,
        "free_tip": "Make a free Upwork profile. Use ChatGPT to write samples.",
        "paid_plan": "12", "link": "https://connectorlink.online/a/31nR6UmLVHQR9Z"
    },
    {
        "name": "Phone Flipping Kenya", 
        "skills": ["sales", "negotiating", "fixing stuff"],
        "min_hours": 5, "max_hours": 20,
        "min_budget": 200, "max_budget": 1000,
        "free_tip": "Start with 1 phone. Buy on Jiji, fix screen, resell for 40% profit.",
        "paid_plan": "7", "link": "https://connectorlink.online/a/31nR6UmLVHQR9Z"
    }
]

if st.button("Find My Hustle", type="primary"):
    matches = []
