#1- Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#Дополнительно: можете проверить, что это действительно число, и что это действительно входит в нужный диапазон
#*Пример:*
#- 6 -> да
#- 7 -> да
#- 1 -> нет


number = int(input("Введите число дня недели: "))

if number < 1 or number > 7:
    print('вы ввели не верное число')
elif number > 5:
    print('-> да')
else:
    print('-> нет')