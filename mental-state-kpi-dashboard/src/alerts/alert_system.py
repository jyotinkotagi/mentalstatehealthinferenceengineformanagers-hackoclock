def check_alert(emp_df):
    scores = emp_df["Score"].values
    decline = 0

    for i in range(1, len(scores)):
        if scores[i] < scores[i-1]:
            decline += 1
        else:
            decline = 0

    if decline >= 3:
        reasons = []
        if emp_df.iloc[-1]["ResponseLatency"] > emp_df["ResponseLatency"].mean():
            reasons.append("Latency increased")
        if emp_df.iloc[-1]["TasksCompleted"] < emp_df["TasksCompleted"].mean():
            reasons.append("Tasks decreased")
        if emp_df.iloc[-1]["MeetingParticipation"] < emp_df["MeetingParticipation"].mean():
            reasons.append("Participation dropped")
        return True, reasons

    return False, []