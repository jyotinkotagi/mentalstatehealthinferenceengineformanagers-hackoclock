def classify_state(score):
    if score >= 75:
        return "🟢 Healthy"
    elif score >= 50:
        return "🟠 low stress"
    else:
        return "🔴 Burnout Risk"
def get_recommendation(state):
    if state == "🟢 Healthy":
        return "Maintain performance"
    elif state == "🟠 At Risk":
        return "Suggest workload balance"
    else:
        return "Immediate manager intervention"
