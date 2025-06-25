import streamlit as st
from datetime import datetime

# Set your anniversary date here
anniversary = datetime(2021, 6, 24, 20, 0, 0)

st.set_page_config(page_title="Our Time Together ❤️", layout="centered")

st.title("💖 Our Anniversary Clock 💖")

now = datetime.now()
delta = now - anniversary

seconds = int(delta.total_seconds())
minutes = seconds // 60
hours = minutes // 60
days = delta.days
weeks = days // 7
months = days // 30  # rough estimate
years = days // 365  # rough estimate

st.markdown(f"""
- **Years:** {years}
- **Months:** {months}
- **Weeks:** {weeks}
- **Days:** {days}
- **Hours:** {hours}
- **Minutes:** {minutes}
- **Seconds:** {seconds}
""")

st.caption(f"Together since: {anniversary.strftime('%B %d, %Y at %I:%M %p')}")

# Optional: Auto-refresh every second (Streamlit only allows manual refresh unless you use workaround)
st.button("Refresh")  # Manual refresh
