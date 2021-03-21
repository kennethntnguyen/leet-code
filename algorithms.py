from typing import List

# 7. Reverse Integer
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

    for i in range(0, len(x)):
        reversed_number += int(x[i]) * (10**i)

    if negative:
        reversed_number *= -1

    if (2**31 - 1 < reversed_number) or (reversed_number < -2**31):
        return 0
    else:
        return reversed_number

# 344. Reverse String
def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    i, j = 0, len(s) - 1
    while i < j:
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        i += 1
        j -= 1

# 1. Two Sum
def twoSum(nums: List[int], target: int) -> List[int]:
    num = dict(zip(nums, list(range(len(nums)))))
    i = 0
    length = len(nums)
    while i < length:
        try:
            compliment = target-nums[i]
            if i is not num[compliment]:
                return [i, num[compliment]]
            else:
                i += 1
        except:
            i += 1

# 121. Best Time to Buy and Sell Stock
def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    min_price = float('inf')
    for price in prices:
        min_price = min(price, min_price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit

# 217. Contains Duplicate
def containsDuplicate(nums: List[int]) -> bool:
    number_set = {} 
    for num in nums:
        if num not in number_set.keys():
            number_set[num] = 0
        else:
            number_set[num] += 1
    return sum(number_set.values()) > 0

# 238. Product of Array Except Self
def productExceptSelf(nums: List[int]) -> List[int]:
    total = 1
    zero = False
    
    for num in nums:
        if zero == False:
            if num == 0:
                zero = True
            else:
                total *= num
        else:
            if num != 0:
                total *= num
            else:
                total = 0
                return [total] * len(nums)
    
    N = len(nums)
    total = [total] * N
    
    for i in range(N):
        if zero == False:
            total[i] = int(total[i]/nums[i]) 
        else:
            if nums[i] != 0:
                total[i] = 0
                
    return total
