N = int(input())
moneys = list(map(int, input().split()))
for i in range(N-1):
    s, t = map(int, input().split())
    # while moneys[i] >= s:
    #     moneys[i+1] += t
    #     moneys[i] -= s
    moneys[i+1] += moneys[i]//s*t

print(moneys[N-1])