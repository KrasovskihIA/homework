# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
fruits = ['яблоко', 'груша', 'лимон', 'слива']
for index, i in enumerate(fruits):
    print('{} {:>}'.format(str(index + 1) + '.', i))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
one = ['яблоко', 'груша', 'лимон', 'слива']
two = ['яблоко', 'огурец', 'арбуз', 'слива']
set_one = set(one)
set_two = set(two )
new_one = set_one - set_two

print(list(new_one))


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
one = [12, 745, 32, 78, 13, 86, 16, 78,32]
two = []
for i in one:
    if i % 2==0:
        two.append(i/4)
    else:
        two.append(i*2)
print(two)