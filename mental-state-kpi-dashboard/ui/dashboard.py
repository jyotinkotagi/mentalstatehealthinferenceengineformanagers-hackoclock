import streamlit as st
from ui.kpi_tab import show_kpi
from ui.mental_state_tab import show_mental
from ui.employee_tab import show_employee
from ui.trends_tab import show_trends

def run_dashboard():
    st.set_page_config(page_title="KPI Dashboard & Mental State", layout="wide")

    tab1, tab2, tab3, tab4 = st.tabs([
        "📊 KPI Dashboard",
        "🧠 Mental State",
        "👤 Employee Analytics",
        "📈 Trends"
    ])

    with tab1:
        show_kpi()

    with tab2:
        show_mental()

    with tab3:
        show_employee()

    with tab4:
        show_trends()