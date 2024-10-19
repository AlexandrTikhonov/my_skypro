# items_list = ['p', 'y', 't', 'h', 'o', 'n']
#
# for item in items_list:
#     print(item)

#--------------------------------------------
# ex_gfs = ["Иветта", "Лизетта", "Мюзетта", "Жанетта", "Жоржетта"]
#
# for ex in ex_gfs:
#     print(ex)
#
# print("Покуда я с вами - клянусь, моя песня не спета")

#--------------------------------------------------------------------
# reasons = ["ты", "все твои мечты", "боль"]
# num = 1
#
# for reason in reasons:
#     print(f"{num} причина - это {reason}")
#     num += 1

#--------------------------------------------------------------------
# words = ["воронка", "лавировали", "тележка", "маленький"]
#
# for word in words:
#     if "р" in word:
#         print(f"{word} - картавое слово")

#----------------------------------------------------------------------
# """
# Дан список трат, суммировать их и вывести общие расходы
# """
#
# expenses = [200, 450, 320, 1100, 650, 280, 325, 490, 830, 420]
# total = 0
#
# for payment in expenses:
#     total += payment
#
# print(f"Всего потрачено: {total}")

# -----------------------------------------------------------------------
medals = ["gold", "gold", "silver", "gold", "bronze", "silver", "gold", "gold", "silver", "chocolate"]

gold_count = 0
silver_count = 0
bronze_count = 0
chocolate_count = 0

for medal in medals:
    if medal == "gold":
        gold_count += 1
    elif medal == "silver":
        silver_count += 1
    elif medal == "bronze":
        bronze_count += 1
    elif medal == "chocolate":
        chocolate_count += 1

print(f"Золотых медалей {gold_count}")
print(f"Серебрянных медалей {silver_count}")
print(f"Бронзовых медалей {bronze_count}")
print(f"Шоколадных медалей {chocolate_count}")

