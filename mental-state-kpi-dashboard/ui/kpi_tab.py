from src.models.inference_engine import classify_state
import streamlit as st
import plotly.express as px
from src.data.data_generator import generate_data
from src.features.feature_engineering import compute_score
def show_kpi():
    df, kpi_df = generate_data()

    df["Score"] = df.apply(compute_score, axis=1)

    # Merge score into KPI table
    for idx, row in df.iterrows():
        kpi_df.loc[
            (kpi_df["Employee"] == row["Employee"]) &
            (kpi_df["Week"] == row["Week"]),
            "Score"
        ] = row["Score"]

    st.header("📊 KPI Dashboard Overview")

    st.dataframe(kpi_df)

    st.divider()

    # ============================
    # 🧠 EMOTION / MENTAL STATE TABLE
    # ============================
    st.subheader("🧠 Employee Mental State Overview")

    emotion_df = kpi_df.copy()

    emotion_df["Mental State"] = emotion_df["Score"].apply(classify_state)

    st.dataframe(
        emotion_df[["Employee", "Week", "Score", "Mental State"]],
        use_container_width=True
    )
