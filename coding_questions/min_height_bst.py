'''
# GENERAL NOTES

## It took me the 2-3 minutes to think and plan out strategy
  - Want to traverse the array as if we're doing binary search
  - Want to make a recursive functuin placeholder to pass in indices

## It took me the rest of the time to code and struggle
  - I took a extra 10 minutes to 
## I had no time left to wrap up code and explain examples + walkthrough
## I had no time to get to another solution
## Took 15 mins extra to sift through errors
## Watched a Neetcode video on this exact problem, mimicked it in solution 3

## TOTAL TIME: 30min (+15min extra, +5min for this reflection) = 45-50 minutes
---------------------------------------------------------------
# REFLECTIONS
  What went well:
    - I was able to devise a strategy quick
    - I was able to divide my functionality up well
    - I was able to put up a placeholder function while explaining in stride

  What went wrong:
    - I forgot to ask clarifying questions 
      - This hurt me when I didn't think to use the insert function
      - I passed in too many parameters to the BST class because of this
    - I messed up using python splicing (e.g didn't put first index)
    - I didn't know whether I should've floored the midpoint or not
'''

import math


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''


''' First solution I came up with.

'''
def min_height_bst_1(array):
  arr_len = len(array)

  if arr_len == 0: return None
  if arr_len == 1: return BST(array[0])
      
  midpoint = math.floor(arr_len / 2)

  root = BST(array[midpoint])

  left = construct_bst_1(0, midpoint, array[0:midpoint], root)
  right = construct_bst_1(midpoint, arr_len, array[midpoint:arr_len], root)
  
  root = BST(array[midpoint])
  root.insert(left)
  root.insdert(right)

  return root


def construct_bst_1(left, right, subarr):
    # Base case: 
    if len(subarr) <= 1: return subarr[0]

    arr_len = right - left
    midpoint = math.floor(arr_len / 2)

    subroot = BST(subarr[midpoint])
    # Recursive case
    left = construct_bst_1(left, midpoint, subarr[0:midpoint])
    subroot.insert(left)
    right = construct_bst_1(midpoint, arr_len, subarr[midpoint:right])
    subroot.insert(right)

    return subarr[midpoint]

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

''' Second solution I came up with.
'''
def min_height_bst_2(array):
  arr_len = len(array)

  if arr_len == 0: return None
  if arr_len == 1: return BST(array[0])
      
  midpoint = math.floor(arr_len / 2)

  root = BST(array[midpoint])

  construct_bst_2(0, midpoint - 1, array, root)
  construct_bst_2(midpoint + 1, arr_len, array, root)
  
  return root

   

def construct_bst_2(left, right, array, root):
    # Base case: 
    if right <= left:
        # print("Child", array[right])
        # print("Array", str(array[left:right+1]))
        # print("Left", left)
        # print("Right", right)
        # print("-----------------------")

        return array[left]


    print("Array", str(array[left:right+1]))
    print("Left", left)
    print("Right", right)
    
    midpoint = math.floor((right + left) / 2)

    print("Midpoint index", midpoint)
    print("Midpoint value", array[midpoint])
    print("-----------------------")

    root.insert(array[midpoint])
 
    root.insert(construct_bst_2(left, midpoint, array, root.left))
    root.insert(construct_bst_2(midpoint + 1, right, array, root.right))

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''


''' Final solution that I replicated from AlgoExpert video.
'''
def min_height_bst_3(array):
    arr_len = len(array)

    if arr_len == 0: return None
    if arr_len == 1: return BST(array[0])
    
    return  construct_bst_3(0, arr_len, array)

def construct_bst_3(left, right, array):
    # Base case: 
    if right <= left:
        return None
    
    midpoint = math.floor((right + left)/2)
    subroot = BST(array[midpoint])
 
    subroot.left = construct_bst_2(left, midpoint, array)
    subroot.right = construct_bst_3(midpoint + 1, right, array)

    return subroot