# JobMatch — словарь данных

**Версия:** 0.1 от 18 сентября 2026 года.

**Связанная схема:** [ERD](erd.md).

**Типы:** ориентированы на PostgreSQL и могут быть отображены в типы EF Core без изменения смысла.

Общие соглашения: идентификаторы — `uuid`; время — `timestamptz` в UTC; календарный день лимита — `date` по `Europe/Moscow`; строки обрезаются от пробелов; пустая строка не заменяет обязательное значение.

## User

Учётная запись и роль пользователя.

| Поле | Тип | Обяз. | Ограничения и смысл |
|---|---|---:|---|
| `id` | `uuid` | да | PK |
| `email` | `varchar(320)` | да | уникален без учёта регистра |
| `password_hash` | `varchar(500)` | да | хеш Identity; пароль не хранится |
| `role` | `varchar(20)` | да | `Candidate` или `Employer`; после регистрации не меняется в MVP |
| `is_active` | `boolean` | да | по умолчанию `true` |
| `created_at` | `timestamptz` | да | время создания |
| `updated_at` | `timestamptz` | да | время последнего изменения |

## CandidateProfile

Профиль соискателя, отделённый от учётной записи.

| Поле | Тип | Обяз. | Ограничения и смысл |
|---|---|---:|---|
| `id` | `uuid` | да | PK |
| `user_id` | `uuid` | да | FK → `User.id`, UNIQUE; только роль `Candidate` |
| `full_name` | `varchar(200)` | да | отображаемое ФИО |
| `phone` | `varchar(32)` | нет | контакт в нормализованном формате |
| `city` | `varchar(120)` | нет | город проживания |
| `created_at`, `updated_at` | `timestamptz` | да | аудит |

## Resume

Единственное текущее резюме соискателя.

| Поле | Тип | Обяз. | Ограничения и смысл |
|---|---|---:|---|
| `id` | `uuid` | да | PK |
| `candidate_profile_id` | `uuid` | да | FK → `CandidateProfile.id`, UNIQUE |
| `desired_position` | `varchar(200)` | да | желаемая должность |
| `summary` | `text` | да | описание кандидата |
| `contact_email` | `varchar(320)` | да | контакт, попадающий в снимок |
| `contact_phone` | `varchar(32)` | да | контакт, попадающий в снимок |
| `created_at`, `updated_at` | `timestamptz` | да | аудит |

Резюме считается заполненным для отклика, если заполнены ФИО профиля, `desired_position`, `summary`, `contact_email` и `contact_phone`.

## WorkExperience

Место работы в резюме; записей может не быть.

| Поле | Тип | Обяз. | Ограничения и смысл |
|---|---|---:|---|
| `id` | `uuid` | да | PK |
| `resume_id` | `uuid` | да | FK → `Resume.id` |
| `company_name` | `varchar(200)` | да | название работодателя |
| `position` | `varchar(200)` | да | должность |
| `started_on` | `date` | да | начало работы |
| `ended_on` | `date` | нет | `NULL` означает текущее место; не раньше начала |
| `description` | `text` | нет | обязанности и результаты |

## Education

Образование в резюме; записей может не быть.

| Поле | Тип | Обяз. | Ограничения и смысл |
|---|---|---:|---|
| `id` | `uuid` | да | PK |
| `resume_id` | `uuid` | да | FK → `Resume.id` |
| `institution` | `varchar(250)` | да | учебное заведение |
| `specialty` | `varchar(200)` | да | направление/специальность |
| `degree` | `varchar(100)` | нет | степень или уровень |
| `graduation_year` | `smallint` | нет | разумный диапазон проверяется приложением и БД |

## Skill

Нормализованный справочник навыков для резюме и вакансий.

| Поле | Тип | Обяз. | Ограничения и смысл |
|---|---|---:|---|
| `id` | `uuid` | да | PK |
| `name` | `varchar(100)` | да | уникален без учёта регистра |

## ResumeSkill

Связь многие-ко-многим между резюме и навыком.

| Поле | Тип | Обяз. | Ограничения и смысл |
|---|---|---:|---|
| `resume_id` | `uuid` | да | PK, FK → `Resume.id` |
| `skill_id` | `uuid` | да | PK, FK → `Skill.id` |

Составной PK запрещает повтор одного навыка в резюме.

## Company

Карточка работодателя.

| Поле | Тип | Обяз. | Ограничения и смысл |
|---|---|---:|---|
| `id` | `uuid` | да | PK |
| `name` | `varchar(200)` | да | название компании |
| `description` | `text` | да | публичное описание |
| `city` | `varchar(120)` | да | основной город |
| `created_at`, `updated_at` | `timestamptz` | да | аудит |

## CompanyMember

Принадлежность работодателя компании и основание проверки доступа.

| Поле | Тип | Обяз. | Ограничения и смысл |
|---|---|---:|---|
| `id` | `uuid` | да | PK |
| `company_id` | `uuid` | да | FK → `Company.id`, UNIQUE в MVP |
| `user_id` | `uuid` | да | FK → `User.id`, UNIQUE; роль `Employer` |
| `member_role` | `varchar(20)` | да | в MVP только `Owner` |
| `created_at` | `timestamptz` | да | дата вступления |

## Vacancy

