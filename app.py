import streamlit as st
import pandas as pd
from datetime import datetime
from PIL import Image
import os

# --- Logo and Banner ---
st.set_page_config(page_title="ShaadiKarwalo", layout="wide")

# Sidebar Logo
st.sidebar.image("logo.png", use_column_width=True)
st.sidebar.title("ShaadiKarwalo.com")
st.sidebar.markdown("India's Ultimate Wedding Planning App 💍")

# Banner Image
st.image("mandap.jpeg", use_column_width=True, caption="Plan Your Dream Wedding With Us")

# --- Form Header ---
st.title("🎉 Wedding Planning Form")

st.markdown("Please fill out the details below. We'll help you organize your big day effortlessly!")

# --- Form Input ---
with st.form("wedding_form"):
    name = st.text_input("Your Full Name")
    phone = st.text_input("Phone Number")
    email = st.text_input("Email")
    budget = st.selectbox("Your Total Budget", ["Under ₹8 Lakhs", "₹8–16 Lakhs", "₹16–25 Lakhs", "₹25–30 Lakhs", "Above ₹30 Lakhs"])
    city = st.text_input("Preferred City/Venue Location")
    guests = st.slider("Number of Guests", 50, 1000, 300)
    days = st.selectbox("Number of Functions", [1, 2, 3, 4, 5])
    cuisine = st.multiselect("Cuisine Preference", ["Vegetarian", "Non-Vegetarian", "Jain", "Continental", "Other"], default=["Vegetarian"])
    decor = st.radio("Preferred Decor Theme", ["Traditional", "Modern", "Minimal", "Lavish"])
    extra = st.text_area("Anything else you'd like us to know?", placeholder="E.g. Destination wedding, celebrity performances, etc.")
    
    submitted = st.form_submit_button("Submit")

    if submitted:
        # Save to CSV
        entry = {
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Name": name,
            "Phone": phone,
            "Email": email,
            "Budget": budget,
            "City": city,
            "Guests": guests,
            "Functions": days,
            "Cuisine": ", ".join(cuisine),
            "Decor": decor,
            "Extras": extra
        }

        df = pd.DataFrame([entry])
        file_exists = os.path.isfile("submissions.csv")
        df.to_csv("submissions.csv", mode='a', header=not file_exists, index=False)

        st.success("✅ Your wedding request has been submitted! Our team will reach out to you soon.")
        st.balloons()
