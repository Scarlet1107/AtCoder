def main():
    N, Y = map(int, input().split())

    # 10000円、5000円、1000円札で全探索
    for x in range(N + 1):  # 10000円札の枚数x
        for y in range(N - x + 1):  # 5000円札の枚数y、残りの枚数から計算
            z = N - x - y  # 1000円札の枚数z
            if 10000 * x + 5000 * y + 1000 * z == Y:
                print(x, y, z)
                return  # 正しい組み合わせが見つかった場合、出力して終了
    # どの組み合わせも条件を満たさなかった場合
    print("-1 -1 -1")

if __name__ == "__main__":
    main()
