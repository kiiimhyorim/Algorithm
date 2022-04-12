import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
cards = {}

for i in range(n):
    if card[i] not in cards.keys():
        cards[card[i]] = 1
    else:
        cards[card[i]] +=1
m = int(input())
M = list(map(int, input().split()))

for i in range(m):
    if M[i] in cards:
        print(cards[M[i]], end=' ')
    else:
        print(0, end=' ')