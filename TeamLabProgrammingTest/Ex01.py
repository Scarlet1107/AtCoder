A = ""

# i = 10
# N = list(str(i))
# print(N)

for i in range(1, 50000):
    # ここでiに８が含まれているかどうかをチュック
    # N = list(str(i))
    # for n in N:
    #     if n == "8":
    
    if "8" in str(i):
        N = list(str(i))
        for n in N:
            if n == "8":
                A = A + "SNOWMAN"
            else:
                A = A + n
        A = A + "-"
    else :         
        A = A + str(i) + "-"


# print(A)

# print(len(A))
print(len(A[388886:388918]))
print(A[388886:388918])
