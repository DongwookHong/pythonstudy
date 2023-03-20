num = int(input())
a = list(map(int , input().split()))
ave = round(sum(a)/num)
min = 2714000000

for index, x in enumerate(a):
    temp = abs(ave-x)
    if(temp <min):
        min = temp
        studnt = index+1
        sol = x
    elif(temp == min):
        if(x >sol):
            studnt =index+1
            sol = x
print(ave,studnt)
