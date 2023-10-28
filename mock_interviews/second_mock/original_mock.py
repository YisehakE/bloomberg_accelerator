

'''
Finding the largest increase in series of prices:

Example 1:
    Input:
    9 8 9 10 -> 2.

Example 2:

    9 8 7 -> None
    
    Output: 2
Example 3:
    10 11 12 15  14 12 18 10 9 16 18
 t: 0   1 2  3 .....   
    
  7   7 12 15 -> 5
  7      12 18          -> 6 (better 8)
  7         10
9    9 16 18 -> 9
 
 
 10 11 15 7 11
 
  10 10 11 15  -> 5
  7   7 11. -> 4
 
 min(10, 7) = 7
   
8
       
    
    min(10, 12) = 10
    min(10, 9) = 9

Constraint on series of prices:

Type - integers
   2 <=n < 10K
'''

def bruteForceLargestInc(prices):
    
    if len(prices) == 2: 
        return prices[1] - prices[0]
    
    maxInc = 0
    for i in range(len(prices)):
        for j in range(len(prices)):
            # Keep max of increase after subtracting

            if i != j:
                inc = prices[j] - prices[i]
                
                if inc > maxInc:
                    maxInc = inc
            
    return maxInc # Time: O(N^2) Space: O(1)
    
    
def findLargestInc(prices):
    
    minPrice = prices[0]
    maxInc = 0
    for i in range(len(prices)):
        if i != 0:
            if prices[i] < prices[i-1]:
                minPrice = prices[i]
            else:
                maxInc = max(maxInc, prices[i] - minPrice)
            
            
    return maxInc




''''





'''
                
    

