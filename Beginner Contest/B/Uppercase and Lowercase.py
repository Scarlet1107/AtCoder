S = str(input())

lower = 0
upper = 0
for c in S:
    if c.islower():
        lower += 1
    else:
        upper += 1

if lower >= upper:
    print(S.lower())
else:
    print(S.upper())
