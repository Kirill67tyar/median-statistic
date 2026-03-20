"""Пакет с отчётами. Здесь регистрируются все поддерживаемые --report."""

from median_statistic.reports.median_coffee import calculate_median_coffee

REPORTS = {
    "median-coffee": calculate_median_coffee,
    # сюда легко добавлять новые отчёты в будущем:
    # "mean-sleep": calculate_mean_sleep,
}
