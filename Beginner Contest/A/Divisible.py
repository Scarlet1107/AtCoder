N, K = map(int, input().split())

A = list(map(int, input().split()))
Ans = []

for i in range(N):
    if(A[i] % K == 0):
        Ans.append(A[i] // K)

print(*Ans)