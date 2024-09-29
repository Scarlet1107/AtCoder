N, A = map(int, input().split())
T = list(map(int, input().split()))

totalTime = 0
for i in range(N):
    if(totalTime < T[i]):
        totalTime += (T[i]-totalTime + A)
    else:
        totalTime += A
    print(totalTime)
