'''
Created on 13 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    N = int(input())
    answers = input()
    Adrian, AScore = "ABC", 0
    Bruno, BScore = "BABC", 0
    Goran, GScore = "CCAABB", 0
    
    for eachanswer in enumerate(answers):
        if eachanswer[1] == Adrian[eachanswer[0] % len(Adrian)]:
            AScore += 1
        if eachanswer[1] == Bruno[eachanswer[0] % len(Bruno)]:
            BScore += 1
        if eachanswer[1] == Goran[eachanswer[0] % len(Goran)]:
            GScore += 1
    maxscore = max([AScore, BScore, GScore])
    print(maxscore)
    if AScore == maxscore:
        print("Adrian")
    if BScore == maxscore:
        print("Bruno")
    if GScore == maxscore:
        print("Goran")
    
    