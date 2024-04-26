N = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)


score_alice = 0
score_bob = 0

for i in range(N):
    if i % 2 == 0:
        score_alice += a[i]
    else:
        score_bob += a[i]    

print(score_alice - score_bob)