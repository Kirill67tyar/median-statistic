import pytest

from median_statistic.main import load_data, main


def test_main_happy_path_prints_table(tmp_path, monkeypatch, capsys, write_csv):
    """Проверяем, что при корректных аргументах выводится таблица с правильными данными."""
    # Arrange
    file1 = write_csv(
        tmp_path / "file1.csv",
        """student,coffee_spent
Петров,100
Петров,300
""",
    )
    file2 = write_csv(
        tmp_path / "file2.csv",
        """student,coffee_spent
Иванов,500
Иванов,700
""",
    )

    # подменяем sys.argv, как будто программу
    # запустили из терминала вот так:
    # python -m median_statistic/main.py --files file1.csv file2.csv --report median-coffee
    monkeypatch.setattr(
        "sys.argv",
        ["prog", "--files", str(file1), str(file2), "--report", "median-coffee"],
    )

    # Act
    main()

    # перехватываем stdout и stderr
    output = capsys.readouterr().out

    # Assert
    # Проверяем, что таблица действительно напечаталась
    # и что внутри есть ожидаемые данные.
    assert "Петров" in output
    assert "Иванов" in output
    assert "200" in output
    assert "600" in output
    assert "student" in output
    assert "median_coffee" in output


def test_load_data_exits_when_file_missing(capsys):
    """Несуществующий файл → sys.exit(1) с понятным сообщением."""
    # Arrange
    missing_file = "missing-file.csv"

    # Act
    # main() в этой ситуации должен завершиться через sys.exit(1),
    # поэтому используем pytest.raises(SystemExit).
    # Без этого pytest счёл бы завершение программы ошибкой теста.
    with pytest.raises(SystemExit) as exc_info:
        load_data([missing_file])

    # Assert
    assert exc_info.value.code == 1

    # Проверяем, что в консоль было выведено сообщение об ошибке
    captured = capsys.readouterr()
    assert f"Ошибка: файл не найден — {missing_file}" in captured.out


def test_main_exits_on_invalid_report(tmp_path, monkeypatch, capsys, write_csv):
    """Неверный --report → sys.exit(1) с перечислением доступных отчётов."""
    # Arrange
    file1 = write_csv(
        tmp_path / "file1.csv",
        """student,coffee_spent
Alice,100
""",
    )

    monkeypatch.setattr(
        "sys.argv",
        ["prog", "--files", str(file1), "--report", "unknown-report"],
    )

    # Act
    # main() в этой ситуации должен завершиться через sys.exit(1),
    # поэтому используем pytest.raises(SystemExit).
    # Без этого pytest счёл бы завершение программы ошибкой теста.
    with pytest.raises(SystemExit) as exc_info:
        main()

    # Assert
    assert exc_info.value.code == 1

    captured = capsys.readouterr()
    assert "Некорректный аргумент --report: unknown-report" in captured.out
