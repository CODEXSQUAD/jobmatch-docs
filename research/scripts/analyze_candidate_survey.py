#!/usr/bin/env python3
"""Aggregate the JobMatch candidate survey without publishing raw free text."""

from __future__ import annotations

import argparse
import csv
import html
import json
import statistics
from collections import Counter
from pathlib import Path


TARGET_SEARCH_ANSWERS = {
    "Да, активно ищу сейчас.",
    "Да, искал(а) в течение последних 12 месяцев.",
}

S5_OPTIONS = [
    "требования выглядят завышенными",
    "надеюсь, что работодатель всё равно рассмотрит резюме",
    "отправляю много откликов, чтобы увеличить шанс ответа",
    "не до конца понимаю обязанности или требования",
    "отклик отправляется быстро, поэтому проще попробовать",
    "подходят зарплата, компания или формат работы, несмотря на часть требований",
]

S9_OPTIONS = [
    "понятные статусы каждого отклика",
    "обязательная или более частая обратная связь работодателя",
    "более точный поиск и фильтры",
    "проверка качества и актуальности вакансий",
    "объяснение, насколько резюме соответствует вакансии",
    "возможность получить дополнительные бесплатные отклики без оплаты",
    "ничего — ограничение для меня неприемлемо",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def column(headers: list[str], prefix: str) -> str:
    matches = [header for header in headers if header.startswith(prefix)]
    if len(matches) != 1:
        raise ValueError(f"Expected one column starting with {prefix!r}, found {len(matches)}")
    return matches[0]


def distribution(rows: list[dict[str, str]], key: str) -> Counter[str]:
    return Counter(row[key].strip() for row in rows)


def multiselect_distribution(
    rows: list[dict[str, str]], key: str, known_options: list[str]
) -> tuple[Counter[str], int, int]:
    counts: Counter[str] = Counter()
    responses_with_other = 0
    nonempty_responses = 0
    known = set(known_options)
    for row in rows:
        raw = row[key].strip()
        if not raw:
            continue
        nonempty_responses += 1
        values = [value.strip() for value in raw.split(";") if value.strip()]
        has_other = False
        for value in values:
            if value in known:
                counts[value] += 1
            else:
                has_other = True
        if has_other:
            responses_with_other += 1
    return counts, responses_with_other, nonempty_responses


def percentage(count: int, denominator: int) -> float | None:
    if denominator == 0:
        return None
    return round(100 * count / denominator, 1)


def positive_value_selected(raw: str) -> bool:
    values = {value.strip() for value in raw.split(";") if value.strip()}
    return bool(values.intersection(S9_OPTIONS[:-1]))


def sanitize_multiselect(raw: str, known_options: list[str]) -> str:
    values = [value.strip() for value in raw.split(";") if value.strip()]
    known = set(known_options)
    sanitized = [value for value in values if value in known]
    if any(value not in known for value in values):
        sanitized.append("другой ответ (текст удалён)")
    return ";".join(sanitized)


def save_horizontal_chart(
    path: Path,
    title: str,
    subtitle: str,
    labels: list[str],
    values: list[int],
    colors: list[str] | None = None,
) -> None:
    width = 1100
    left = 470
    right = 80
    top = 110
    row_height = 48
    height = top + len(labels) * row_height + 55
    plot_width = width - left - right
    maximum = max(values + [1])
    colors = colors or ["#4C78A8"] * len(labels)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        f'<text x="28" y="40" font-family="Arial, DejaVu Sans, sans-serif" font-size="24" font-weight="700" fill="#1f2937">{html.escape(title)}</text>',
        f'<text x="28" y="70" font-family="Arial, DejaVu Sans, sans-serif" font-size="15" fill="#6b7280">{html.escape(subtitle)}</text>',
    ]
    for index, (label, value, color) in enumerate(zip(labels, values, colors)):
        y = top + index * row_height
        bar_width = 0 if value == 0 else max(4, plot_width * value / maximum)
        parts.extend(
            [
                f'<text x="28" y="{y + 22}" font-family="Arial, DejaVu Sans, sans-serif" font-size="15" fill="#374151">{html.escape(label)}</text>',
                f'<rect x="{left}" y="{y}" width="{plot_width}" height="28" rx="4" fill="#eef2f7"/>',
                f'<rect x="{left}" y="{y}" width="{bar_width:.1f}" height="28" rx="4" fill="{color}"/>',
                f'<text x="{left + bar_width + 10:.1f}" y="{y + 20}" font-family="Arial, DejaVu Sans, sans-serif" font-size="15" font-weight="700" fill="#1f2937">{value}</text>',
            ]
        )
    parts.append("</svg>")
    path.write_text("\n".join(parts), encoding="utf-8")


