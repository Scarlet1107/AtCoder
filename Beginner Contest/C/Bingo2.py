N, T = map(int, input().split())
A = list(map(int, input().split()))

Bingo = [[0] * N for _ in range(N)]

# print(Bingo)
# ビンゴの数字を入れる
for i in range(T):
    A[i] -= 1
    x = (A[i] % N)
    y = (A[i] // N)
    Bingo[y][x] = 1
    # print("x: ", x, "y: ", y)
    
    # for j in range(N):
    #     print(Bingo[j])
    
    #　縦をチェック
    for j in range(N):
        if(Bingo[j][x] == 0):
            break
    else:
        print(i+1)
        exit()
    
    #　横をチェック
    for j in range(N):
        # print("j: ", j, "y: ", y, "A[i]: ", A[i], "Bingo[j][y]: ", Bingo[j][y])
        if(Bingo[y][j] == 0):
            # print("break")
            break
    else:
        print(i+1)
        exit()

    #　斜めをチェック(座標的にありえない場合もあるから注意)
    if(x == y):
        for j in range(N):
            if(Bingo[j][j] == 0):
                break

        else:
            print(i+1)
            exit()
            
    if(x == N - y - 1):
        for j in range(N):
            if(Bingo[j][N - j - 1] == 0):
                break
        else:
            print(i+1)
            exit()
    
#　ビンゴがなければ-1を出力
print(-1)