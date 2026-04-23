import streamlit as st
from src.data.data_generator import generate_data
from src.features.feature_engineering import compute_score


def classify_state(score):
    if score >= 0.7:
        return "Positive"
    elif score >= 0.4:
        return "Neutral"
    else:
        return "Negative"


def get_recommendation(state):
    if state == "Positive":
        return "🟢 Maintain current performance"
    elif state == "Neutral":
        return "🟡 Monitor workload and stress levels"
    else:
        return "🔴 Provide support / reduce workload"


def show_kpi(kpi_df):
    emotion_df = kpi_df.copy()

    # compute score
    df, _ = generate_data()
    df["Score"] = df.apply(compute_score, axis=1)

    for idx, row in df.iterrows():
        emotion_df.loc[
            (emotion_df["Employee"] == row["Employee"]) &
            (emotion_df["Week"] == row["Week"]),
            "Score"
        ] = row["Score"]

    # safety fallback
    if "Score" not in emotion_df.columns:
        possible_cols = [col for col in emotion_df.columns if col.lower() == "score"]
        if possible_cols:
            emotion_df["Score"] = emotion_df[possible_cols[0]]
        else:
            raise ValueError("Score column missing")

    # mental state
    emotion_df["Mental State"] = emotion_df["Score"].apply(classify_state)

    # recommendation
    emotion_df["Recommendation"] = emotion_df["Mental State"].apply(get_recommendation)

    # UI (ONLY ONE TABLE)
    st.header("📊 KPI Dashboard Overview")
    st.dataframe(emotion_df)

    return emotion_df
