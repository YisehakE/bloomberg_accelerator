


'''
Input: [2,4,5,10]
Output: 7

VAR -> possibilities
SORT & REVERSE
INIT SET POINTERS 
    target -> 0
    L -> target_i + 1
    R -> LEN(ARR) - 1

IF L * R < TARGET:
    R -= 1
IF L * R > TARGET:
    L += 1
IF L * R == TARGET: 
    IF L != R: VAR += 2
    ELSE: VAR += 1
    R -= 1

[10, 5, 4, 2]

ITERATION 1
    target = 10
    l = 5
    r = 2

    5 * 2 == 10
        5 != 2: possible += 2
        l += 1
        r -= 1

ITERATION 2
    target = 10
    l = 5
    r = 4

    5 * 4 > 10
        L += 1

ITERATION 3
    target = 10
    l = 4
    r = 4

    4 * 4 > 10
        l += 1
ITERATION 4

    target = 10
    l = 2
    r = 4

    L < R:
        target += 1
        l = target + 2
        r = len(arr) - 1
    



Failing test case
  Input: [18, 6, 2, 3]
  My output:    [ [18], [6], [3], [2],
                  [18, 6, 3], [18, 3, 6],
                  [6, 3, 2], [6, 2, 3]
                ]
  Expected output; [ [18], [6], [3], [2],
                     [18, 6, 3], [18, 3, 6],
                     [6, 3, 2], [6, 2, 3],
                     [18, 6, 3, 3, 2],
                     [18, 6, 3, 2, 3],
                     [18, 3, 6, 3, 2],
                     [18, 3, 6, 2, 3]
                    ]


     18                18               18                   18
    /  \              /  \             /  \                 /  \
   6    3            6    3           3     6              3    6
  / \                / \                   / \                 / \
 2   3              3   2                 2   3               3   2

[18, 6, 3, 2, 3]  [18, 6, 3, 3, 2]    [18, 3, 6, 2, 3]     [18, 3, 6, 3, 2]
        

'''
    
def numFactoredBinaryTrees_1(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    arr.sort(reverse=True)
    possible = len(arr)

    target = 0
    l = target + 1
    r = len(arr) - 1

    while target < len(arr):
        while l < len(arr) and l <= r:
            if arr[l] * arr[r] > arr[target]:
                l += 1
            elif arr[l] * arr[r] < arr[target]:
                r -= 1
            else:
                if arr[l] == arr[r]:
                    possible += 1
                else:
                    possible += 2
                l += 1
                r -= 1
                
                
        target += 1
        l = target + 1
        r = len(arr) - 1

    return possible

def numFactoredBinaryTrees_2(arr):
  # Approaching this DP question from bottom up (i.e building from smaller stored values in iterative fashion rather than recursive)

  n = len(arr)
  arr.sort() # Sort in ascending order | T: O(nlogn) S: O(1)
  dp = [1] * n # Create DP memoization structure, default values of 1
  num_set = set(arr) # Initialize set containing values in array | T: O(n) S: O(n)

  num_index_map = dict([ (num, i) for num, i in enumerate(arr)]) # Map to store index of any num in array | T: O(n) S: O(n)
    

  for i in range(1, n): # Start from 1 so inner for loop can at least go up to the value in array at i (i.e single root nodes count)
      for j in range(i): # Iterate up to i
          num2 = arr[i] // arr[j] # Retrieve a possible factor for current num we're looking at 

          if num2 in num_set: # See if this obtained factor  exist in arr | T: O(1) S: O(1)
              index2 = num_index_map[num2] # Find associated 
              dp[i] = dp[j] * dp[index2]
  

  mod = pow(10, 9) + 7 # We want to cap how many possibilities exist
  return sum(dp[n]) % mod # Sum up all the values in DP modded by cap | 

