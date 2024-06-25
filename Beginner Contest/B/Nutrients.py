# numpyを使うことで配列同士の引き算を可能にしている

import numpy as np

N, M = map(int, input().split())
A = np.array(list(map(int, input().split())))

X = []
for i in range(N):
    X = np.array(list(map(int, input().split())))
    A -= X
    
print("Yes" if all(x <= 0 for x in A ) else "No")
