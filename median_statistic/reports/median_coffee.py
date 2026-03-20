import statistics
from collections import defaultdict


def calculate_median_coffee(rows: list[dict]) -> list[tuple[str, float | int]]:
    """
    Вычисляет медиану трат на кофе для каждого студента
    и возвращает список, отсортированный по убыванию.
    """
    coffee_by_student = defaultdict(list)

    for row in rows:
        student = row["student"]
        coffee_by_student[student].append(int(row["coffee_spent"]))

    medians = []
    for student, spends in coffee_by_student.items():
        if spends:
            medians.append((student, statistics.median(spends)))

    medians.sort(key=lambda x: x[-1], reverse=True)
    return medians
