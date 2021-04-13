#Sum of Digits

def SumOfDigits(n):
    Sum = 0
    
    while n > 0:
        Sum += n%10
        n = n / 10
    return int(Sum)

n = 1234
print(SumOfDigits(n))
