S = list(input())
A = {'a':1, 't':2, 'c':3, 'o':4, 'd':5, 'e':6, 'r':7}

count = 0
for i in range(len(S)):
    for j in range(len(S)-1,i,-1):
        if A[S[j-1]] > A[S[j]]:
            S[j-1], S[j] = S[j], S[j-1]
            count += 1

print(count)