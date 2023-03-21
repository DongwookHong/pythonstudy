str = (input())

res =0
cnt =0
for x in str:
    if(x.isdecimal()):
        res = res*10 + int(x)
for i in range(1,res+1):
    if res%i == 0:
        cnt +=1
print(res, cnt)