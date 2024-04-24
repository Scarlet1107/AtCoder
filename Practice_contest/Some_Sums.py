N, A, B = map(int, input().split())

count = 0


# N回のループ
for i in range(1, N + 1):
    temp_sum = 0
    j = i
    # まず数字をここで分解
    while j >= 10:
        temp_sum += j % 10
        j = j // 10
        
    temp_sum += j
    if temp_sum >= A and temp_sum <= B:
        count += i

print(count)
