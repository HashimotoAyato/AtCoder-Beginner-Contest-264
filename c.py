# input
H1, W1 = map(int, input().split())
A = []
for h in range(H1):
    A.append(list(map(int, input().split())))
H2, W2 = map(int, input().split())
B = []
for h in range(H2):
    B.append(list(map(int, input().split())))

# functions
def del_col(X, c):
    x = []
    for i in range(len(X)):
        x.append(X[i][:c]+X[i][c+1:])
    return x

def del_row(X, r):
    x = X[:r] + X[r+1:]
    return x

# main
stack = []
stack.append(A)
check = False
while len(stack) > 0:
    x = stack.pop()
    print(len(stack))
    if x == B:
        check = True
        break

    if len(x) > len(B): 
        for i in range(len(x)):
            stack.append(del_row(x,i))
    if len(x[0]) > len(B[0]):
        for i in range(len(x[0])):
            stack.append(del_col(x,i))
    else:
        continue

print('Yes' if check else 'No')