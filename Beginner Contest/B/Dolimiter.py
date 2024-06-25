A = []

while True:
    a = int(input())
    if(a == 0):
        A.append(0)
        break
    A.append(a)

for i in range(len(A) - 1, -1, -1 ):
    print(A[i])
