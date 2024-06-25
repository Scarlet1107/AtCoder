N = int(input())
P = list(map(int, input().split()))
Q = int(input())

for i in range(Q):
        a, b = input().split()
        if(P.index(int(a)) < P.index(int(b))):
            print(a)
        else:
            print(b)