Черновик, опубликованная или закрытая вакансия.

| Поле | Тип | Обяз. | Ограничения и смысл |
|---|---|---:|---|
| `id` | `uuid` | да | PK |
| `company_id` | `uuid` | да | FK → `Company.id` |
| `title` | `varchar(200)` | да | название должности |
| `description` | `text` | да | условия и задачи |
| `requirements` | `text` | да | требования к кандидату |
| `city` | `varchar(120)` | да | город вакансии |
| `work_format` | `varchar(20)` | да | `Office`, `Remote` или `Hybrid` |
| `salary_from` | `integer` | нет | рублей в месяц, неотрицательно |
| `salary_to` | `integer` | нет | не меньше `salary_from` |
| `status` | `varchar(20)` | да | `Draft`, `Published`, `Closed` |
| `published_at` | `timestamptz` | нет | обязательно после публикации |
| `closed_at` | `timestamptz` | нет | обязательно после закрытия |
| `created_at`, `updated_at` | `timestamptz` | да | аудит |

Индексы каталога: `(status, published_at DESC)`, `city`, `work_format`; способ поиска по названию согласуется с backend.

## VacancySkill

Связь многие-ко-многим между вакансией и требуемым навыком.

| Поле | Тип | Обяз. | Ограничения и смысл |
|---|---|---:|---|
| `vacancy_id` | `uuid` | да | PK, FK → `Vacancy.id` |
| `skill_id` | `uuid` | да | PK, FK → `Skill.id` |

## Application

Отклик кандидата на вакансию и история его статуса.

| Поле | Тип | Обяз. | Ограничения и смысл |
|---|---|---:|---|
| `id` | `uuid` | да | PK |
| `candidate_profile_id` | `uuid` | да | FK → `CandidateProfile.id` |
| `resume_id` | `uuid` | да | FK → `Resume.id`; источник снимка |
| `vacancy_id` | `uuid` | да | FK → `Vacancy.id`; `NO ACTION` при удалении |
| `idempotency_key` | `varchar(100)` | да | уникален в пределах кандидата |
| `status` | `varchar(20)` | да | `Submitted`, `Viewed`, `Invited`, `Rejected`, `Withdrawn` |
| `cover_letter` | `text` | нет | сопроводительное письмо |
| `resume_snapshot` | `jsonb` | да | неизменяемые данные резюме на момент отправки |
| `snapshot_version` | `integer` | да | версия формата; начало с `1` |
| `submitted_at`, `updated_at` | `timestamptz` | да | аудит |

Уникальность `(candidate_profile_id, vacancy_id)` запрещает повторный отклик даже после отзыва. `resume_snapshot` не обновляется при изменении текущего резюме.

Минимальная структура снимка версии 1:

```json
{
  "fullName": "Иван Петров",
  "contactEmail": "candidate@example.test",
  "contactPhone": "+70000000000",
  "desiredPosition": "Разработчик",
  "summary": "Учебное резюме",
  "skills": ["C#", "PostgreSQL"],
  "workExperience": [],
  "education": []
}
```

## CreditAccount

Текущий бесплатный остаток соискателя.

| Поле | Тип | Обяз. | Ограничения и смысл |
|---|---|---:|---|
| `id` | `uuid` | да | PK |
| `candidate_profile_id` | `uuid` | да | FK → `CandidateProfile.id`, UNIQUE |
| `period_date` | `date` | да | текущий московский календарный день |
| `balance` | `integer` | да | `0 <= balance <= daily_limit` |
| `daily_limit` | `integer` | да | положительная настройка; рабочее значение 5 |
| `version` | `integer` | да | токен конкурентного обновления |
| `updated_at` | `timestamptz` | да | аудит |

При первом обращении в новый московский день счёт обновляется до `daily_limit` в той же транзакции, которая читает или списывает остаток. Неиспользованный остаток не переносится.

## CreditTransaction

Неизменяемый журнал операций лимита.

| Поле | Тип | Обяз. | Ограничения и смысл |
|---|---|---:|---|
| `id` | `uuid` | да | PK |
| `credit_account_id` | `uuid` | да | FK → `CreditAccount.id` |
| `application_id` | `uuid` | нет | FK → `Application.id`; задан для списания за отклик |
| `type` | `varchar(20)` | да | `DailyReset` или `Debit` |
| `amount` | `integer` | да | положительное число; направление задаёт `type` |
| `reason` | `varchar(100)` | да | машинно-читаемая причина |
| `created_at` | `timestamptz` | да | время операции |

Для `Debit` используется уникальный частичный индекс по `application_id`, чтобы один отклик не списывал лимит дважды. Журнал не редактируется и не удаляется обычными пользовательскими операциями.

## Справочные значения и переходы

- `User.role`: `Candidate`, `Employer`.
- `Vacancy.status`: `Draft → Published → Closed`.
- `Application.status`: `Submitted → Viewed → Invited`; из `Submitted`/`Viewed` допустим `Rejected`; из `Invited` допустим `Rejected`; из `Submitted`/`Viewed`/`Invited` допустим `Withdrawn`.
- `Rejected` и `Withdrawn` — конечные состояния.

Проверки переходов выполняются в доменной логике backend. Ограничение БД гарантирует только принадлежность значения разрешённому набору.
