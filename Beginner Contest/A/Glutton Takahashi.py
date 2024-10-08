N = int(input())

isfull = False

S = []

for i in range(N):
    S.append(str(input()))

for i in range(N):
    if S[i] == "sweet" and (isfull == True) and (i != N - 1):
        print("No")
        exit()
    elif S[i] == "sweet":
        isfull = True
    else:
        isfull = False

print("Yes")
