# Задание-1:
# Напишите функцию, переводящую км в мили и выводящую информацию на консоль
# т.е функция ничего не возвращает, а выводит на консоль ответ самостоятельно
# Предполагается, что 1км = 1,609 мили
def convert(km):
    miles= km * 1.609
    print(miles)
convert(12)


 km = input('km = ')
def convert(km):
    miles = km * 1.609
    return miles
print(convert(int(km)))

# Задание-2:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
def my_round(number, ndigits):
    int_ndigits = int(ndigits)
    degree = pow(10,int(ndigits))
    mu =  number * degree
    res = int(mu)
    ost = mu - res
    if not (abs(ost) < 0.5):
        if res > 0: 
            res += 1
        else: 
            res -= 1
    return res / degree
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-3:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить, должна возвращать либо True,
# ибо False (если счастливый и несчастливый соответственно)

def lucky_ticket(ticket_number):
    tn_list=str(ticket_number)
    if len(tn_list) != 6:
         return False
    first = 0
    last = 0
    for i in range(3):
        first += int(tn_list[i])
        last += int(tn_list[-i - 1])
    return first == last
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