def save_charts(
    output_dir: Path,
    n: int,
    distributions: dict[str, Counter[str]],
    s9_counts: Counter[str],
) -> None:
    chart_dir = output_dir / "charts"
    chart_dir.mkdir(parents=True, exist_ok=True)
    charts = [
        (
            "candidate-application-behavior.svg",
            "Отклик при сомнении в соответствии",
            ["никогда", "редко", "иногда", "часто", "почти всегда"],
            ["Никогда", "Редко", "Иногда", "Часто", "Почти всегда"],
            distributions["s4"],
            None,
        ),
        (
            "candidate-status-clarity.svg",
            "Понимание результата отклика",
            [
                "почти всегда вижу понятный итоговый статус",
                "иногда получаю ответ или вижу статус",
                "чаще всего не понимаю, был ли отклик рассмотрен",
                "затрудняюсь ответить",
            ],
            ["Почти всегда понятен итог", "Иногда есть ответ или статус", "Чаще всего итог непонятен", "Затруднились ответить"],
            distributions["s6"],
            None,
        ),
        (
            "candidate-concept-reaction.svg",
            "Ожидаемая реакция на ограничение",
            [
                "буду внимательнее сравнивать вакансии перед откликом",
                "поведение почти не изменится",
                "буду реже искать работу через такой сервис",
                "полностью откажусь от такого сервиса",
                "затрудняюсь ответить",
            ],
            ["Будут выбирать внимательнее", "Поведение не изменится", "Будут пользоваться реже", "Полностью откажутся", "Затруднились ответить"],
            distributions["s7"],
            ["#59A14F", "#4C78A8", "#F28E2B", "#E15759", "#9CA3AF"],
        ),
        (
            "candidate-acceptable-limit.svg",
            "Приемлемый дневной лимит бесплатных откликов",
            ["1–2", "3–5", "6–10", "более 10", "ограничения быть не должно", "затрудняюсь ответить"],
            ["1–2", "3–5", "6–10", "Более 10", "Без ограничения", "Затруднились ответить"],
            distributions["s8"],
            ["#4C78A8", "#59A14F", "#4C78A8", "#4C78A8", "#E15759", "#9CA3AF"],
        ),
    ]
    for filename, title, order, labels, counts, colors in charts:
        save_horizontal_chart(
            chart_dir / filename,
            title,
            f"Целевая выборка: n={n}; значения на столбцах — число респондентов",
            labels,
            [counts[item] for item in order],
            colors,
        )

    benefit_order = [S9_OPTIONS[0], S9_OPTIONS[2], S9_OPTIONS[1], S9_OPTIONS[5], S9_OPTIONS[3], S9_OPTIONS[4], S9_OPTIONS[6]]
    save_horizontal_chart(
        chart_dir / "candidate-valued-features.svg",
        "Что делает сервис полезным несмотря на ограничение",
        f"Целевая выборка: n={n}; можно выбрать несколько вариантов",
        ["Понятные статусы", "Точный поиск и фильтры", "Более частая обратная связь", "Дополнительные бесплатные отклики", "Проверка качества вакансий", "Оценка соответствия резюме", "Ограничение неприемлемо"],
        [s9_counts[item] for item in benefit_order],
        ["#4C78A8"] * 6 + ["#E15759"],
    )

    score_counts = distributions["s10"]
    save_horizontal_chart(
        chart_dir / "candidate-trial-intent.svg",
        "Вероятность попробовать JobMatch параллельно с привычными площадками",
        f"Целевая выборка: n={n}; шкала от 0 до 10",
        [str(score) for score in range(11)],
        [score_counts[str(score)] for score in range(11)],
        ["#F28E2B"] * 11,
    )


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    with args.source.open("r", encoding="utf-8-sig", newline="") as source_file:
        reader = csv.DictReader(source_file)
        rows = list(reader)
        headers = list(reader.fieldnames or [])

    timestamp = column(headers, "Отметка времени")
    consent = column(headers, "Согласны ли вы")
    s1 = column(headers, "С1.")
    s2 = column(headers, "С2.")
    s3 = column(headers, "С3.")
    s4 = column(headers, "С4.")
    s5 = column(headers, "С5.")
    s6 = column(headers, "С6.")
    s7 = column(headers, "С7.")
    s8 = column(headers, "С8.")
    s9 = column(headers, "С9.")
    s10 = column(headers, "С10.")
    comment = column(headers, "Почему вы поставили")

    consented = [row for row in rows if row[consent].strip() == "Да."]
    declined = [row for row in rows if row[consent].strip() != "Да."]
    recent_search = [row for row in consented if row[s1].strip() in TARGET_SEARCH_ANSWERS]
    outside_target = [row for row in consented if row[s1].strip() not in TARGET_SEARCH_ANSWERS]

    required = [s1, s2, s3, s4, s6, s7, s8, s9, s10]
    incomplete = [row for row in recent_search if any(not row[key].strip() for key in required)]
    included = [row for row in recent_search if row not in incomplete]

    answer_signatures = [tuple(row[key] for key in headers if key != timestamp) for row in included]
    duplicate_groups = sum(1 for count in Counter(answer_signatures).values() if count > 1)

    n = len(included)
    s5_counts, s5_other, s5_answered = multiselect_distribution(included, s5, S5_OPTIONS)
    s9_counts, s9_other, s9_answered = multiselect_distribution(included, s9, S9_OPTIONS)

    scores = [int(row[s10]) for row in included]
    score_distribution = Counter(scores)
    distributions = {
        "s1": distribution(included, s1),
        "s2": distribution(included, s2),
        "s3": distribution(included, s3),
        "s4": distribution(included, s4),
        "s6": distribution(included, s6),
        "s7": distribution(included, s7),
        "s8": distribution(included, s8),
        "s10": Counter({str(score): score_distribution[score] for score in sorted(score_distribution)}),
    }
    positive_value = sum(positive_value_selected(row[s9]) for row in included)
    contradictory_value = sum(
        positive_value_selected(row[s9]) and S9_OPTIONS[-1] in row[s9].split(";")
        for row in included
    )
    summary = {
        "source": {
            "received": len(rows),
            "consented": len(consented),
            "declined": len(declined),
            "outside_target": len(outside_target),
            "incomplete_target": len(incomplete),
            "included": n,
            "duplicate_groups": duplicate_groups,
            "first_response": min((row[timestamp] for row in rows), default=""),
            "last_response": max((row[timestamp] for row in rows), default=""),
        },
        "distributions": distributions,
        "multi_select": {
            "s5": {
                "counts": s5_counts,
                "other_text_responses": s5_other,
                "answered": s5_answered,
            },
            "s9": {
                "counts": s9_counts,
                "other_text_responses": s9_other,
                "answered": s9_answered,
            },
        },
        "metrics": {
            "active_now": sum(row[s1].strip() == "Да, активно ищу сейчас." for row in included),
            "reads_always_or_often": sum(row[s3].strip() in {"всегда", "часто"} for row in included),
            "applies_when_unsure": sum(
                row[s4].strip() in {"иногда", "часто", "почти всегда"} for row in included
            ),
            "usually_no_status": sum(
                row[s6].strip() == "чаще всего не понимаю, был ли отклик рассмотрен"
                for row in included
            ),
            "will_choose_more_carefully": sum(
                row[s7].strip() == "буду внимательнее сравнивать вакансии перед откликом"
                for row in included
            ),
            "will_reduce_or_reject_use": sum(
                row[s7].strip()
                in {"буду реже искать работу через такой сервис", "полностью откажусь от такого сервиса"}
                for row in included
            ),
            "accepts_3_to_5": sum(row[s8].strip() == "3–5" for row in included),
            "rejects_any_limit": sum(row[s8].strip() == "ограничения быть не должно" for row in included),
            "trial_score_median": statistics.median(scores) if scores else None,
            "trial_score_mean": round(statistics.mean(scores), 2) if scores else None,
            "trial_score_7_to_10": sum(score >= 7 for score in scores),
            "trial_score_0_to_4": sum(score <= 4 for score in scores),
            "selects_any_positive_value": positive_value,
            "contradictory_value_selection": contradictory_value,
            "optional_comments": sum(bool(row[comment].strip()) for row in included),
        },
        "percentages": {},
    }
    summary["percentages"] = {
        key: percentage(value, n)
        for key, value in summary["metrics"].items()
        if isinstance(value, int) and not isinstance(value, bool) and key != "optional_comments"
    }

    json_path = args.output_dir / "candidate-survey-summary.json"
    json_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    aggregate_rows: list[dict[str, str | int | float]] = []
    for question, counts in summary["distributions"].items():
        for answer, count in counts.items():
            aggregate_rows.append(
                {
                    "question": question.upper(),
                    "answer": answer,
                    "count": count,
                    "denominator": n,
                    "percent": percentage(count, n),
                }
            )
    for question, details in summary["multi_select"].items():
        denominator = n if question == "s9" else details["answered"]
        for answer, count in details["counts"].items():
            aggregate_rows.append(
                {
                    "question": question.upper(),
                    "answer": answer,
                    "count": count,
                    "denominator": denominator,
                    "percent": percentage(count, denominator),
                }
            )
        if details["other_text_responses"]:
            aggregate_rows.append(
                {
                    "question": question.upper(),
                    "answer": "другой ответ (текст не публикуется)",
                    "count": details["other_text_responses"],
                    "denominator": denominator,
                    "percent": percentage(details["other_text_responses"], denominator),
                }
            )

    csv_path = args.output_dir / "candidate-survey-aggregates.csv"
    with csv_path.open("w", encoding="utf-8-sig", newline="") as output_file:
        writer = csv.DictWriter(
            output_file,
            fieldnames=["question", "answer", "count", "denominator", "percent"],
        )
        writer.writeheader()
        writer.writerows(aggregate_rows)

    anonymized_rows = [
        {
            "search_status": row[s1].strip(),
            "weekly_applications": row[s2].strip(),
            "reads_vacancy": row[s3].strip(),
            "applies_when_unsure": row[s4].strip(),
            "mismatch_reasons": sanitize_multiselect(row[s5], S5_OPTIONS),
            "status_clarity": row[s6].strip(),
            "concept_reaction": row[s7].strip(),
            "acceptable_daily_limit": row[s8].strip(),
            "valued_features": sanitize_multiselect(row[s9], S9_OPTIONS),
            "trial_score": row[s10].strip(),
        }
        for row in included
    ]
    anonymized_rows.sort(key=lambda row: tuple(row.values()))
    anonymized_path = args.output_dir / "candidate-survey-anonymized.csv"
    anonymized_headers = ["response_id", *anonymized_rows[0].keys()] if anonymized_rows else ["response_id"]
    with anonymized_path.open("w", encoding="utf-8-sig", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=anonymized_headers)
        writer.writeheader()
        for index, row in enumerate(anonymized_rows, start=1):
            writer.writerow({"response_id": f"R{index:02d}", **row})

    save_charts(args.output_dir, n, distributions, s9_counts)

    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
