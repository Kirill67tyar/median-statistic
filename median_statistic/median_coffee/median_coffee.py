from collections import defaultdict
import statistics


def calculate_median_coffee(rows: list[dict]) -> list[tuple[str, float | int]]:
    coffee_by_student = defaultdict(list)

    for row in rows:
        student = row["student"]
        coffee_by_student[student].append(int(row["coffee_spent"]))

    medians = []
    for student, spends in coffee_by_student.items():
        if spends:
            median = statistics.median(spends)
            medians.append((student, median))

    medians.sort(key=lambda x: x[-1], reverse=True)
    return medians