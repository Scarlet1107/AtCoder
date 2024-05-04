N = int(input())

s = 0
h = 0

for _ in range(N):
    a, b = map(int, input().split())
    s += a
    h = max(h, b-a)

print(s+h)