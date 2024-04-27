import math

N = int(input())

points = []

for i in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

# check farthest point

for i in range(N):
    max_distance = 0
    for j in range(N):
        if i == j:
            continue
        distance = math.sqrt(
            (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
        )
        if distance > max_distance:
            max_distance = distance
            max_distance_number = j + 1
        
    print(max_distance_number)