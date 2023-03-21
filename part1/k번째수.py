#자연수  s 번째부터 e 번째 까지의수 오름차순  k번째로 나 타내는 숫자를 출력 하는 프로그램 
# import sys
# sys.stdin=open("input.txt","rt")
count = int(input())

for i in range(count):
    a,b,c,d = map(int,input().split())
    z = list(map(int, input().split()))
    str_num = z[b-1:c]
    str_num.sort
    print("#%d %d" %(i+1,str_num[d-1]))