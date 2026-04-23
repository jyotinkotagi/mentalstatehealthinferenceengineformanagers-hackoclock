import streamlit as st
from src.data.data_generator import generate_data
from src.features.feature_engineering import compute_score
from src.alerts.alert_system import check_alert

def show_mental():
    df, _ = generate_data()

    df["Score"] = df.apply(compute_score, axis=1)

    st.header("Mental State Analysis")

    emp = st.selectbox("Employee", df["Employee"].unique(), key="mental_emp")
    emp_df = df[df["Employee"] == emp]

    st.line_chart(emp_df.set_index("Week")["Score"])

    alert, reasons = check_alert(emp_df)

    if alert:
        st.error("⚠️ Issue detected")
    else:
        st.success("✅ OK")