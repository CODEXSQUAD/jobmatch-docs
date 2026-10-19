# API-контракты

Ответственный за подготовку: Альберт, с ревью Клима и согласованием с Владом и Игорем.

Рабочий контракт находится в [openapi.yaml](openapi.yaml). Статус каждого описанного запроса также указан в контракте через `x-implementation-status`. На 19 октября 2026 года все перечисленные ниже запросы реализованы в интеграционных ветках MVP и проверены на настоящем PostgreSQL через Docker Compose.

| Метод и путь | Статус | Назначение |
|---|---|---|
| `GET /health` | Реализован | Проверяет, что backend отвечает. Подключение к БД не проверяет. |
| `POST /api/auth/register`, `POST /api/auth/login`, `POST /api/auth/logout`, `GET /api/users/me` | Реализованы | Регистрация, сессия и текущий пользователь. |
| `GET /api/resume/me`, `PUT /api/resume/me` | Реализованы | Резюме соискателя. |
| `GET /api/company/me`, `PUT /api/company/me` | Реализованы | Компания работодателя. |
| `GET /api/vacancies` | Реализован | Каталог опубликованных вакансий из PostgreSQL; `q`, `city`, `workFormat`, `page`, `pageSize`. |
| `GET /api/vacancies/{vacancyId}` | Реализован | Карточка опубликованной вакансии. |
| `GET /api/employer/vacancies`, `POST /api/employer/vacancies`, `PUT /api/vacancies/{vacancyId}`, `POST /api/employer/vacancies/{vacancyId}/publish`, `POST /api/employer/vacancies/{vacancyId}/close` | Реализованы | Кабинет работодателя, черновик, публикация и закрытие вакансии. |
| `POST /api/vacancies/{vacancyId}/applications`, `GET /api/vacancies/{vacancyId}/applications`, `GET /api/applications/me`, `POST /api/applications/{applicationId}/withdraw`, `PATCH /api/employer/applications/{applicationId}/status` | Реализованы | Отправка, просмотр и обработка откликов. |
| `GET /api/credits/me` | Реализован | Остаток бесплатных откликов. |

Для `GET /api/vacancies` на этой неделе поддерживаются поиск по части названия, точный фильтр по городу, формат работы и пагинация. Фильтры по зарплате, компании, навыкам, полнотекстовый поиск и произвольная сортировка оставлены на будущее.

Пути, поля, статусы и форматы ответов нужно независимо сверить с Климом, Альбертом и frontend-разработчиками перед лабораторной 22 октября. Число бесплатных откликов и связанные бизнес-правила остаются рабочим предложением до утверждения командой, даже если текущая реализация использует значение 5.

Изменения контракта согласуются до реализации. Фактический OpenAPI backend сверяется с принятым контрактом.
