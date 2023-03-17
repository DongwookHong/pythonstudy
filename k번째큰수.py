import sys

sys.stdin=open("input.txt","rt")

card_deck , big_num= map(int,input().split())
deck_num = list(map(int,input().split()))
arry_num = set()
for i in range(card_deck):
    for j in range(i+1,card_deck):
        for k in range(j+1,card_deck):
            arry_num.add(deck_num[i]+deck_num[j]+deck_num[k])
deck = list(arry_num)
deck.sort(reverse=True)

print(deck[big_num-1])
