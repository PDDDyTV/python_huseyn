def grade(score):
    if (score > 100 and score < 0):
        return "value error"
    if (score >= 90 and score <= 100):
        return "Отлично"
    if (score >= 70 and score <= 89):
        return "Хорошо"
    if (score >= 50 and score < 69):
        return "Удовлетворительно"
    if (score >= 0 and score <= 49):
        return "Неудовлетворительно"

n = int(input("введите число"))
print(grade(n))

