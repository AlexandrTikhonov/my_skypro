# a = []
# for i in range(1, 10):
#     a.append(i)
#
# print(a)

# ------------------------
# РАВНОСИЛЬНО НАПИСАНОМУ ВЫШЕ !!!
# a = [item for item in range(1, 10)]
#
# print(a)

# ---------------------------
# items = [1, 2, 3]
# items_plus = []
#
# for item in items:
#     items_plus.append(item + 1)
#
# print(items_plus)
#
# # -----------------------------
# # РАВНОСИЛЬНО НАПИСАНОМУ ВЫШЕ !!!
# items = [1, 2, 3]
#
# items_plus = [item + 1 for item in items]
#
# print(items_plus)

# ----------------------------------
# items = [1, 2, 3]
# items_exp = []
#
# for item in items:
#     items_exp.append(item ** 2)
#
# print(items_exp)

# -----------------------------------
# РАВНОСИЛЬНО НАПИСАНОМУ ВЫШЕ !!!
# items = [1, 2, 3]
#
# items_exp = [item ** 2 for item in items]
#
# print(items_exp)

# ------------------------------------
# """                                                               ПРЕОБРАЗОВАНИЕ ТИПОВ"""
# items = ['1', '2', '3']
# items_int = []
#
# for item in items:
#     items_int.append(int(item))
#
# print(items_int)

# ---------------------------------------
# # РАВНОСИЛЬНО НАПИСАНОМУ ВЫШЕ !!!
# items = ['1', '2', '3']
#
# items_int = [int(item) for item in items]
#
# print(items_int)

# -----------------------------------------
# """                                                                  ФИЛЬТРАЦИЯ СПИСКОВ"""
# numbers = [-2, -1, 0, 1, 2]
# numbers_positive = []
#
# for num in numbers:
#     if num > 0:
#         numbers_positive.append(num)
#
# print(numbers_positive)

# -------------------------------------------
# # РАВНОСИЛЬНО НАПИСАНОМУ ВЫШЕ !!!
# numbers = [-2, -1, 0, 1, 2]
#
# numbers_positive = [num for num in numbers if num > 0 ]
#
# print(numbers_positive)

# -------------------------------------------
# """                                                                               ВЫЗОВ ФУНКЦИЙ"""
# numbers = [-1, -2, -3]
#
# numbers_abs = [abs(num) for num in numbers]
#
# print(numbers_abs)