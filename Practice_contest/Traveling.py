def main():
    N = int(input())
    T, X, Y = [0], [0], [0]

    for i in range(N):
        t, x, y = map(int, input().split())
        T.append(t)
        X.append(x)
        Y.append(y)
    
    # print(T, X, Y)

    marker = False
    for i in range(N):
        if checkTravelCheck(T[i], X[i], Y[i], T[i + 1], X[i + 1], Y[i + 1]):
            marker = True
        else:
            marker = False
    
    if marker:
        print("Yes")
    else:
        print("No")


def checkTravelCheck(T1, X1, Y1, T2, X2, Y2):
    # ここで時間的に到達可能かどうかを判定する
    timeLimit = T2 - T1
    
    if(timeLimit - abs(X2 - X1) - abs(Y2 - Y1)) < 0:
        return False
    
    if (timeLimit - abs(X2 - X1) + abs(Y2 - Y1)) % 2 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
