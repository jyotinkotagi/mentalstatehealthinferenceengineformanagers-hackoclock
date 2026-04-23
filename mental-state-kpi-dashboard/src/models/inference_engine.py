def classify_state(score):
    if score >= 75:
        return "🟢 Healthy"
    elif score >= 50:
        return "🟠 low stress"
    else:
        return "🔴 Burnout Risk"
