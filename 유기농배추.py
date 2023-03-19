

case = int(input())
for i in range(case):
    M , N, K = list(map(int, input()))
    
    arr = [[0 for width in range(M)]for len in range(N)]
    for j in range(K):
        a ,b = list(map(int, input()))
    i