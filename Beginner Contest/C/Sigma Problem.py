N = int(input())
A = list(map(int, input().split()))
M= 10**8
count = 0

A = sorted(A, reverse=True)

# print("after sorting", A)

for i in range(N):
    for j in range(i+1, N):
        if(A[i]+ A[j] >= M):
            count += 1
        else:
            break

print(sum(A)*(N-1) - count*M)




