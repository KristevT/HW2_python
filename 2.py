n = int(input()) #кол-во чисел
cnt = 0 #счётчик
for i in range(n):
    if (num := int(input())) == 0: #если введённое число = 0, счётчик увеличивается
        cnt += 1
if cnt != 0:
    print('YES')
else:
    print('NO')