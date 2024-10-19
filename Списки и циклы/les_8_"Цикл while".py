# answer = None
#
# while answer != 'да':
#     answer = input("Пойдешь тусить? ")
#
# print("Я знал, что ты согласишься!")

# ------------------------------------
# num = 4
# is_solved = False
#
# while not is_solved:
#     ans = input("Угадай число ")
#     if int(ans) == num:
#         print("Угадал")
#         is_solved = True
#     else:
#         print("Не верно")

#---------------------------------------
# num = 5
#
# while True:
#     ans = input("Угадай число ")
#     if int(ans) == num:
#         print("Угадал")
#         break
#     else:
#         print("не верно")

# ----------------------------------------
# Мы должны некоторую сумму. Выводится месяц и остаток долга, предлагается ввести сколько в этом месяце погасим
# Продолжаем, пока долг не исчезнет

debt = 10000

while debt > 0:
    print(f"Ваш долг - {debt}")
    payment = int(input("Введите сумму для погашения:"))
    debt -= payment

print("Ваш долг погашен")