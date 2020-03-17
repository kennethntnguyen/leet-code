from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    num = dict(zip(nums,list(range(len(nums)))))
    i = 0
    length = len(nums)
    while i < length:
        try:
            compliment = target-nums[i]
            if i is not num[compliment]:
                return [i,num[compliment]]
            else:
                i += 1
        except:
            i += 1
def reverse(x: int) -> int:
    if (-9 < x) and (x < 9):
        return x
    
    negative = x < 0
    if negative:
        x = abs(x)
    
    while (x % 10 == 0):
        x = int(x/10)
    
    x = list(str(x))
    reversed_number = 0
    
    for i in range(0,len(x)):
        reversed_number += int(x[i]) * (10**i)
    
    if negative:
        reversed_number *= -1 
    
    if (2**31 - 1 < reversed_number) or (reversed_number < -2**31):
        return 0
    else:
        return reversed_number
def countPrimes(n: int) -> int:
    n -= 1
    number_of_primes = 0
    def isPrime(x: int) -> bool:
        divisors = (2,3,4,5,6,7,8,9)
        prime_divisors = (2,3,5,7)
        length_divisors = len(divisors)
        if x in prime_divisors:
            return True
        i = 0
        while i < length_divisors:
            if x % divisors[i] == 0:
                return False
            i += 1
        return True
    def isEven(k: int) -> bool:
        if k % 2 == 0:
            return True
        else:
            return False
    if isEven(n):
        n -= 1
    while n > 1:
        if isPrime(n):
            number_of_primes += 1
            print(n)
        n -= 2
    return number_of_primes