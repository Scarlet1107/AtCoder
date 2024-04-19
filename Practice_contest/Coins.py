A = input()
B = input()
C = input()
X = input()

count = 0

while True:
    a = A
    b = B
    c = C
    x = X
    while True:
        if x == 0:
            break
        if x >= 500 and a > 0:
            x -= 500
            a -= 1
        elif x >= 100 and b > 0:
            x -= 100
            b -= 1
        elif x >= 50 and c > 0:
            x -= 50
            c -= 1        
        