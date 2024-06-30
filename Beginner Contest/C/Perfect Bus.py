N = int(input())
A = list(map(int, input().split()))

n = 0

for a in A:
    n += a
    if(n < 0):
        n = 0

print(n)
