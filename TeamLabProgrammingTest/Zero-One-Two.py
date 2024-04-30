import numpy as np

A = ""

for i in range (1, 101):
    if(i % 3 == 0):
        for j in range(i):
            A += "ZERO"
    elif(i % 3 == 1):
        for j in range(i):
            A += "ONE"
    elif(i % 3 == 2):
        for j in range(i):
            A += "TWO"
        
# print("len(A) = ", len(A))

Ans = ""

for i in range(0, 17):
    print(i)
    Ans += A[199 + i*1000]

print(Ans)

# for i in range(1000):
#     for j in range(20):
#         N[i][j] = A[k]
#         k += 1O
