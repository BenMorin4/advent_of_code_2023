import sys
import re
from collections import defaultdict, Counter # In Python, what is the Counter _ from the  collections Module
D = open("day7.txt", "r").read().strip() # document read and stored
L = D.split("\n") # document split into an array of lines; L = [D[0], D[1], ..., D[n]]
ans = 0

def strength(hand):
    hand = hand.replace('T', chr(ord('9')+1))
    hand = hand.replace('J', chr(ord('1')-1))
    hand = hand.replace('Q', chr(ord('9')+3))
    hand = hand.replace('K', chr(ord('9')+4))
    hand = hand.replace('A', chr(ord('9')+5))
    C = Counter(hand) # Counter - dictionary, key = iterable (number, letter, line), value = number of times seen while iterating
    if list(C.values()) == [5]:
        return (10, hand)
    elif sorted(C.values()) == [1, 4]:
        if C[chr(ord('1')-1)] == 1:
            return (10, hand)
        elif C[chr(ord('1')-1)] == 4:
            return (10, hand)
        else:
            return (9, hand)
    elif sorted(C.values()) == [2, 3]:
        if C[chr(ord('1')-1)] == 2:
            return (10, hand)
        elif C[chr(ord('1')-1)] == 3:
            return (10, hand)
        else:
            return (8, hand)
    elif sorted(C.values()) == [1, 1, 3]:
        if C[chr(ord('1')-1)] == 1:
            return (9, hand)
        elif C[chr(ord('1')-1)] == 3:
            return (9, hand)
        else:
            return (7, hand)
    elif sorted(C.values()) == [1, 2, 2]:
        if C[chr(ord('1')-1)] == 1:
            return (8, hand)
        elif C[chr(ord('1')-1)] == 2:
            return (9, hand)
        else:
            return (6, hand)
    elif sorted(C.values()) == [1, 1, 1, 2]:
        if C[chr(ord('1')-1)] == 1:
            return (7, hand)
        elif C[chr(ord('1')-1)] == 2:
            return (7, hand)
        else:
            return (5, hand)
    elif sorted(C.values()) == [1, 1, 1, 1, 1]:
        if C[chr(ord('1')-1)] == 1:
            return (5, hand)
        else:
            return (4, hand)
    else:
        assert False, f'{C} {hand} [sorted(C.values())]'

H = []
for line in L:
    hand, bid = line.split()
    H.append((hand, bid))
H = sorted(H, key=lambda hb:strength(hb[0]))

for i,(h,b) in enumerate(H):
    ans += (i+1)*int(b)
print(ans)