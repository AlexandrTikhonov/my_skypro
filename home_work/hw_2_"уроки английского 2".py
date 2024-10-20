count = 0
res = 0

questions = ['My name ___ Vova', 'I ___ a coder', 'I live ___ Moscow']
answers = ['is', 'am', 'in']

print('Привет!\nПредлагаю проверить свои знания английского!\nНабери "ready", чтобы начать!')

starter = input()

if starter == 'ready':
    print(f"Вопрос 1\n{questions[0]}")
else:
    print("Кажется, вы не хотите играть. Очень жаль.")

ans_1 = input()
if ans_1 == answers[0]:
    print("Ответ верный, Вы заработали 10 баллов")
    count += 10
    res += 1
else:
    print(f"Неправильно. Правильный ответ {answers[0]}")

print(f"Вопрос 2\n{questions[1]}")

ans_2 = input()
if ans_2 == answers[1]:
    print("Ответ верный, Вы заработали 10 баллов")
    count += 10
    res += 1
else:
    print(f"Неправильно. Правильный ответ {answers[1]}")

print(f"Вопрос 3\n{questions[2]}")

ans_3 = input()
if ans_3 == answers[2]:
    print("Ответ верный, Вы заработали 10 баллов")
    count += 10
    res += 1
else:
    print(f"Неправильно. Правильный ответ {answers[2]}")

print(
    f"Вот и все! Вы ответили на {res} вопросов из 3 верно, это {round(res / 3 * 100)} процентов. И заработали {count} баллов")
