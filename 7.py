x = int(input())
cnt = 0 #счётчик делителей
for i in range(1, x+1):
    if x % i == 0: #подбор делителей
        cnt += 1
print(cnt)