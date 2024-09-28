R, G, B = map(int, input().split())
Color = str(input())

match str(Color[0]):
    case "R":
        print(min(G, B))
    case "G":
        print(min(R, B))
    case "B":
        print(min(R, G))
