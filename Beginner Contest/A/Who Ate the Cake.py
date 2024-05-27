A, B = map(int, input().split())

Arr = [1, 2, 3]



Arr.remove(A)
if(A != B):
    Arr.remove(B)

if(len(Arr) == 1):
    print(Arr[0])
else:
    print(-1)