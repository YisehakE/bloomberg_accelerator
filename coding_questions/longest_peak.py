'''
# Original Answer

## Time
  * Alloted = 15 mins

  - Actual = 15 mins
  - Extra = 15 mins

  - Total = 30 mins

## Reflection


'''


def longest_peak_1(array):
    if len(array) < 3:
        return 0
    if len(array) == 3:
        isPeak = array[0] < array[1] < array[2]
        return 3


    start_p = array[0]
    mid_p = None

    longest = 0

    for i in range(1, len(array)):
        curr = array[i]
        prev = array[i - 1]

        if curr == prev:
            start_p = i
            
        if (mid_p and curr > prev) or start_p == i:
            longest = i - start_p
            start_p = i
            mid_p = None
        elif not mid_p and curr < prev:
            mid_p = prev

    if not mid_p:
        longest = len(array) - start_p

    return longest


'''
  ## Assumption(s)
    *Tip: just write their answer and MAYBE briefly what I asked


  ## Walkthrough
    Input: [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
    Output: 6
    ^ View above function declaration for steps!

  ## Time complexity

    Time ~ O(N), linear time
    - ADD WHY
    Space ~ O(1), constant space
    - ADD WHY
-------------------------------------------------------
## Time
  * Alloted = 20 mins

  - Actual = mins
  - Extra =  mins

  - Total = mins


## Reflection
 - 

'''

'''

Walkthrough steps

SP = 0
MP = None
L = 0

CURR = 2
PREV = 1

--> 

SP = 0
MP = None
L = 0

CURR = 2
PREV = 1




'''


 # [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
def longest_peak_2(array):
    if len(array) < 3:
        return 0
    if len(array) == 3:
        isPeak = array[0] < array[1] > array[2]
        return 3 if isPeak else 0 # FIX: utilized the boolean according to peak logic

    start_p, mid_p, longest = 0, None, 0 # FIX: changed from value to index and just single lined instatiations

    for i in range(1, len(array)):
        curr, prev = array[i], array[i - 1] # FIX: just single lined instatiations

        if mid_p and curr >= prev:
          longest = i - start_p + 1
          start_p = i
          mid_p = None
        elif curr == prev:
          start_p = i
          mid_p = None
        elif curr < prev:
          mid_p = i - 1

    if mid_p: # FIX: Midpoint must be to check this edge case
        longest = len(array) - start_p

    return longest


test_arr_1 = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
print(longest_peak_2(test_arr_1))

test_arr_2 = [1, 2, 3, 3]
print(longest_peak_2(test_arr_2))

test_arr_3 = [1, 2, 3, 2]
print(longest_peak_2(test_arr_3))

test_arr_4 = [1, 2, 3, 2, 1]
print(longest_peak_2(test_arr_4))

test_arr_5 = [1, 2, 2]
print(longest_peak_2(test_arr_5))

test_arr_6 = [1, 2, 1]
print(longest_peak_2(test_arr_6))

test_arr_7 = [1, 2]
print(longest_peak_2(test_arr_7))
