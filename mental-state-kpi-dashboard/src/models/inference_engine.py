def classify_state(score):
    if score >= 75:
        return "Healthy"
    elif score >= 50:
        return "At Risk"
    else:
        return "Critical"