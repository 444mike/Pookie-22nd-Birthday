import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
from dateutil.relativedelta import relativedelta
from datetime import datetime

# current time
now = datetime.now()



# Set your anniversary date here
anniversary = datetime(2022, 11, 25)


st.set_page_config(page_title="Our Time Together ❤️", layout="centered")
st_autorefresh(interval=1000, limit=None, key="refresh")


st.title("💖 Our Anniversary Clock 💖")

# Calculate detailed duration
rd = relativedelta(now, anniversary)

years = rd.years
months = rd.months
days = rd.days

st.subheader("🕰️ Time We've Been Together")
st.markdown(f"{years} years, {months} months, {days} days")

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
