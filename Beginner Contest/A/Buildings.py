N = int(input())
A = list(map(int, input().split()))
ans = 0

for i in range(1, N):
    if(A[0] < A[i]):
        ans = i
        break

if(ans == 0):
    print(-1)
else:
    print(ans + 1)