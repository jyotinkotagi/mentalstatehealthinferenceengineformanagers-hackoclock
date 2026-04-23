import streamlit as st
import plotly.express as px
from src.data.data_generator import generate_data
from src.features.feature_engineering import compute_score

def show_trends():
    df, _ = generate_data()

    df["Score"] = df.apply(compute_score, axis=1)

    trend = df.groupby("Week")["Score"].mean()

    fig = px.line(x=trend.index, y=trend.values)

    st.plotly_chart(fig)