cnt = 0 #счётчик
sum = 0
while (n := int(input())) != 0:
    cnt += 1 #счётчик запоминает кол-во введённых чисел
    sum += n #все введённые числа складываются
print(sum/cnt)