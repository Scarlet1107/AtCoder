N, K = map(int, input().split())
A = list(map(int, input().split()))

space = K
count = 1
i = 0

while i < N:
    if(A[i] <= space):
        space -= A[i]
        i += 1
    else:
        space = K
        count += 1
        continue


print(count)