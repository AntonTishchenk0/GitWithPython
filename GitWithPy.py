# Task 1:  

# Имеется 100 рублей. Сколько быков, коров и телят можно купить на все эти деньги, 
# если плата за быка – 10 рублей, за корову – 5 рублей, за теленка – 0.5 рубля 
# и надо купить 100 голов скота?

# 10b + 5k + 0.5t = 100

# for b in range(1, 11):
#     for k in range(1, 21):
#         for t in range(1, 201):
#             if 10 * b + 5 * k + 0.5 * t == 100:
#                 if b + k + t == 100:
#                     print('b =', b, 'k =', k, 't =', t)

# Task 2:

# На вход программе подается два натуральных числа a и b (a < b). 
# Напишите программу, которая находит все простые числа от a до b включительно.

# a = int(input('Input a first number: '))
# b = int(input('Input a second number: '))
# for i in range(a, b + 1):
#     if i == 1:
#         continue 
#     for j in range(2, i):
#         if i % j == 0:
#             break 
#     else:
#         print(i)