## Описание
- Этот проект разрабатывается для автоматизации торговли и помощи в выборе финансовых инструментов, а также для
    отработки навыков работы с сервисами

# Структура проекта (проект состоит из микросервисов)
- `fast_api`, фреймворк FastAPI и логика проекта (интерфейс взаимодействия с сервисами, обработка логики проекта).
- `redis`, служит для взаимодействия между микросервисами.
- `moex_parser`, разработан на Python(парсит данные с MOEX) и отдает их микросервису `redis`.