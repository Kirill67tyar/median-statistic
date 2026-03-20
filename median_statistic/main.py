import argparse
import csv
import sys
from median_statistic.median_coffee.median_coffee import calculate_median_coffee
from tabulate import tabulate


OUTPUT_FUNCS = {
    "median-coffee": calculate_median_coffee,
}


def load_data(file_paths: list[str]) -> list[dict]:
    result = []
    for path in file_paths:
        try:
            with open(path, newline="", encoding="utf-8") as f:
                result.extend(list(csv.DictReader(f)))
        except FileNotFoundError as e:
            print(e)
            sys.exit(1)
        except Exception as e:
            print(e)
            sys.exit(1)
    return result


def main():
    parser = argparse.ArgumentParser(description="Отчёт о потреблении кофе")
    parser.add_argument("--files", nargs="+", required=True,
                        help="Пути к CSV-файлам (можно несколько)")
    parser.add_argument("--report", required=True,
                        help="Название отчёта (сейчас только median-coffee)")
    arguments = parser.parse_args()
    raw_data = load_data(arguments.files)
    output_func = OUTPUT_FUNCS.get(arguments.report)
    if not output_func:
        print("Некорректный аргумент")
        sys.exit(1)
    result = output_func(raw_data)
    print(
        tabulate(
            result,
            headers=["student", "median_coffee",],
            tablefmt="grid",
        )
    )


if __name__ == "__main__":
    main()
