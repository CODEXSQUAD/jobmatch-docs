# Архитектура JobMatch

**Версия:** 1.0 от 22 октября 2026 года.
**Статус:** фактическая архитектура демонстрационного MVP в ветке `main`.

## Общая схема

```mermaid
flowchart TB
    user[Соискатель или работодатель]

    subgraph browser[Браузер]
        react[React + TypeScript<br/>страницы и API-клиент]
    end

    subgraph compose[Docker Compose: JobMatch]
        subgraph frontend[Frontend-контейнер]
            nginx[Nginx<br/>единая точка входа :8080]
            static[Production-сборка frontend<br/>HTML, CSS и JavaScript]
            static --> nginx
        end

        subgraph backend[Backend-контейнер]
            api[ASP.NET Core Minimal API<br/>HTTP endpoints и бизнес-правила]
            auth[ASP.NET Core Identity<br/>cookie-сессия, роли и права]
            persistence[EF Core + Npgsql<br/>доступ к данным и транзакции]
            api --> auth
            api --> persistence
            auth --> persistence
        end

        subgraph database[Контейнер данных]
            postgres[(PostgreSQL 17<br/>пользователи, резюме, вакансии,<br/>отклики и лимиты)]
        end

        nginx -->|reverse proxy<br/>внутренняя сеть Docker| api
        persistence -->|SQL| postgres
    end

    user -->|работает с интерфейсом| react
    nginx -->|отдаёт frontend<br/>http://localhost:8080| react
    react -->|HTTP /api и /health| nginx
    postgresVolume[(postgres_data)] --> postgres
    keysVolume[(data_protection_keys)] --> auth
```

На компьютере пользователя опубликован только порт frontend-контейнера `127.0.0.1:8080`. Браузер получает React-приложение от Nginx и отправляет запросы на тот же адрес. Nginx перенаправляет `/api/*` и `/health` к backend во внутренней сети Docker. Backend напрямую из браузера не публикуется, а PostgreSQL доступен только backend.

## Ответственность компонентов

| Компонент | Ответственность |
|---|---|
| React + TypeScript | Страницы гостя, соискателя и работодателя; формы; навигация; состояния загрузки и ошибок; вызовы API. |
| Nginx | Раздача production-сборки frontend, поддержка маршрутов SPA и проксирование запросов в backend. |
| ASP.NET Core API | Авторизация, проверка ролей и владения ресурсами, сценарии резюме, компании, вакансий и откликов, лимиты и переходы статусов. |
| ASP.NET Core Identity | Пользователи, проверка паролей и cookie-сессии. Пользователь выбирает одну роль: `Candidate` или `Employer`. |
| EF Core + Npgsql | Отображение доменных сущностей в PostgreSQL, миграции, ограничения и атомарные операции со списанием отклика. |
| PostgreSQL | Постоянное хранение данных MVP. Схема подробнее показана в [ERD](erd.md). |
| Docker Compose | Сборка и согласованный запуск трёх контейнеров, зависимости запуска и проверки готовности. |

## Прохождение основного сценария

```mermaid
sequenceDiagram
    actor Employer as Работодатель
    actor Candidate as Соискатель
    participant UI as React / Nginx
    participant API as ASP.NET Core API
    participant DB as PostgreSQL

    Employer->>UI: Создаёт и публикует вакансию
    UI->>API: POST /api/employer/vacancies
    API->>DB: Сохраняет черновик и публикацию

    Candidate->>UI: Заполняет резюме и выбирает вакансию
    UI->>API: PUT /api/resume/me
    API->>DB: Сохраняет резюме

    Candidate->>UI: Отправляет отклик
    UI->>API: POST /api/vacancies/{id}/applications
    API->>DB: Одна транзакция: снимок резюме,
    API->>DB: отклик, списание лимита и запись операции

    Employer->>UI: Приглашает кандидата
    UI->>API: PATCH /api/employer/applications/{id}/status
    API->>DB: Проверяет владельца вакансии и меняет статус

    Candidate->>UI: Открывает свои отклики
    UI->>API: GET /api/applications/me
    API->>DB: Читает актуальный статус
    API-->>UI: Invited
```

## Размещение исходников

- `jobmatch-frontend` — React-приложение, Nginx и frontend-тесты.
- `jobmatch-backend` — API, доменная модель, EF Core, миграции, seed, backend-тесты и `compose.yaml`.
- `jobmatch-docs` — требования, архитектура, ERD, OpenAPI, планирование и материалы демонстрации. Этот репозиторий не требуется для работы запущенного приложения.

Архитектура представляет собой один клиент, один модульный backend и одну базу данных. Микросервисы, отдельная очередь сообщений и внешний сервис авторизации в MVP не используются.
