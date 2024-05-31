A, B, C, X = [], [], [], []
N = input()
A = list(map(int, input().split()))
M = input()
B = list(map(int, input().split()))
L = input()
C = list(map(int, input().split()))
Q = input()
X = list(map(int, input().split()))

s = set()

for a in A:
    for b in B:
        for c in C:
            s.add(a + b + c)

for x in X:
    print("Yes" if x in s else "No")

