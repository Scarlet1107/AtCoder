N, X, Y, Z = map(int, input().split())

if(not (1 <= X <= N)  or  not(1 <= Y <= N)):
    exit()

if(X < Z < Y or Y < Z < X):
    print("Yes")
else:
    print("No")
