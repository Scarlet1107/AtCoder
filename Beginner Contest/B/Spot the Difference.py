# check difference between A and B strings
N = int(input())

A = []

for i in range(N):
    A.append(list(input()))


for i in range(N):
    B = list(input())
    for j in range(N):
        if A[i][j] != B[j]:
            print(i+1, j+1)
            exit()
