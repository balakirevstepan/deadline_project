# Практическая работа 3

**Студент:** Балакирев Степан Сергеевич
**Группа:** ЗКИ24-17Б
**Предмет:** Введение в профессиональную деятельность

---

## Описание варианта

Система оценивания работ с учётом дедлайнов. Необходимо реализовать две функции:

1. `deadline_score(pass_date, deadline_date)` — определяет баллы за работу (от 5 до 0). За каждую неделю опоздания снимается 1 балл.

2. `late_list(grades, deadline_date)` — возвращает список фамилий студентов, сдавших работу после дедлайна, в алфавитном порядке.

Формат даты: `DD.MM.YYYY`

---

## Шаг 1. Инициализация git-репозитория

```bash
git init
```
Эта команда создаёт новый пустой git-репозиторий в текущей папке. После выполнения появляется скрытая папка `.git`, в которой git хранит всю историю изменений.

**Результат:**
```
Initialized empty Git repository in /Users/stepan/vpd/z3/deadline_project/.git/
```

---

## Шаг 2. Создание начального файла и первый коммит

```bash
git add deadline.py
```
Команда `git add` добавляет файл `deadline.py` в индекс (staging area). Это подготовка файла к коммиту — мы говорим git, что хотим сохранить изменения в этом файле.

```bash
git commit -m "Инициализация проекта"
```
Команда `git commit` сохраняет все проиндексированные изменения в историю репозитория. Флаг `-m` позволяет указать сообщение коммита прямо в командной строке.

**Результат:**
```
[main (root-commit) 1283a11] Инициализация проекта
 1 file changed, 3 insertions(+)
 create mode 100644 deadline.py
```
Здесь `1283a11` — это сокращённый хеш коммита (уникальный идентификатор).

---

## Шаг 3. Создание ветки для первой функции

```bash
git checkout -b feature/deadline-score
```
Команда `git checkout -b` создаёт новую ветку и сразу переключается на неё. Ветка `feature/deadline-score` будет использоваться для разработки первой функции. Это позволяет изолировать изменения от основной ветки `main`.

**Результат:**
```
Switched to a new branch 'feature/deadline-score'
```

---

## Шаг 4. Реализация функции deadline_score и коммит

После написания кода функции `deadline_score` в файле `deadline.py`:

```bash
git add deadline.py
```
Добавляем изменённый файл в индекс.

```bash
git commit -m "Добавлена функция deadline_score"
```
Сохраняем изменения в историю с описательным сообщением.

**Результат:**
```
[feature/deadline-score 77d8e40] Добавлена функция deadline_score
 1 file changed, 19 insertions(+), 1 deletion(-)
```
Коммит создан в ветке `feature/deadline-score` с хешем `77d8e40`.

---

## Шаг 5. Слияние первой ветки в main

```bash
git checkout main
```
Переключаемся обратно на основную ветку `main`. Команда `git checkout` без флага `-b` просто переключает на существующую ветку.

```bash
git merge feature/deadline-score
```
Команда `git merge` сливает изменения из указанной ветки (`feature/deadline-score`) в текущую ветку (`main`). Все коммиты из ветки `feature/deadline-score` теперь становятся частью ветки `main`.

**Результат:**
```
Switched to branch 'main'
Updating 1283a11..77d8e40
Fast-forward
 deadline.py | 20 +++++++++++++++++++-
 1 file changed, 19 insertions(+), 1 deletion(-)
```
`Fast-forward` означает, что слияние прошло без конфликтов — git просто "перемотал" указатель ветки `main` вперёд.

---

## Шаг 6. Создание ветки для второй функции

```bash
git checkout -b feature/late-list
```
Создаём вторую ветку `feature/late-list` для разработки функции `late_list`. Ветка создаётся от текущего состояния `main` (которое уже включает первую функцию).

**Результат:**
```
Switched to a new branch 'feature/late-list'
```

---

## Шаг 7. Реализация функции late_list и коммит

После написания кода функции `late_list`:

```bash
git add deadline.py
```
Добавляем изменённый файл в индекс.

