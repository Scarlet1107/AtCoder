N, T = map(int, input().split())
A = list(map(int, input().split()))

Bingo = [[0] * N for _ in range(N)]

print(Bingo)
# ビンゴの数字を入れる
for i in range(len(A)):
    x = A[i] % N - 1
    y = A[i] // N

#　縦をチェック

#　横をチェック

#　斜めをチェック(座標的にありえない場合もあるから注意)

#　ビンゴがあればYesを出力