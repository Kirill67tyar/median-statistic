.PHONY: format check test run all

all: format check test

format:
	poetry run ruff format median_statistic tests
	poetry run ruff check --fix median_statistic tests

check:
	poetry run ruff format --check median_statistic tests
	poetry run ruff check median_statistic tests

test:
	poetry run pytest

run:
	poetry run python -m median_statistic.main \
		--files test-files/math.csv test-files/physics.csv test-files/programming.csv \
		--report median-coffee