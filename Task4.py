# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество 
# журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Примеры:
# 6 -> 1 4 1
# 24 -> 4 16 4 60 -> 10 40 10

print ('Введите число журавликов: ')
S = int(input('S = '))
if S%6==0:
    print('Петя и Сережа сделали каждый по', (S//6), 'журавликов, а Катя', (4*S//6))
else:
    print('Заданое число журавликов не соответствует условию') 