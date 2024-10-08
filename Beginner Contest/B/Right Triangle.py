def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    L1 = calcSquaredDistance(x1, y1, x2, y2)
    L2 = calcSquaredDistance(x2, y2, x3, y3)
    L3 = calcSquaredDistance(x3, y3, x1, y1)
    ans = isRightTriangle(L1, L2, L3)
    print("Yes" if ans else "No")


def calcSquaredDistance(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2


def isRightTriangle(L1, L2, L3):
    return L1 == L2 + L3 or L2 == L1 + L3 or L3 == L1 + L2


if __name__ == "__main__":
    main()
