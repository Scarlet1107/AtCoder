N = int(input())
Result = []

for i in range(N):
    if(i % 3 == 0 or i % 3 == 1):
        Result.append("o")
    else:
        Result.append("x")
    
print("".join(Result))