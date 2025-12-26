from typing import List
from datetime import datetime

def parse_date(date_str: str) -> datetime:
    try:
        return datetime.strptime(date_str, "%d.%m.%Y")
    except ValueError:
        raise ValueError(f"Некорректный формат даты: {date_str}. Ожидается DD.MM.YYYY")

def deadline_score(pass_date: str, deadline_date: str) -> int:
    submission = parse_date(pass_date)
    deadline = parse_date(deadline_date)

    if submission <= deadline:
        return 5

    days_late = (submission - deadline).days
    weeks_late = (days_late + 6) // 7

    score = 5 - weeks_late
    return max(0, score)

def late_list(grades: dict, deadline_date: str) -> List[str]:
    deadline = parse_date(deadline_date)
    late_students = []

    for student, pass_date in grades.items():
        submission = parse_date(pass_date)
        if submission > deadline:
            late_students.append(student)

    return sorted(late_students)
