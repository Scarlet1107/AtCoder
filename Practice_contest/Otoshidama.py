N, M = map(int, input().split())

count = 0

for i in range(N):
    money = M
    x = money // 10000
    money = money % 10000

    y = money // 5000
    money = money % 5000

    z = money // 1000
    money = money % 1000


if x + y + z < N and money == 0:
    print(str(x) + " " + str(y) + " " + str(z))
else:
    print("-1 -1 -1")
