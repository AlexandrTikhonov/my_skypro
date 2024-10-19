numbers = [1, 2, 3]
numbers.remove(2)

print(numbers)

#---------------------------------------------
letters = ['a', 'b', 'c']
letters.remove('b')

print(letters)

#----------------------------------------------
numbers = [1, 2, 3]

del numbers[0]
print(numbers)

#------------------------------------------------
num = [1, 2, 3, 4, 5]

removed = num.pop(0)                  # pop удаляет элемент списка указанного индекса
print(removed)
print(num)

#------------------------------------------------
num = [1, 2, 3, 4, 5]

removed = num.pop()                   # pop без аргумента удаляет последний элемент списка
print(removed)
print(num)