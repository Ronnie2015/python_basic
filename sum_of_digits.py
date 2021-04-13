#Sum of Digits iterative

def SumOfDigits(n):
    Sum = 0
    
    while n > 0:
        Sum += n%10
        n = int(n/10)
    return Sum

n = 1234
print(SumOfDigits(n))

#recursive
#Sum of Digits


def SumOfDigits(n):
    if n <= 0:
        return 0
    return n%10 + SumOfDigits(int(n/10))
    

n = 1234
print(SumOfDigits(n))