```bash
git commit -m "Добавлена функция late_list"
```
Сохраняем изменения с сообщением.

**Результат:**
```
[feature/late-list d8f9fc8] Добавлена функция late_list
 1 file changed, 11 insertions(+)
```

---

## Шаг 8. Слияние второй ветки в main

```bash
git checkout main
```
Переключаемся на ветку `main`.

```bash
git merge feature/late-list
```
Сливаем изменения из `feature/late-list` в `main`.

**Результат:**
```
Switched to branch 'main'
Updating 77d8e40..d8f9fc8
Fast-forward
 deadline.py | 11 +++++++++++
 1 file changed, 11 insertions(+)
```

---

## Шаг 9. Создание ветки для интерактивного ввода

```bash
git checkout -b feature/interactive-input
```
Создаём третью ветку `feature/interactive-input` для добавления интерактивного ввода с клавиатуры.

**Результат:**
```
Switched to a new branch 'feature/interactive-input'
```

---

## Шаг 10. Реализация интерактивного ввода и коммит

После добавления блока `if __name__ == "__main__"` с вводом с клавиатуры:

```bash
git add deadline.py
```
Добавляем изменённый файл в индекс.

```bash
git commit -m "Добавлен интерактивный ввод с клавиатуры"
```
Сохраняем изменения с сообщением.

**Результат:**
```
[feature/interactive-input e2bd27f] Добавлен интерактивный ввод с клавиатуры
 1 file changed, 29 insertions(+)
```

---

## Шаг 11. Слияние третьей ветки в main

```bash
git checkout main
```
Переключаемся на ветку `main`.

```bash
git merge feature/interactive-input
```
Сливаем изменения из `feature/interactive-input` в `main`.

**Результат:**
```
Switched to branch 'main'
Updating d8f9fc8..e2bd27f
Fast-forward
 deadline.py | 29 +++++++++++++++++++++++++++++
 1 file changed, 29 insertions(+)
```

---

## Граф коммитов

```bash
git log --all --graph --oneline --decorate
```
Эта команда показывает историю коммитов в виде графа:
- `--all` — показать все ветки
- `--graph` — нарисовать граф ASCII-символами
- `--oneline` — каждый коммит в одну строку
- `--decorate` — показать названия веток

**Результат:**
```
* e2bd27f (HEAD -> main, feature/interactive-input) Добавлен интерактивный ввод с клавиатуры
* d8f9fc8 (feature/late-list) Добавлена функция late_list
* 77d8e40 (feature/deadline-score) Добавлена функция deadline_score
* 1283a11 Инициализация проекта
```

Здесь видно:
- 4 коммита в хронологическом порядке (снизу вверх)
- `HEAD -> main` — мы сейчас находимся на ветке `main`
- Ветки `feature/deadline-score`, `feature/late-list` и `feature/interactive-input` указывают на соответствующие коммиты

---

## Список веток

```bash
git branch -a
```
Команда показывает все ветки репозитория. Звёздочка `*` отмечает текущую ветку.

**Результат:**
```
  feature/deadline-score
  feature/interactive-input
  feature/late-list
* main
```

---

## Демонстрация работы функций

### Примеры из задания

**Пример 1:** Сдача раньше дедлайна (01.09 < 02.09) — максимальные 5 баллов
```bash
python3 -c "from deadline import deadline_score; print(deadline_score('01.09.2020', '02.09.2020'))"
```
```
5
```

**Пример 2:** Опоздание на 1 день — это 1 неделя, снимается 1 балл
```bash
python3 -c "from deadline import deadline_score; print(deadline_score('03.09.2020', '02.09.2020'))"
```
```
4
```

**Пример 3:** Опоздание на ~17 недель — снимается 5+ баллов, но минимум 0
```bash
python3 -c "from deadline import deadline_score; print(deadline_score('31.12.2020', '02.09.2020'))"
```
```
0
```

**Пример 4:** Иванов сдал 03.09, Петров сдал 01.09. Дедлайн 02.09. Опоздал только Иванов.
```bash
python3 -c "from deadline import late_list; print(late_list({'Иванов': '03.09.2020', 'Петров': '01.09.2020'}, '02.09.2020'))"
```
```
['Иванов']
```

