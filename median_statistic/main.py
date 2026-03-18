import os
import argparse
import csv
import sys


def load_data(file_paths: list[str]) -> list[dict]:
    for path in file_paths:
        try:
            with open(path, newline="", encoding="utf-8") as f:
                return list(csv.DictReader(f))
        except FileNotFoundError as e:
            print(e)
            sys.exit(1)
        except Exception as e:
            print(e)
            sys.exit(1)
    return []

def main():
    parser = argparse.ArgumentParser(description="Отчёт о потреблении кофе")
    parser.add_argument("--files", nargs="+", required=True,
                        help="Пути к CSV-файлам (можно несколько)")
    parser.add_argument("--report", required=True,
                        help="Название отчёта (сейчас только median-coffee)")

    arguments = parser.parse_args()
    raw_data = load_data(arguments.files)
    # path = os.path.abspath(__file__)
    
    pass

if __name__ == "__main__":
    main()
