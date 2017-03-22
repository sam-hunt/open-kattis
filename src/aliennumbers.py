'''
Created on 22 March 2017

@author: Sam
'''

# Python 3.5

def toDecimal(anum, alang):
    decimalSum, base = 0, len(alang)
    for i in range(1,len(anum)+1):
        decimalSum += alang.find(anum[-i]) * (base ** (i-1))
    return decimalSum

def toAlien(decimalNum, alang):
    base, alienNum, step = len(alang), [], 0
    while decimalNum > 0:
        alienNum.append(alang[decimalNum % base])
        decimalNum -= decimalNum % base
        decimalNum = int(decimalNum / base)
        step += 1
    alienNum.reverse()
    return ''.join(alienNum)

if __name__ == '__main__':
    cases = int(input())
    for eachCase in range(1, cases+1):
        alienNum1, alienLang1, alienLang2 = input().split()
        alienNum2 = toAlien(toDecimal(alienNum1, alienLang1), alienLang2)
        print('Case #' + str(eachCase) + ': ' + alienNum2)