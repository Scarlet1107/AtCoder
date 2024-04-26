N = input()
A = list(map(int, input().split()))

for i in range(len(A)):
    count = 0
    while A[i] % 2 == 0:
        A[i] = A[i] / 2
        count += 1
    if i == 0:
        min_count = count
    else:
        if count < min_count:
            min_count = count
print(min_count)
