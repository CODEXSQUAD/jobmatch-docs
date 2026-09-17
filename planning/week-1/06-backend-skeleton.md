# Создать backend-каркас и endpoint /health

- **Репозиторий Issue:** `jobmatch-backend`
- **Ответственный:** Клим
- **Срок:** День 2
- **Проверяет:** Альберт

## Описание

Подготовить запускаемый ASP.NET Core проект для дальнейшей реализации API.

## Что сделать

- После утверждения стека создать solution и проекты Api, Application, Domain, Infrastructure.
- Настроить зависимости между проектами.
- Реализовать GET /health.
- Подключить OpenAPI и Swagger UI.
- Подготовить конфигурацию разработки и зафиксировать версию SDK.
- Обновить README: инструменты, команды сборки и запуска, адреса проверки.

## Критерии готовности

- [ ] Проект собирается без ошибок.
- [ ] API запускается по README.
- [ ] GET /health возвращает 200 OK.
- [ ] Swagger открывается и показывает реализованные endpoints.
- [ ] Альберт воспроизвёл запуск.

## Входные файлы

- [Ответственность репозиториев](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/architecture/repositories.md).
- [MVP и решения по стеку](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/requirements/mvp.md).
- [README backend](https://github.com/CODEXSQUAD/jobmatch-backend/blob/main/README.md).

## Зависимости от задач

- [Задача №1: Утвердить границы MVP и бизнес-правила JobMatch](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/planning/week-1/01-mvp.md).

## Файлы результата

- [Инструкция backend](https://github.com/CODEXSQUAD/jobmatch-backend/blob/main/README.md) — существующий файл, обновляется в этой задаче.
