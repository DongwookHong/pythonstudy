num , big = map(int,input().split())

card_num = list(map(int, input().split()))

card_fix = set()

for i in range(num):
    for j in range(i+1, num):
        for k in range(j+1,num):
            card_fix.add(card_num[i]+card_num[j]+card_num[k])
list_card = list(card_fix)
list_card.sort(reverse=True)
print(list_card[big-1])


