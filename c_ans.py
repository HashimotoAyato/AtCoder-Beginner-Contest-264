from itertools import combinations
from re import L

# input
H1, W1 = map(int, input().split())
A = []
for h in range(H1):
    A.append(list(map(int, input().split())))
H2, W2 = map(int, input().split())
B = []
for h in range(H2):
    B.append(list(map(int, input().split())))

# main
h_idx, w_idx = list(range(H1)), list(range(W1))
for h in combinations(h_idx, H2):
    for w in combinations(w_idx, W2):
        check = True
        for i in range(H2):
            for j in range(W2):
                if B[i][j] == A[h[i]][v[j]]:
                    continue
                else:
                    check = False
                    break
        if check:
            break

print('Yes' if check else 'No')