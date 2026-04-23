def compute_score(row):
    latency_score = max(0, 100 - row["ResponseLatency"] * 15)
    task_score = min(100, row["TasksCompleted"] * 8)
    meeting_score = row["MeetingParticipation"]

    return round(0.4 * task_score + 0.3 * meeting_score + 0.3 * latency_score, 2)