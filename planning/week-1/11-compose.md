# Настроить совместный запуск через Docker Compose

- **Репозиторий Issue:** `jobmatch-backend`
- **Ответственный:** Игорь
- **Срок:** День 4–5
- **Проверяет:** Клим

## Описание

Обеспечить совместный запуск frontend, backend и PostgreSQL по одной инструкции. Изменения также нужны в jobmatch-frontend; оба PR связать с этой Issue.

## Что сделать

- Создать Dockerfile backend и Dockerfile frontend со сборкой и Nginx.
- Создать compose.yaml в backend для трёх компонентов.
- Настроить перенаправление /api из Nginx к backend.
- Настроить volume PostgreSQL и безопасные примеры переменных окружения.
- Зафиксировать последовательность создания схемы и демонстрационных данных.
- Описать запуск, остановку и сохранение данных в backend README.
- Указать соседнее расположение frontend и backend; исключить абсолютные пути участников.

## Критерии готовности

- [ ] docker compose up --build запускает окружение.
- [ ] Сайт открывается, API отвечает, backend обращается к БД.
- [ ] Каталог отображает данные PostgreSQL.
- [ ] После обычного перезапуска данные сохраняются.
- [ ] Миграции и заполнение воспроизводятся по README.
- [ ] Клим повторил запуск; оба связанных PR приняты.

## Входные файлы

- [Организация совместного запуска](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/architecture/repositories.md).
- [README backend](https://github.com/CODEXSQUAD/jobmatch-backend/blob/main/README.md).
- [README frontend](https://github.com/CODEXSQUAD/jobmatch-frontend/blob/main/README.md).

## Зависимости от задач

- [Задача №6: Создать backend-каркас и endpoint /health](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/planning/week-1/06-backend-skeleton.md).
- [Задача №7: Создать frontend-каркас и подключить проверку backend](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/planning/week-1/07-frontend-skeleton.md).
- [Задача №8: Подключить PostgreSQL и создать начальную миграцию](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/planning/week-1/08-database.md).
- [Задача №9: Добавить тестовые данные и API списка вакансий](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/planning/week-1/09-vacancies-api.md).
- [Задача №10: Реализовать каталог с данными backend](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/planning/week-1/10-vacancies-ui.md).

Dockerfiles и Compose готовить параллельно с каркасами. API, данные и каталог нужны для финальной приёмки.

## Файлы результата

- [Совместный запуск](https://github.com/CODEXSQUAD/jobmatch-backend/blob/main/README.md) — существующий файл, обновляется в этой задаче.
- [Compose](https://github.com/CODEXSQUAD/jobmatch-backend/blob/main/compose.yaml) — планируемый файл, создаётся при выполнении задачи.
- [Dockerfile backend](https://github.com/CODEXSQUAD/jobmatch-backend/blob/main/Dockerfile) — планируемый файл, создаётся при выполнении задачи.
- [Dockerfile frontend](https://github.com/CODEXSQUAD/jobmatch-frontend/blob/main/Dockerfile) — планируемый файл, создаётся при выполнении задачи.
- [Nginx](https://github.com/CODEXSQUAD/jobmatch-frontend/blob/main/deploy/nginx.conf) — планируемый файл, создаётся при выполнении задачи.
- [Переменные окружения](https://github.com/CODEXSQUAD/jobmatch-backend/blob/main/.env.example) — планируемый файл, создаётся при выполнении задачи.