### Дополнительные примеры

**Сдача точно в день дедлайна — 5 баллов (опоздания нет):**
```bash
python3 -c "from deadline import deadline_score; print(deadline_score('15.10.2024', '15.10.2024'))"
```
```
5
```

**Опоздание на 14 дней = 2 полные недели — снимается 2 балла:**
```bash
python3 -c "from deadline import deadline_score; print(deadline_score('29.10.2024', '15.10.2024'))"
```
```
3
```

**Несколько опоздавших студентов — возвращаются в алфавитном порядке:**
```bash
python3 -c "from deadline import late_list; print(late_list({'Сидоров': '20.10.2024', 'Балакирев': '14.10.2024', 'Козлов': '25.10.2024'}, '15.10.2024'))"
```
```
['Козлов', 'Сидоров']
```
Балакирев сдал 14.10 (до дедлайна 15.10), поэтому его нет в списке.

**Некорректный формат даты — выбрасывается исключение ValueError:**
```bash
python3 -c "from deadline import deadline_score; deadline_score('2024-10-15', '15.10.2024')"
```
```
ValueError: Некорректный формат даты: 2024-10-15. Ожидается DD.MM.YYYY
```

---

## Итоговый код (deadline.py)

```python
from typing import List
from datetime import datetime

def parse_date(date_str: str) -> datetime:
    try:
        return datetime.strptime(date_str, "%d.%m.%Y")
    except ValueError:
        raise ValueError(f"Некорректный формат даты: {date_str}. Ожидается DD.MM.YYYY")

def deadline_score(pass_date: str, deadline_date: str) -> int:
    submission = parse_date(pass_date)
    deadline = parse_date(deadline_date)

    if submission <= deadline:
        return 5

    days_late = (submission - deadline).days
    weeks_late = (days_late + 6) // 7

    score = 5 - weeks_late
    return max(0, score)

def late_list(grades: dict, deadline_date: str) -> List[str]:
    deadline = parse_date(deadline_date)
    late_students = []

    for student, pass_date in grades.items():
        submission = parse_date(pass_date)
        if submission > deadline:
            late_students.append(student)

    return sorted(late_students)


if __name__ == "__main__":
    print("=== Система оценивания работ ===")
    print("1 - Рассчитать баллы за работу")
    print("2 - Список опоздавших студентов")

    choice = input("Выберите режим (1 или 2): ")

    if choice == "1":
        deadline_date = input("Введите дату дедлайна (DD.MM.YYYY): ")
        pass_date = input("Введите дату сдачи (DD.MM.YYYY): ")
        score = deadline_score(pass_date, deadline_date)
        print(f"Оценка: {score} баллов")

    elif choice == "2":
        deadline_date = input("Введите дату дедлайна (DD.MM.YYYY): ")
        n = int(input("Сколько студентов? "))
        grades = {}
        for i in range(n):
            name = input(f"Фамилия студента {i+1}: ")
            date = input(f"Дата сдачи {name} (DD.MM.YYYY): ")
            grades[name] = date

        late = late_list(grades, deadline_date)
        if late:
            print(f"Опоздавшие: {late}")
        else:
            print("Все сдали вовремя!")
```

---

## Подключение к удалённому репозиторию

```bash
gh repo create deadline_project --public --source=. --push
```
Команда `gh repo create` создаёт репозиторий на GitHub и сразу пушит код. Флаги:
- `--public` — публичный репозиторий
- `--source=.` — использовать текущую папку как источник
- `--push` — сразу отправить код

**Результат:**
```
https://github.com/balakirevstepan/deadline_project
```

```bash
git push origin feature/deadline-score feature/late-list feature/interactive-input
```
Отправляем все feature-ветки на GitHub.

**Результат:**
```
 * [new branch]      feature/deadline-score -> feature/deadline-score
 * [new branch]      feature/late-list -> feature/late-list
 * [new branch]      feature/interactive-input -> feature/interactive-input
```
