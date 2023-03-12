n = int(input())
cnt = 1 #счётчик для факториала
num = 1
for i in range(n):
    cnt = cnt*n
    num += 1/cnt #цикл 1+...+1/N!
print(num)