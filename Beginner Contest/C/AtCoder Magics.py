N = int(input())

A = [] #カードの強さ
C = [] #カードのコスト

for _ in range(N):
    a, c = map(int, input().split())
    A.append(a)
    C.append(c)