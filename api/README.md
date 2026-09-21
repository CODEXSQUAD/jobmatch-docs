# API-контракты

Ответственный за подготовку: Альберт, с ревью Клима и согласованием с Владом и Игорем.

Рабочий контракт находится в [openapi.yaml](openapi.yaml). Статус каждого описанного запроса также указан в контракте через `x-implementation-status`. Все пути, кроме `/health`, пока являются предложением для согласования, а не работающим API.

| Метод и путь | Статус | Назначение |
|---|---|---|
| `GET /health` | Реализован | Проверяет, что backend отвечает. Подключение к БД не проверяет. |
| `POST /api/auth/register`, `POST /api/auth/login`, `POST /api/auth/logout`, `GET /api/users/me` | Запланированы | Регистрация, сессия и текущий пользователь. |
| `GET /api/resume/me`, `PUT /api/resume/me` | Запланированы | Резюме соискателя. |
| `GET /api/company/me`, `PUT /api/company/me` | Запланированы | Компания работодателя. |
| `GET /api/vacancies`, `GET /api/vacancies/{vacancyId}` | Запланированы | Каталог и карточка опубликованной вакансии. |
| `POST /api/employer/vacancies`, `PUT /api/vacancies/{vacancyId}`, `POST /api/employer/vacancies/{vacancyId}/publish`, `POST /api/employer/vacancies/{vacancyId}/close` | Запланированы | Черновик, публикация и закрытие вакансии. |
| `POST /api/vacancies/{vacancyId}/applications`, `GET /api/vacancies/{vacancyId}/applications`, `GET /api/applications/me`, `POST /api/applications/{applicationId}/withdraw`, `PATCH /api/employer/applications/{applicationId}/status` | Запланированы | Отправка, просмотр и обработка откликов. |
| `GET /api/credits/me` | Запланирован | Остаток бесплатных откликов. |

Пути, поля, статусы и форматы ответов запланированных запросов из [задачи №4](../planning/week-1/04-api-contract.md) предстоит проверить с Климом, Альбертом и frontend-разработчиками. До такой проверки контракт остаётся черновиком.

Изменения контракта согласуются до реализации. Фактический OpenAPI backend сверяется с принятым контрактом.
