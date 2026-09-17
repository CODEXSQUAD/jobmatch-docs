# Реализовать каталог с данными backend

- **Репозиторий Issue:** `jobmatch-frontend`
- **Ответственный:** Влад
- **Срок:** День 5
- **Проверяет:** Игорь

## Описание

Создать первый экран, отображающий вакансии из PostgreSQL через API.

## Что сделать

- Реализовать каталог по макету.
- Показать название, компанию, город, формат работы и зарплату при её наличии.
- Подключить GET /api/vacancies и переключение страниц.
- Обработать загрузку, пустую выдачу и ошибку.
- До готовности backend использовать mock-ответы по контракту; на демонстрации подключить настоящий API.
- Проверить отображение на узком экране.
- Описать проверку каталога в README.

## Критерии готовности

- [ ] Каталог отображает данные настоящего API.
- [ ] Поля и необязательная зарплата отображаются корректно.
- [ ] Переключение страниц запрашивает нужные данные.
- [ ] Загрузка, ошибка и пустая выдача имеют отдельные состояния.
- [ ] Страница пригодна для узкого экрана.
- [ ] Сборка проходит.

## Входные файлы

- [MVP](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/requirements/mvp.md).
- [Ссылка на макеты](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/design/README.md).
- [README frontend](https://github.com/CODEXSQUAD/jobmatch-frontend/blob/main/README.md).

## Зависимости от задач

- [Задача №4: Подготовить OpenAPI-контракт основных сценариев](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/planning/week-1/04-api-contract.md).
- [Задача №5: Подготовить первичные макеты и пользовательские потоки](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/planning/week-1/05-design.md).
- [Задача №7: Создать frontend-каркас и подключить проверку backend](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/planning/week-1/07-frontend-skeleton.md).
- [Задача №9: Добавить тестовые данные и API списка вакансий](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/planning/week-1/09-vacancies-api.md).

Начать после согласования контракта и макета с mock-данными. Задача №9 нужна для окончательной проверки с API.

## Файлы результата

- [Проверка каталога](https://github.com/CODEXSQUAD/jobmatch-frontend/blob/main/README.md) — существующий файл, обновляется в этой задаче.

## Контракт для реализации

- [OpenAPI](https://github.com/CODEXSQUAD/jobmatch-docs/blob/main/api/openapi.yaml) — планируемый файл из задачи №4; использовать после согласования нужных endpoints.
