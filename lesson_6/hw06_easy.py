# Задача-1:
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:
def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.
    """
    return (a * b) ** 0.5


a = float(input("a = "))
b = float(input("b = "))
c = avg(a, b)
print("Среднее геометрическое = {:.2f}".format(c))

# ПРИМЕЧАНИЕ: Для решения задач 2-4 необходимо познакомиться с модулями os, sys!
# СМ.: https://pythonworld.ru/moduli/modul-os.html, https://pythonworld.ru/moduli/modul-sys.html

# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
print('Ваща текущая директория {}'.format(os.getcwd()))
def makedir(i):
    os.mkdir('{}'.format(i))
def removedir(i):
    os.rmdir('{}'.format(i))
def chdir(i):
    os.chdir(i)
for r in range(9):
    makedir('dir_{}'.format(r+1))
print(os.listdir())
for r in range(9):
    removedir('dir_{}'.format(r+1))

# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.
import os
def nowdir():
    print('Содержимое текущей папки: {}'.format(os.listdir()))
    
# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import shutil
shutil.copy('hw05_easy.py','hw05_easy_copy.py')