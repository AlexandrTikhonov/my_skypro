# for num in range(1, 10):
#     for i in range(1, 10):
#         print(f"{num} * {i} = {num * i}")

# ----------------------------------------
# actions = ['buy it', 'use it', 'break it', 'fix it']
#
# action_indexes = range(len(actions))
#
# for act_idx in action_indexes:
#     print(act_idx + 1, actions[act_idx])

# -----------------------------------------
price = int(input("Введите полную сумму покупки "))

for month in range(1, 13):
    month_payment = int(price / month)
    print(f"{month} месяцев - {month_payment} руб")
