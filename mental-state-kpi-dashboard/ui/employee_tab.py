import streamlit as st
from src.data.data_generator import generate_data

def show_employee():
    _, kpi_df = generate_data()

    st.header("Employee Analytics")

    emp = st.selectbox("Employee", kpi_df["Employee"].unique(), key="employee_emp")

    st.dataframe(kpi_df[kpi_df["Employee"] == emp])
