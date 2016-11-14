'''
Created on 15 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    S = input()
    cards = {'P' : set(),
             'K' : set(),
             'H' : set(),
             'T' : set()}
    GRESKA = False
    
    for i in range(int(len(S)/3)):
        card = S[3*i:3*i+3]
        #print(card)
        if str(card[1:]) in cards[card[0]]:
            GRESKA = True
            break
        cards[card[0]].add(str(card[1:]))
        #print(cards)
    
    if not GRESKA: print(13-len(cards['P']), 13-len(cards['K']), 13-len(cards['H']), 13-len(cards['T']))
    else: print("GRESKA")
        