# API-контракты

Ответственный за подготовку: Альберт, с ревью Клима и согласованием с Владом и Игорем.

Рабочий контракт находится в [openapi.yaml](openapi.yaml). Статус каждого описанного запроса также указан в контракте через `x-implementation-status`. Реализованы `/health` и список опубликованных вакансий; остальные пути пока являются предложением для согласования, а не работающим API.

| Метод и путь | Статус | Назначение |
|---|---|---|
| `GET /health` | Реализован | Проверяет, что backend отвечает. Подключение к БД не проверяет. |
| `POST /api/auth/register`, `POST /api/auth/login`, `POST /api/auth/logout`, `GET /api/users/me` | Запланированы | Регистрация, сессия и текущий пользователь. |
| `GET /api/resume/me`, `PUT /api/resume/me` | Запланированы | Резюме соискателя. |
| `GET /api/company/me`, `PUT /api/company/me` | Запланированы | Компания работодателя. |
| `GET /api/vacancies` | Реализован | Каталог опубликованных вакансий из PostgreSQL; `q`, `city`, `workFormat`, `page`, `pageSize`. |
| `GET /api/vacancies/{vacancyId}` | Запланирован | Карточка опубликованной вакансии. |
| `POST /api/employer/vacancies`, `PUT /api/vacancies/{vacancyId}`, `POST /api/employer/vacancies/{vacancyId}/publish`, `POST /api/employer/vacancies/{vacancyId}/close` | Запланированы | Черновик, публикация и закрытие вакансии. |
| `POST /api/vacancies/{vacancyId}/applications`, `GET /api/vacancies/{vacancyId}/applications`, `GET /api/applications/me`, `POST /api/applications/{applicationId}/withdraw`, `PATCH /api/employer/applications/{applicationId}/status` | Запланированы | Отправка, просмотр и обработка откликов. |
| `GET /api/credits/me` | Запланирован | Остаток бесплатных откликов. |

Для `GET /api/vacancies` на этой неделе поддерживаются поиск по части названия, точный фильтр по городу, формат работы и пагинация. Фильтры по зарплате, компании, навыкам, полнотекстовый поиск и произвольная сортировка оставлены на будущее.

Пути, поля, статусы и форматы ответов остальных запланированных запросов из [задачи №4](../planning/week-1/04-api-contract.md) предстоит проверить с Климом, Альбертом и frontend-разработчиками. До такой проверки контракт остаётся черновиком.

Изменения контракта согласуются до реализации. Фактический OpenAPI backend сверяется с принятым контрактом.
