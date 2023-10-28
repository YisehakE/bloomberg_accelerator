
'''
# Finding the largest increase in series of prices:
Given an series of numbers, which you can think of as prices of a stock, ________, etc, we want you to find the maximum
increase that can be found in said series.

## LeetCode reference 
  Question 121: Best time to buy and sell a stock
  - Very similiar, only difference is that if no increase you'd report back a None in this variation

## Assumptions/clarifying questions

   Q: Is there any constraint on the series of prices? Whether it's the individual value OR length of series?:
   A: - Type of price: integers
      - Prices length: 2 <= n < 10K
   Q: Can we assume the position of the price, i.e the index, to be the time at which stock was valued?
   A: Yes


## Examples
  Example 1:
      Input: [9, 8, 9, 10]
      Output: 2
      (Between 8 and 10)

  Example 2:
      Input: [9, 8, 7]
      Output: None
      (Nonincreasing series)

  Example 3:
      Input: [10, 11, 12, 15, 12, 18, 10, 9, 16, 18]
      Output: 8
      (Between 9 and 18)


## Walkthrough!

  Example 3...  
    Given: [10, 11, 12, 15, 12, 18, 10, 9, 16, 18]
    
    10 12 15     | min price = 10 <> max inc = 5
      12 18      | min price = 10 <> max inc = 8
        9 16 18  | min price =  9 <> max inc = 9

  Example 3 (alternative posed by Chris)
    Given: [10 11 15 7 11]
 
    10 10 11 15 | min price = 10 <> max inc = 5
      7 11      | min price = 7 <> max inc = 11
 
'''

def findLargestInc1(prices):
    if len(prices) < 2: return None
    
    maxInc = 0
    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
          inc = prices[j] - prices[i]
          maxInc = max(maxInc, inc)
            
    return None if maxInc == 0 else maxInc # Time: O(N^2) Space: O(1)
    
    
def findLargestInc2(prices):
    if len(prices) < 2: return None

    minPrice = prices[0]
    maxInc = 0
    for i in range(len(prices)):
        if i != 0:
            if prices[i] < prices[i-1]:
                minPrice = min(minPrice, prices[i])
            else:
              maxInc = max(maxInc, prices[i] - minPrice)
                
    return None if maxInc == 0 else maxInc # Time: O(N) Space: O(1)



print("---------------------------------------\n Example 1: Repeat prices \n---------------------------------------")
test_1_prices = [9, 8, 9, 10]

test_1_inc_brute = findLargestInc1(test_1_prices)
test_1_inc_optim = findLargestInc2(test_1_prices)

assert(test_1_inc_brute == 2)
assert(test_1_inc_optim == 2)

print("Test 1 (Brute)|| Prices: ", test_1_prices, " | Expected increase: ", 2, " vs Actual increase: ", test_1_inc_brute)
print("Test 1 (Optimized)|| Prices: ", test_1_prices, " | Expected increase: ", 2, " vs Actual increase: ", test_1_inc_optim, "\n")


print("---------------------------------------\n Example 2: Non-increasing prices \n---------------------------------------")
test_2_prices = [9, 8, 7]
test_2_inc_brute = findLargestInc1(test_2_prices)
test_2_inc_optim = findLargestInc2(test_2_prices)

assert(test_2_inc_brute == None)
assert(test_2_inc_optim == None)

print("Test 2 (Brute)|| Prices: ", test_2_prices, " | Expected increase: ", None, " vs Actual increase: ", test_2_inc_brute)
print("Test 2 (Optimized)|| Prices: ", test_2_prices, " | Expected increase: ", None, " vs Actual increase: ", test_2_inc_optim, "\n")

print("---------------------------------------\n Example 3: long series \n---------------------------------------")
test_3_prices = [10, 11, 12, 15, 12, 18, 10, 9, 16, 18]

test_3_inc_brute = findLargestInc1(test_3_prices)
test_3_inc_optim = findLargestInc2(test_3_prices)

assert(test_3_inc_brute == 9)
assert(test_3_inc_optim == 9)

print("Test 3 (Brute)|| Prices: ", test_3_prices, " | Expected increase: ", 9, " vs Actual increase: ", test_3_inc_brute)
print("Test 3 (Optimized)|| Prices: ", test_3_prices, " | Expected increase: ", 9, " vs Actual increase: ", test_3_inc_optim, "\n")

print("---------------------------------------\n Example 4: series of 1 price only \n---------------------------------------")
test_4_prices = [9]

test_4_inc_brute = findLargestInc1(test_4_prices)
test_4_inc_optim = findLargestInc2(test_4_prices)

assert(test_4_inc_brute == None)
assert(test_4_inc_optim == None)

print("Test 4 (Brute)|| Prices: ", test_4_prices, " | Expected increase: ", None, " vs Actual increase: ", test_4_inc_brute)
print("Test 4 (Optimized)|| Prices: ", test_4_prices, " | Expected increase: ", None, " vs Actual increase: ", test_4_inc_optim, "\n")

print("---------------------------------------\n Example 5: series of 2 prices only \n---------------------------------------")
test_5_prices = [9, 14]

test_5_inc_brute = findLargestInc1(test_5_prices)
test_5_inc_optim = findLargestInc2(test_5_prices)

assert(test_5_inc_brute == 5)
assert(test_5_inc_optim == 5)

print("Test 5 (Brute)|| Prices: ", test_5_prices, " | Expected increase: ", 5, " vs Actual increase: ", test_5_inc_brute)
print("Test 5 (Optimized)|| Prices: ", test_5_prices, " | Expected increase: ", 5, " vs Actual increase: ", test_5_inc_optim, "\n")






''' 
# REFLECTIONS

## Chris Feedback
  * [TO CHRIS] CAN YOU ADD THE NOTES YOU MADE HERE?
  

## Personal Feedback
* Things that I found that I've done well or could improve on

 ### During the interview
  - 

 ### During fixing solution


'''