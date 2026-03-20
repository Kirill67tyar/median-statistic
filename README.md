# median-statistic
CLI-скрипт для расчёта медианы трат на кофе по студентам.
Архитектура через REPORTS позволяет легко добавлять новые отчёты.
Все ключевые сценарии покрыты тестами (pytest).

### Запуск
```bash
make run
```
или 
```bash
poetry run python -m median_statistic.main \
  --files test-files/math.csv test-files/physics.csv test-files/programming.csv \
  --report median-coffee
```
### Запуск тестов:
```bash
make test
```
или
```bash
poetry run pytest
```