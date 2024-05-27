N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

i = 0
j = 0
check = bool

while i < N and j < M:
    if(A[i] < B[j] and check == True):
        print("Yes")
        exit()
    elif(A[i] < B[j]):
        i += 1
        # print("i = ",i)
        check = True
    elif(A[i] > B[j]):
        j += 1
        # print("j = ",j)
        check = False
    else:
        print("何かがおかしい")
               
if(len(A) - i > 1):
    print("Yes")
else:
    print("No")