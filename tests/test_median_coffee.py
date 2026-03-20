import pytest

from median_statistic.reports.median_coffee import calculate_median_coffee


@pytest.mark.parametrize(
    "rows, excpected_result",
    [
        (
            [
                {"student": "Иванов", "coffee_spent": "100"},
                {"student": "Иванов", "coffee_spent": "300"},
                {"student": "Иванов", "coffee_spent": "200"},
                {"student": "Иванов", "coffee_spent": "400"},
            ],
            [("Иванов", 250.0)],
        ),
        (
            [
                {"student": "Иванов", "coffee_spent": "100"},
                {"student": "Иванов", "coffee_spent": "300"},
                {"student": "Иванов", "coffee_spent": "200"},
            ],
            [("Иванов", 200)],
        ),
    ],
    ids=[
        "Test even count values",
        "Test odd count values",
    ],
)
def test_calculate_median_coffee_for_even_count_values(rows, excpected_result):
    """Проверяем расчёт медианы при чётном и нечётном количестве дней."""
    # Act
    result = calculate_median_coffee(rows)
    # Assert
    assert result == excpected_result


def test_calculate_median_coffee_sorts_by_median_descending():
    """Проверяем сортировку студентов по убыванию медианы."""
    # Arrange
    rows = [
        {"student": "Иванов", "coffee_spent": "100"},
        {"student": "Иванов", "coffee_spent": "200"},
        {"student": "Петров", "coffee_spent": "500"},
        {"student": "Петров", "coffee_spent": "700"},
        {"student": "Сидоров", "coffee_spent": "300"},
        {"student": "Сидоров", "coffee_spent": "300"},
    ]

    # Act
    result = calculate_median_coffee(rows)

    # Assert
    assert result == [
        ("Петров", 600.0),
        ("Сидоров", 300.0),
        ("Иванов", 150.0),
    ]
