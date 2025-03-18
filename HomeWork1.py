def determine_grade(score):
    if 0 <= score <= 49:
        return "Незадовільно"
    elif 50 <= score <= 69:
        return "Задовільно"
    elif 70 <= score <= 89:
        return "Добре"
    elif 90 <= score <= 100:
        return "Відмінно"
    else:
        return "Некоректний бал"

try:
    score = int(input("Введіть кількість балів (0-100): "))
    print("Оцінка:", determine_grade(score))
except ValueError:
    print("Будь ласка, введіть ціле число!")