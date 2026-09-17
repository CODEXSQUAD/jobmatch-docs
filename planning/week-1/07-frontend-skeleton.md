# Создать frontend-каркас и подключить проверку backend

- **Репозиторий Issue:** `jobmatch-frontend`
- **Ответственный:** Игорь
- **Срок:** День 2
- **Проверяет:** Влад

## Описание

Подготовить React-приложение и проверить обращение браузера к backend.

## Что сделать

- Создать React + TypeScript + Vite проект после утверждения стека.
- Подключить маршрутизацию, общий layout и простую навигацию.
- Добавить общий способ выполнения запросов к API.
- Настроить обращение к backend в окружении разработки.
- Временно показать результат GET /health и состояние ошибки.
- Обновить README с командами установки, запуска и сборки.

## Критерии готовности

- [ ] Приложение запускается по README.
- [ ] Производственная сборка проходит.
- [ ] Навигация работает.
- [ ] В браузере виден результат обращения к backend.
- [ ] Недоступность backend отображается понятной ошибкой.
- [ ] Влад воспроизвёл запуск.

## Входные файлы

- [Организация репозиториев](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/architecture/repositories.md).
- [README frontend](https://github.com/CODEXSQUAD/jobmatch-frontend/blob/main/README.md).

## Зависимости от задач

- [Задача №1: Утвердить границы MVP и бизнес-правила JobMatch](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/planning/week-1/01-mvp.md).
- [Задача №6: Создать backend-каркас и endpoint /health](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/planning/week-1/06-backend-skeleton.md).

Каркас можно создавать параллельно с backend. Задача №6 нужна для проверки соединения.

## Файлы результата

- [Инструкция frontend](https://github.com/CODEXSQUAD/jobmatch-frontend/blob/main/README.md) — существующий файл, обновляется в этой задаче.

## Контракт для реализации

- [OpenAPI](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/api/openapi.yaml) — планируемый файл из задачи №4; использовать после согласования нужных endpoints.
