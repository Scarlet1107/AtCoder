N, T = map(int, input().split())
A = list(map(int, input().split()))
row = [0] * N
col = [0] * N
d1, d2 = 0, 0
ans = -1

for i in range(T):
    r, c = (A[i] - 1) // N, (A[i] - 1) % N
    row[r] += 1
    col[c] += 1
    if(r == c):
        d1 += 1
    if(r + c == N - 1):
        d2 += 1
    if(row[r] == N or col[c] == N or d1 == N or d2 == N):
        ans = i + 1
        break
print(ans)