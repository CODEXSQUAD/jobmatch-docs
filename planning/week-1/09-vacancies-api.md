# Добавить тестовые данные и API списка вакансий

- **Репозиторий Issue:** `jobmatch-backend`
- **Ответственный:** Альберт
- **Срок:** День 4
- **Проверяет:** Клим

## Описание

Реализовать чтение вакансий из PostgreSQL и подготовить вымышленные данные для демонстрации.

## Что сделать

- Добавить вымышленные компании, работодателей и вакансии с корректными связями.
- Подготовить вакансии разных городов и форматов работы, а также черновик и закрытую вакансию для проверки.
- Реализовать GET /api/vacancies по контракту: DTO, опубликованные вакансии и пагинация.
- Зафиксировать поддерживаемые на этой неделе фильтры; остальные отметить как будущие.
- Сделать заполнение демонстрационными данными повторяемым без дубликатов.
- Описать заполнение и примеры запросов в README.
- Обновить статус реализованных endpoints в api/README.md.

## Критерии готовности

- [ ] API получает данные из БД, а не из списка в памяти.
- [ ] Формат ответа соответствует контракту.
- [ ] Черновики и закрытые вакансии не входят в активный каталог.
- [ ] Пагинация и пустая выдача работают.
- [ ] Повторное заполнение не создаёт дубликаты.
- [ ] Поддерживаемые фильтры описаны и проверены.

## Входные файлы

- [MVP](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/requirements/mvp.md).
- [Статус API](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/api/README.md).
- [README backend](https://github.com/CODEXSQUAD/jobmatch-backend/blob/main/README.md).

## Зависимости от задач

- [Задача №4: Подготовить OpenAPI-контракт основных сценариев](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/planning/week-1/04-api-contract.md).
- [Задача №8: Подключить PostgreSQL и создать начальную миграцию](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/planning/week-1/08-database.md).

## Файлы результата

- [Тестовые данные и запросы](https://github.com/CODEXSQUAD/jobmatch-backend/blob/main/README.md) — существующий файл, обновляется в этой задаче.
- [Статус API](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/api/README.md) — существующий файл, обновляется в этой задаче.

## Контракт для реализации

- [OpenAPI](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/api/openapi.yaml) — планируемый файл из задачи №4; использовать после согласования нужных endpoints.
