N = int(input())

S = []
C = []
total = 0

for _ in range(N):
    s, c = input().split()
    S.append(str(s))
    C.append(int(c))
    total += int(c)  

sorted_pairs = sorted(zip(S, C))

S_sorted, C_sorted = zip(*sorted_pairs)

winner = total % N
print(S_sorted[winner])
