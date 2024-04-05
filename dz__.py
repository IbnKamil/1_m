# 1 work
# age = int(input('Введите ваш возраст: '))
# if age < 18:
#     print('Доступ запрещен')
# else:
#     print('Доступ разрешен')



# 2 work
# number = str(input('Введите четырехзначное число: '))
# x = number [0]
# c = number [3]
# z = number [1]
# y = number [2]
# x, c, z, y = int(x), int(c), int(z), int(y)
# if x + c == z - y:
#     print(True)
# else:
#     print(False)



# 3 work
# number = int(input("Введие целое число: "))
# if number//2 == number/2:
#     print('Число четное')
# else:
#     print("Число нечетное")




# 4 work
# password_1 = str(input("Введите пароль: "))
# password_2 = str(input("Введите повторно пароль: "))
# if password_1 == password_2:
#     print("Пароль принят")
# else:
#     print("Пароль не принят")



# 5 work
# months = {1:31, 2: 28, 3:31, 4:30 ,5:31 ,6:30 ,7:31 ,8:31 ,9:30 ,10:31 ,11:30 ,12:31}
# print(months [int(input('Введите номер месяца: '))], 'дней в данном месяце')



# 6 work
# weight = int(input('Введите вес (kg): '))
# if weight < 60:
#     print('Легкий вес')
# elif 60 <= weight < 64:
#     print('Первый полусредний вес')
# elif 64 <= weight < 69:
#     print('Полусредний вес')
# else:
#     print('Не удовлетворяет ни одной из категорий')



# 7 work
num_1, str_, num_2 = int(input()), str(input()), int(input())
if num_2 != 0:
    if str == '/':
        print(num_1 / num_2)
    elif str == '*':
        print(num_1 * num_2)
    elif str == '-':
        print(num_1 - num_2)
    elif str == '+':
        print(num_1 + num_2)
    else:
        print("Неверная операция")
else:
    print('На ноль делить нельзя')

