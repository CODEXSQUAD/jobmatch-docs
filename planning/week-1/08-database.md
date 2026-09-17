# Подключить PostgreSQL и создать начальную миграцию

- **Репозиторий Issue:** `jobmatch-backend`
- **Ответственный:** Клим
- **Срок:** День 3
- **Проверяет:** Матвей и Альберт

## Описание

Реализовать принятую схему средствами EF Core и обеспечить её создание в пустой БД.

## Что сделать

- Подключить EF Core и Npgsql; создать DbContext.
- Реализовать модели и конфигурации согласованной начальной схемы.
- Настроить ключи, связи, индексы и ограничения.
- Создать начальную миграцию.
- Вынести параметры подключения в конфигурацию.
- Описать применение миграции в README.
- При изменении схемы обновить ERD и словарь данных через связанный PR.

## Критерии готовности

- [ ] Backend подключается к PostgreSQL.
- [ ] Миграция создаёт схему в пустой БД.
- [ ] Схема соответствует ERD и словарю данных.
- [ ] Уникальность и связи реализованы.
- [ ] Реальные пароли не включены в репозиторий.
- [ ] Матвей проверил таблицы и связи.

## Входные файлы

- [Организация кода и БД](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/architecture/repositories.md).
- [README backend](https://github.com/CODEXSQUAD/jobmatch-backend/blob/main/README.md).

## Зависимости от задач

- [Задача №3: Подготовить ERD и словарь данных](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/planning/week-1/03-erd.md).
- [Задача №6: Создать backend-каркас и endpoint /health](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/planning/week-1/06-backend-skeleton.md).

## Файлы результата

- [Инструкция миграций](https://github.com/CODEXSQUAD/jobmatch-backend/blob/main/README.md) — существующий файл, обновляется в этой задаче.

## Согласованная схема для реализации

- [ERD](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/architecture/erd.md) — планируемый файл из задачи №3.
- [Словарь данных](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/architecture/data-dictionary.md) — планируемый файл из задачи №3.
