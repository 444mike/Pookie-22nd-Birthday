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

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #ffe4ec, #e0f7fa);
        color: #333333;
    }

    h1, h2, h3, .stMarkdown, .stMarkdown p {
        color: #222222 !important;
        text-shadow: 1px 1px 2px #ffffff80;
    }

    .stMarkdown ul li {
        color: #444444 !important;
        font-size: 20px;
    }

    .highlight {
        font-size: 22px;
        font-weight: bold;
        color: #c71585;
        text-align: center;
    }

    header, footer {
        visibility: hidden;
        display: none;
    }
    </style>
""", unsafe_allow_html=True)





st_autorefresh(interval=1000, limit=None, key="refresh")


st.markdown("<h1>💖 Our Anniversary Clock 💖</h1>", unsafe_allow_html=True)


# Main breakdown
rd = relativedelta(now, anniversary)
years = rd.years
months = rd.months
days = rd.days
hours = rd.hours
minutes = rd.minutes
seconds = rd.seconds

# Display in Streamlit
st.subheader("🕰️ Time We've Been Together:")
st.markdown(f"""
    <div style='text-align: center; font-size: 26px;'>
        <p><strong>{years}</strong> years, <strong>{months}</strong> months, <strong>{days}</strong> days, <strong>{hours}</strong> hours, <strong>{minutes}</strong> minutes, <strong>{seconds}</strong> seconds</p>
    </div>
""", unsafe_allow_html=True)


delta = now - anniversary

seconds = int(delta.total_seconds())
minutes = seconds // 60
hours = minutes // 60
days = delta.days
weeks = days // 7
months = days // 30  # rough estimate

st.markdown(f"""
- **Months:** {months}
- **Weeks:** {weeks}
- **Days:** {days}
- **Hours:** {hours}
- **Minutes:** {minutes}
- **Seconds:** {seconds}
""")

st.caption(f"Together since: {anniversary.strftime('%B %d, %Y at %I:%M %p')}")
