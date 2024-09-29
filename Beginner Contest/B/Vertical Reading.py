S, T = map(str, input().split())

for w in range(1, len(S)):
    for c in range(w):
        l = []
        for i in range(c, len(S), w):
            l.append(S[i])
        if "".join(l) == T:
            print("Yes")
            exit()

print("No")
