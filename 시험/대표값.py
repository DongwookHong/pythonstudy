import sys
sys.stdin=open("./input.txt","rt")

num = int(input())
a = list(map(int , input().split()))
avg = round(sum(a)/num)
max = 99999999

for index,score in enumerate(a):
    tmp = abs(avg-score)
    if(tmp < max):
        max =tmp
        number = index +1
        mark= score
    elif tmp ==max:
        if mark < score:
            number =index +1
            mark = score
print(avg ,number)            


