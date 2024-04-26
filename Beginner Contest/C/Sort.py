N = int(input())
A = list(map(int, input().split()))
Ans = []

"""
計算量的にN^2になって解けなかった

for i in range(N):
    # もうすでにソートされている場合はスキップ。ここでiは配列番号、i+1はほしい数字
    if A[i] == i + 1:
        continue
    else:
        for j in range(i + 1, N):
            if A[j] == i + 1:
                A[i], A[j] = A[j], A[i]
                Ans.append([i + 1, j + 1])
                break


print(len(Ans))
for i in range(len(Ans)):
    print(Ans[i][0], Ans[i][1])
"""


