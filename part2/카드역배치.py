import sys
sys.stdin=open("abc.txt","rt")

t = list (range(21))

for _ in range(10):
    a , b = map(int, input().split())
    for i in range((b -a+1)//2):
        t[a+i],t[b-i] =t[b-i],t[a+i]
t.pop(0)
print(t)