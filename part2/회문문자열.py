num = int(input())

str = list(map(str,input().split()))
for index,x in enumerate(str):
    rever=x[::-1]
    rever_upper=rever.upper()
    x_upper=x.upper()
    if rever_upper == x_upper:
        print("#%d YES" % (index+1))
    else:
        print("#%d NO" % (index+1))
