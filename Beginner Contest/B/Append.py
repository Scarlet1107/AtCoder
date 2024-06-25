Q = int(input())
ans = []
for _ in range(Q):
    query, x = map(int, input().split())
    if query == 1:
        ans.append(x)
    else:
        print(ans[len(ans)-x])