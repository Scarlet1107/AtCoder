N, L, R = map(int, input().split())
Ans = []
for i in range(N):
    Ans.append(i+1)

Ans[L-1:R] = Ans[L-1:R][::-1]

print(" ".join(map(str, Ans)))
