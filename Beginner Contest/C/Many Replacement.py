def compress_and_modify(S, Q):
    # 圧縮
    compressed = []
    count = 1
    for i in range(1, len(S)):
        if S[i] == S[i - 1]:
            count += 1
        else:
            compressed.append(f"{S[i-1]}{count if count > 1 else ''}")
            count = 1
    compressed.append(f"{S[-1]}{count if count > 1 else ''}")
    T = ''.join(compressed)

    # 置き換え
    for _ in range(Q):
        a, b = input().split()
        T = T.replace(a, b)

    return T

def decompress(compressed_string):
    # 解凍
    Ans = []
    i = 0
    while i < len(compressed_string):
        if compressed_string[i].isdigit():
            count = ""
            while i < len(compressed_string) and compressed_string[i].isdigit():
                count += compressed_string[i]
                i += 1
            Ans.append(compressed_string[i-1-len(count)] * (int(count)-1))
        else:
            Ans.append(compressed_string[i])
            i += 1

    return ''.join(Ans)

# 入力処理
N = int(input())
S = input()
Q = int(input())

# 圧縮と置き換え
compressed_modified = compress_and_modify(S, Q)

# 解凍
result = decompress(compressed_modified)

# 結果の出力
print(result)
