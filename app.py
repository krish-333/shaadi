
import streamlit as st

st.set_page_config(page_title="ShaadiKarwalo.com", layout="centered")

# App Header
st.title("💍 ShaadiKarwalo.com")
st.markdown("### India’s Simplest Wedding Planning App")

st.image("https://i.imgur.com/5bT3hYk.png", use_column_width=True)  # Placeholder banner image

st.markdown("---")
st.header("📦 Wedding Packages")
packages = {
    "Budget Package (₹8L)": [
        "Venue coordination (Local)",
        "Catering (Vegetarian)",
        "Basic decor & sound",
        "Photography (1 day)"
    ],
    "Classic Package (₹16L)": [
        "Venue + Catering (Multi-day)",
        "Enhanced decor",
        "Makeup, Mehandi",
        "Photography + Cinematic Video"
    ],
    "Premium Package (₹25L)": [
        "Destination venue options",
        "3-day event planning",
        "Premium photography, reels",
        "Luxury decor & artists"
    ],
    "Royal Package (₹30L)": [
        "Luxury destination (India)",
        "Outfit styling + transport",
        "Celebrity anchoring options",
        "Dedicated planning manager"
    ],
    "Elite Package (₹50L+)": [
        "Global destination",
        "Luxury travel & hotels",
        "Designer wear",
        "End-to-end execution"
    ]
}

for name, details in packages.items():
    with st.expander(name):
        for item in details:
            st.markdown(f"- {item}")

st.markdown("---")
st.header("✨ Add-ons (Optional)")
add_ons = [
    "Fireworks / Varmala Entry",
    "Drone Videography",
    "Luxury Car Rentals",
    "Eco-friendly Decor",
    "Live Streaming for Guests"
]
for item in add_ons:
    st.markdown(f"- {item}")

st.markdown("---")
st.header("📝 Customer Inquiry Form")
with st.form("customer_form"):
    name = st.text_input("Your Name")
    phone = st.text_input("Phone Number")
    selected_package = st.selectbox("Select Wedding Package", list(packages.keys()))
    message = st.text_area("Any specific requests?")
    submitted = st.form_submit_button("Submit Inquiry")
    if submitted:
        st.success(f"Thanks {name}, we will contact you shortly at {phone}!")

st.markdown("---")
st.header("🤝 Vendor Registration")
with st.form("vendor_form"):
    vendor_name = st.text_input("Vendor Name")
    service_type = st.selectbox("Service Type", ["Makeup", "Photography", "Venue", "Catering", "Decor", "Other"])
    location = st.text_input("City / Region")
    vendor_phone = st.text_input("Contact Number")
    registered = st.form_submit_button("Register Vendor")
    if registered:
        st.success(f"Thanks {vendor_name}, your service will be reviewed and listed!")

st.markdown("---")
st.caption("Made with ❤️ by the ShaadiKarwalo Team")
