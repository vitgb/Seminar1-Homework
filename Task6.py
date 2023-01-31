# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, 
# которая проверяет счастливость билета

# Примеры:
# 385916 -> yes
# 123456 -> no

print ('Введите 6-ти значный номер билета: ')
n = int(input('n = '))

a = n%1000
b = n//1000

if (a//100 + a%10 + (a//10)%10)==(b//100 + b%10 + (b//10)%10):
    print('YES')
else:
    print('NO')