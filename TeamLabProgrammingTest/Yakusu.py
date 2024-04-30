n = 1022221200

count = 0
for i in range(10000, 100000):
    if n % i == 0:
        count += 1
        
        
print(count)