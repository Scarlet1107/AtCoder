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


# 値からそのインデックスへのマッピングを作成
index_map = {value: i for i, value in enumerate(A)}
Ans = []

for i in range(N):
    correct_value = i + 1
    if A[i] != correct_value:
        # 正しい値が現在あるインデックスを見つける
        swap_idx = index_map[correct_value]
        
        # インデックスマップを更新
        index_map[A[i]] = swap_idx
        index_map[correct_value] = i
        
        # 実際の配列で値を交換
        A[i], A[swap_idx] = A[swap_idx], A[i]
        
        # 交換記録を保存
        Ans.append((i + 1, swap_idx + 1))

print(len(Ans))
for x, y in Ans:
    print(x, y)
