S = list(input())
T = list(input())

j = 0

for i in range(len(T)):
    if(S[j] == T[i]):
        print(i+1, end=" ")
        j += 1