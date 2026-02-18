import streamlit as st
import pandas as pd 
from datetime import datetime
from src.aggent import WaterIntakeAgent
from src.database import log_intake, get_intake_history

st.set_page_config(
    page_title="AI Water Tracker",
    page_icon="💧",
    layout="wide"
)

if 'tracker_started'not in st.session_state:
    st.session_state.tracker_started = False


if not st.session_state.tracker_started:
    st.title("💧 AI Water Tracker Agent")

    st.markdown("""
    ### Stay Hydrated. Stay Healthy.

    Track your daily hydration with an intelligent AI assistant.
    Log your intake, analyze patterns, and improve your health effortlessly.
    """)

    col1, col2, col3 = st.columns(3)
    col1.metric("Daily Goal", "2000 ml")
    col2.metric("AI Powered", "✔")
    col3.metric("History Tracking", "✔")

    st.markdown("---")

    if st.button("🚀 Start Tracking"):
        st.session_state.tracker_started = True
        st.rerun()
    

else:
    st.title("💧 AI Water Tracker Dashboard")

   #Side bar : intake input 
    st.sidebar.header('Log your water intake') 
    user_id = st.sidebar.text_input('User ID',value = 'user_123')
    intake_ml = st.sidebar.number_input('Water Intake(ml)',min_value = 0,step = 100)

    if st.sidebar.button('Submit'):
        if user_id and intake_ml:
            log_intake(user_id,intake_ml)
            st.success(f"Logged {intake_ml}ml for {user_id}")

            agent = WaterIntakeAgent()
            feedback = agent.analyze_intake(intake_ml)
            st.info(f" AI Feedback: {feedback}")


    # Divider
    st.markdown("....")

   # history section
    st.header("📊 water Intake history")

    if user_id:
        history = get_intake_history(user_id)
        if history:
            dates = [datetime.strptime(row[1],"%Y-%m-%d") for row in history] 
            values = [row[0] for row in history]

            df = pd.DataFrame({
                'Date':dates,
                "Water Intake (ml)":values
            })

            st.dataframe(df)
            st.line_chart(df,x = 'Date',y = 'Water Intake (ml)')
        else :
            st.warning("no watter intake date found. Please log your intake first.")

