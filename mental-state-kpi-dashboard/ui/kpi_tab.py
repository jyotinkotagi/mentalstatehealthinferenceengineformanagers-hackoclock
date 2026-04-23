import streamlit as st
import plotly.express as px
from src.data.data_generator import generate_data
from src.features.feature_engineering import compute_score

def show_kpi():
    df, kpi_df = generate_data()

    df["Score"] = df.apply(compute_score, axis=1)

    for idx, row in df.iterrows():
        kpi_df.loc[(kpi_df["Employee"] == row["Employee"]) & 
                   (kpi_df["Week"] == row["Week"]), "Score"] = row["Score"]

    st.header("Mental Health Overview")

    st.dataframe(kpi_df)