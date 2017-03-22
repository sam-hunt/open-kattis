'''
Created on 22 March 2017

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    X, Y, N = [int(i) for i in input().split()]
    [print(('Fizz' if not out % X else '') + ('Buzz' if not out % Y else '') if not (out % X) or not (out % Y) else str(out)) for out in range(1,N+1)]