# создадим счетчик
count = 0

res = 0

# правильный ответ на вопрос 1
answer_1 = 'is'

# правильный ответ на вопрос 2
answer_2 = 'am'

# правильный ответ на вопрос 3
answer_3 = 'in'

print('Привет! Предлагаю проверить свои знания английского!\nНапиши, как тебя зовут: ')

name = input()

print(f"Привет, {name}, начинаем тренировку")

print("Вопрос 1:\nMy name ___ Vova.")

ans_1 = input()
if ans_1 == answer_1:
    print("Ответ верный!\nВы получаете 10 баллов")
    count += 10
    res += 1
else:
    print(f"Ответ неверный\nПравильный ответ: {answer_1}")

print("Вопрос 2:\nI ___ a coder.")

ans_2 = input()
if ans_2 == answer_2:
    print("Ответ верный!\nВы получаете 10 баллов")
    count += 10
    res += 1
else:
    print(f"Ответ неверный\nПравильный ответ: {answer_2}")

print("Вопрос 3:\nI live ___ Moscow.")
ans_3 = input()
if ans_3 == answer_3:
    print("Ответ верный!\nВы получаете 10 баллов")
    count += 10
    res += 1
else:
    print(f"Ответ неверный\nПравильный ответ: {answer_3}")

print(
    f"Вот и все, {name}\nВы ответили на вопросов {res} из 3 верно.\nВы заработали {count} баллов.\nЭто {round(res / 3 * 100)} процентов")
