N, Q = map(int, input().split())
a = list(map(int, input().split()))
T = [True] * N


for i in range(Q):
    T[a[i] - 1] = not T[a[i] - 1]

count = 0
for i in range(N):
    if T[i]:
        count += 1

print(count)