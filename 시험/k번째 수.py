case = int(input())

for i in range (case):
    n, s,e,k = list(map(int, input().split()))
    num =list(map(int, input().split()))
    str_num= num[s-1:e]
    str_num.sort()
    print(str_num[k-1])
