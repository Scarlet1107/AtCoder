N = int(input())

plant = 1
i = 1
while plant <= N:
    plant += 2**i
    i += 1
    
print(i)