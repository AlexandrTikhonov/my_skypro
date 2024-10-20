letters = ['A', 'B', 'C', 'D', 'E', 'F']

# for i in range(len(letters)):
#     letter = letters[i]
#     print(i, letter)

# for i, letter in enumerate(letters): # РАВНОЗНАЧЕН ЦИКЛУ ПОКАЗАННОМУ ВЫШЕ
#     print(i, letter)

# for i, letter in enumerate(letters, start=1):
#     print(i, letter)

# -------------------------------------
# # Вывести позиции элементов, равных True:
# items = [True, True, False, True, True, False, True]
#
# for index, value in enumerate(items, start=1):
#     if value:
#         print(index)

# --------------------------------------
# Вывести только четные элементы
letters = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot']
let_ = []
for i, letter in enumerate(letters, start=1):
    if i % 2 == 0:
       print(i, letter)

# ---------------------------------------
