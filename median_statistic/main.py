import argparse
import csv
import sys

from tabulate import tabulate

from median_statistic import REPORTS


def load_data(file_paths: list[str]) -> list[dict]:
    """Читает все переданные CSV-файлы и объединяет строки."""
    all_data = []
    for path in file_paths:
        try:
            with open(path, newline="", encoding="utf-8") as f:
                all_data.extend(list(csv.DictReader(f)))
        except FileNotFoundError:
            print(f"Ошибка: файл не найден — {path}")
            sys.exit(1)
        except Exception as e:
            print(f"Ошибка чтения файла {path}: {e}")
            sys.exit(1)
    return all_data


def main() -> None:
    """Точка входа. Парсит аргументы и формирует отчёт."""
    parser = argparse.ArgumentParser(description="Отчёт о потреблении кофе")
    parser.add_argument(
        "--files", nargs="+", required=True, help="Пути к CSV-файлам (можно несколько)"
    )
    parser.add_argument(
        "--report", required=True, help="Название отчёта (сейчас только median-coffee)"
    )
    arguments = parser.parse_args()
    raw_data = load_data(arguments.files)
    report_func = REPORTS.get(arguments.report)
    if not report_func:
        print(f"Некорректный аргумент --report: {arguments.report}")
        print(f"Доступные отчёты: {list(REPORTS.keys())}")
        sys.exit(1)
    result_output = report_func(raw_data)
    print(
        tabulate(
            result_output,
            headers=[
                "student",
                "median_coffee",
            ],
            tablefmt="grid",
        )
    )


if __name__ == "__main__":
    main()
