R, C = map(int, input().split())

R = abs(R-8)
C = abs(C-8)

a = max(R,C)

print('white' if a % 2 == 0 else 'black')