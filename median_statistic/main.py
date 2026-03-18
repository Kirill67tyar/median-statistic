import argparse
import csv

def main():
    parser = argparse.ArgumentParser(description="Отчёт о потреблении кофе")
    parser.add_argument("--files", nargs="+", required=True,
                        help="Пути к CSV-файлам (можно несколько)")
    parser.add_argument("--report", required=True,
                        help="Название отчёта (сейчас только median-coffee)")

    arguments = parser.parse_args()
    pass

if __name__ == "__main__":
    main()
