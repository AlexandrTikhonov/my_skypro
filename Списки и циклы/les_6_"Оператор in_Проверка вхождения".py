# """
# Выберите, что вернет оператор in при работе со списком
# """
# things = ["кошки", "мышки", "мошки", "тотошки"]
#
# name = "Кошки"
#
# var = name.lower() in things
#
# print(var)

#-----------------------------------------------

# Пример:
my_list = ['apple', 'banana', 'orange']
string = 'BanANA'

# Изменить все элементы списка на верхний регистр
# my_list_upper = [word.upper() for word in my_list]
# print(my_list_upper)
if string.lower() in [word.lower() for word in my_list]:
    print("Ok!")