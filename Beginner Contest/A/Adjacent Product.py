N = int(input())
A = list(map(int, input().split()))
Ans = []

for i in range(N - 1):
    Ans.append(A[i] * A[i + 1])
    
print(*Ans)