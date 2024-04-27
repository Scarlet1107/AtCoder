import collections

S = input().strip()

# 各文字の出現回数をカウント
char_count = collections.Counter(S)

# 各出現回数が何回出現するかをカウント
frequency_count = collections.Counter(char_count.values())

# 各出現回数の頻度が0または2であることを確認
good_string = True

for freq in frequency_count.values():  # 修正点: frequency_countの値に対してループ
    if freq != 2 and freq != 0:
        good_string = False
        break

# 出力
print("Yes" if good_string else "No")
