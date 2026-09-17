# Подготовить демонстрацию и проверить готовность ко второй лабораторной

- **Репозиторий Issue:** `jobmatch-docs`
- **Ответственный:** Матвей
- **Срок:** Дни 6–7
- **Проверяет:** Клим; участвует вся команда

## Описание

Собрать комплект материалов защиты и воспроизвести запуск. Игорь выполняет техническую проверку окружения, Клим помогает с интеграцией; Матвей координирует результат.

## Что сделать

- Создать demo/lab-2.md с рассказом: проблема → MVP → сценарии → ERD → API → дизайн → работающая основа → roadmap.
- Записать шаги демонстрации и ссылки на команды запуска.
- Проверить ссылки на документы, Figma и репозитории.
- Провести запуск по README в чистом Linux-окружении с 8 ГБ RAM.
- Проверить цепочку: браузер → API → PostgreSQL → вакансии на странице.
- Назначить исправления обнаруженных проблем и проверить результат.
- Провести репетицию: каждый участник объясняет свой вклад и принятые решения.
- Отдельно обозначить реализованные и будущие функции.

## Критерии готовности

- [ ] Все обязательные материалы доступны.
- [ ] Запуск воспроизведён в согласованном окружении.
- [ ] Каталог получает данные из PostgreSQL через API.
- [ ] Команда провела репетицию.
- [ ] У каждого участника виден вклад.
- [ ] Блокирующие проблемы устранены.

## Входные файлы

- [MVP](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/requirements/mvp.md).
- [Команда](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/planning/team.md).
- [Roadmap](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/planning/roadmap.md).
- [Статус API](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/api/README.md).
- [Дизайн](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/design/README.md).
- [README backend](https://github.com/CODEXSQUAD/jobmatch-backend/blob/main/README.md).
- [README frontend](https://github.com/CODEXSQUAD/jobmatch-frontend/blob/main/README.md).

## Зависимости от задач

- [Задача №1: Утвердить границы MVP и бизнес-правила JobMatch](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/planning/week-1/01-mvp.md).
- [Задача №2: Описать пользовательские сценарии и права доступа MVP](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/planning/week-1/02-use-cases.md).
- [Задача №3: Подготовить ERD и словарь данных](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/planning/week-1/03-erd.md).
- [Задача №4: Подготовить OpenAPI-контракт основных сценариев](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/planning/week-1/04-api-contract.md).
- [Задача №5: Подготовить первичные макеты и пользовательские потоки](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/planning/week-1/05-design.md).
- [Задача №6: Создать backend-каркас и endpoint /health](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/planning/week-1/06-backend-skeleton.md).
- [Задача №7: Создать frontend-каркас и подключить проверку backend](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/planning/week-1/07-frontend-skeleton.md).
- [Задача №8: Подключить PostgreSQL и создать начальную миграцию](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/planning/week-1/08-database.md).
- [Задача №9: Добавить тестовые данные и API списка вакансий](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/planning/week-1/09-vacancies-api.md).
- [Задача №10: Реализовать каталог с данными backend](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/planning/week-1/10-vacancies-ui.md).
- [Задача №11: Настроить совместный запуск через Docker Compose](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/planning/week-1/11-compose.md).
- [Задача №12: Настроить автоматическую проверку сборки frontend и backend](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/planning/week-1/12-ci.md).
- [Задача №13: Актуализировать roadmap и GitHub Projects](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/planning/week-1/13-roadmap.md).

Сценарий защиты можно готовить раньше. Итоговая проверка выполняется после готовности всех материалов и окружения.

## Файлы результата

- [Сценарий второй лабораторной](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/demo/lab-2.md) — планируемый файл, создаётся при выполнении задачи.

## Материалы после выполнения зависимостей

- [Сценарии](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/requirements/use-cases.md) — задача №2.
- [Права](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/requirements/permissions.md) — задача №2.
- [ERD](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/architecture/erd.md) — задача №3.
- [Словарь данных](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/architecture/data-dictionary.md) — задача №3.
- [OpenAPI](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/api/openapi.yaml) — задача №4.
- [Compose](https://github.com/CODEXSQUAD/jobmatch-backend/blob/main/compose.yaml) — задача №11.

Эти файлы пока запланированы; к итоговой проверке должны существовать.
