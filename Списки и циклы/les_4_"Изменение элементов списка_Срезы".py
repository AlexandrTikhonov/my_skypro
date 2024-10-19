ladies = ['Маша', 'Таня', 'Оля']
tanya = ladies[1]

print(tanya)

#-----------------------------------------------
flock = ['sheep', 'sheep', 'sheep', 'sheep' ]
flock[1] = 'wolf'

print(flock)

# -----------------------------------------------
kings = ['Genrih', 'Ludovik', 'Fridrih', 'Richard']
pos = 3

print(kings[pos])

#--------------------------------------------------
drinks = ['пиво', 'чай', 'кофе', 'водка']
print(drinks[0:3])

#--------------------------------------------------
"""
Вам предоставлен список с англоязычными и русскими терминами.
Разделите их по 2 разным спискам
"""
terms = ["MVP", "Маржинальность", "Гипотеза", "Деплой", "ROI", "IDE", "Python"]

terms_en = terms[0:1] + terms[4:]
# terms_en = [terms[0]] + terms[4:]   альтернатива решения
terms_ru = terms[1:4]

print(terms)
print(terms_en)
print(terms_ru)