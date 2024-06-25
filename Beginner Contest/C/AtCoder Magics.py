N = int(input())
p = []
for i in range(N):
    p.append(list(map(int, input().split())) + [i+1])

p.sort()

ans = []
min_cost = 10**18
for a,c,i in p[::-1]:
    if c < min_cost:
        min_cost = c
        ans.append(i)

print(len(ans))
print(*sorted(ans))