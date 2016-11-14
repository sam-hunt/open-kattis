'''
Created on 15 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    line = input().split()
    scheme = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    S = len(scheme)
    while len(line) > 1:
        N, message, encoded = int(line[0])%S, str(line[1][::-1]), ""
        for eachchar in message:
            encoded += (scheme[(scheme.find(eachchar) + N)%S])
        print(encoded)
        line = input().split()
        