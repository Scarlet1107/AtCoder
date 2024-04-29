# スイカゲーム
N = int(input())
A = list(map(int, input().split()))
B = []

for a in A:
    B.append(a)
    while len(B) >= 2 and B[-1] == B[-2]:
        x = B.pop()
        B.pop()
        B.append(x + 1)
    
print(len(B))



