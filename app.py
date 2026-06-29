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
    st.success("✅ All 8 Hustles For You:")
    
    st.markdown("### 1. CV Writing Service")
    st.write("**Potential:** KSh 15,000-45,000/month | **Budget:** KSh 0 | **Time:** 5hrs/week")
    st.caption("Write CVs for graduates on Fiverr. Zero startup cost.")
    
    st.markdown("### 2. Canva Social Media Posts")
    st.write("**Potential:** KSh 10,000-30,000/month | **Budget:** KSh 500 | **Time:** 8hrs/week")
    st.caption("Design Instagram posts for small businesses using free Canva.")
    
    st.markdown("### 3. Academic Research Assistant")
    st.write("**Potential:** KSh 20,000-60,000/month | **Budget:** KSh 0 | **Time:** 10hrs/week")
    st.caption("Help Masters students with data collection & analysis.")
    
    st.markdown("### 4. Transcription Services")
    st.write("**Potential:** KSh 8,000-25,000/month | **Budget:** KSh 0 | **Time:** 6hrs/week")
    st.caption("Convert audio to text for podcasts, interviews, meetings.")
    
    st.markdown("### 5. Online Tutoring")
    st.write("**Potential:** KSh 12,000-40,000/month | **Budget:** KSh 0 | **Time:** 8hrs/week")
    st.caption("Teach KCSE subjects or English to students via Zoom.")
    
    st.markdown("### 6. Article/Blog Writing")
    st.write("**Potential:** KSh 18,000-50,000/month | **Budget:** KSh 0 | **Time:** 10hrs/week")
    st.caption("Write 500-word articles for blogs & websites at $5-20 each.")
    
    st.markdown("### 7. Virtual Assistant")
    st.write("**Potential:** KSh 15,000-35,000/month | **Budget:** KSh 0 | **Time:** 10hrs/week")
    st.caption("Manage emails, scheduling, data entry for busy clients.")
    
    st.markdown("### 8. Proofreading & Editing")
    st.write("**Potential:** KSh 10,000-30,000/month | **Budget:** KSh 0 | **Time:** 6hrs/week")
    st.caption("Fix grammar & structure for student essays and business docs.")
    
    st.balloons()
    st.info("💡 Tip: Start with 1 hustle. Master it before adding another.")
