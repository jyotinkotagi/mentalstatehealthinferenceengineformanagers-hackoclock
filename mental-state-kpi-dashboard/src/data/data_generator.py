import pandas as pd
import numpy as np

def generate_data():
    np.random.seed(42)

    employees = ["E1", "E2", "E3", "E4", "E5"]
    weeks = ["W1", "W2", "W3", "W4"]

    data = []
    kpi_data = []

    for emp in employees:
        base_latency = np.random.randint(1, 5)
        base_tasks = np.random.randint(8, 15)
        base_meet = np.random.randint(60, 90)
        base_productivity = np.random.randint(70, 95)
        base_quality = np.random.randint(80, 98)
        base_projects = np.random.randint(2, 5)

        for i, week in enumerate(weeks):
            decline = 1 - (i * np.random.uniform(0.05, 0.15))

            latency = base_latency * (1 + i * 0.2)
            tasks = base_tasks * decline
            meeting = base_meet * decline
            productivity = base_productivity * decline
            quality = base_quality * decline
            projects = max(1, int(base_projects * decline))
            revenue_generated = np.random.uniform(5000, 25000) * decline

            data.append([emp, week, latency, tasks, meeting])
            kpi_data.append({
                "Employee": emp,
                "Week": week,
                "Productivity": round(productivity, 2),
                "Quality": round(quality, 2),
                "ProjectsCompleted": projects,
                "RevenueGenerated": round(revenue_generated, 2),
                "TasksCompleted": tasks,
                "MeetingParticipation": meeting,
                "ResponseLatency": latency
            })

    df = pd.DataFrame(data, columns=[
        "Employee", "Week", "ResponseLatency",
        "TasksCompleted", "MeetingParticipation"
    ])

    kpi_df = pd.DataFrame(kpi_data)

    return df, kpi_df