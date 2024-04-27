S = str(input())

unique_substrings = set()

for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        unique_substrings.add(S[i:j])

print(len(unique_substrings))