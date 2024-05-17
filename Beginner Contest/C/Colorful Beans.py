N = int(input())
A = {}

for _ in range(N):
    a, b = map(int, input().split())
    if b in A:
        A[b] = min(a, A[b])
    else:
        A[b] = a
    

print(max(A.values()))
    