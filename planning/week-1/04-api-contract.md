# Подготовить OpenAPI-контракт основных сценариев

- **Репозиторий Issue:** `jobmatch-docs`
- **Ответственный:** Альберт
- **Срок:** Основные договорённости — день 2; полный черновик — день 3
- **Проверяет:** Клим, Влад и Игорь

## Описание

Согласовать запросы и ответы между frontend и backend до реализации функциональности.

## Что сделать

- Создать api/openapi.yaml.
- Описать регистрацию, вход, текущего пользователя, резюме, компании, вакансии, отклики и остаток лимита.
- Для каждого endpoint указать метод, путь, параметры, тело запроса, ответы и примеры.
- Указать обязательные поля, роли, ограничения, формат ошибок и пагинации.
- В первую очередь согласовать GET /health и GET /api/vacancies.
- В api/README.md перечислить реализованные и пока запланированные endpoints, чтобы их не путали на защите.

## Критерии готовности

- [ ] OpenAPI открывается в инструменте просмотра без ошибок.
- [ ] Основные сценарии MVP покрыты.
- [ ] Для каталога определены фильтры и формат пагинации.
- [ ] Frontend-разработчики понимают данные; Клим подтвердил реализацию.
- [ ] Запланированные endpoints явно обозначены.

## Входные файлы

- [MVP](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/requirements/mvp.md).
- [Правила ведения контрактов](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/api/README.md).
- [Организация репозиториев](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/architecture/repositories.md).

## Зависимости от задач

- [Задача №1: Утвердить границы MVP и бизнес-правила JobMatch](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/planning/week-1/01-mvp.md).
- [Задача №2: Описать пользовательские сценарии и права доступа MVP](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/planning/week-1/02-use-cases.md).
- [Задача №3: Подготовить ERD и словарь данных](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/planning/week-1/03-erd.md).

Можно начать по MVP; сценарии и ERD нужны для окончательной сверки. Формат ответа каталога зафиксировать до начала его реализации.

## Файлы результата

- [OpenAPI-контракт](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/api/openapi.yaml) — планируемый файл, создаётся при выполнении задачи.
- [Статус API](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/api/README.md) — существующий файл, обновляется в этой задаче.

## Документы для сверки после выполнения зависимостей

- [Сценарии](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/requirements/use-cases.md) — создаёт задача №2.
- [Права](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/requirements/permissions.md) — создаёт задача №2.
- [ERD](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/architecture/erd.md) — создаёт задача №3.
- [Словарь данных](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/architecture/data-dictionary.md) — создаёт задача №3.
