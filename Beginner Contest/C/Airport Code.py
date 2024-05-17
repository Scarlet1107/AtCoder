S = str(input())
T = str(input())
count = 0
j = 0

for i in range(len(T)):
    while j < len(S):
        if(T[i] == S[j].upper()):
            count += 1
            j += 1
            break
        else:
            j += 1

if(count == 3 or (count == 2 and T[2] == "X")):
    print("Yes")
else:
    print("No")
    