import math

# Definition for a binary tree node.
class TreeNode:
    
    # Static variables added to tackle problem
    smallest = None
    node_dict = {}


    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
Assumption(s):
- Can't assume k <= n
- Therefore, could be errors with the k values
  - Ex: 
    - call w/ k = 0 or k > n should return some distinguished value 
'''
class Solution:

  ''' Recursive function to determine kth smallest element in BST.
  @type node: TreeNode
  @param node: any given node in a BST.

  @type pos: int
  @param pos: the current position when traversing a BST, in ascending order.

  @rtype: int
  @returns: the current position before travesing to the next node in ascending order.
  '''
  def findKthSmallest(self, node, pos, k):
    if node is None: return pos
          
    prev_pos = self.findKthSmallest(node.left, pos, k)

    # 2 ways utilizing given class to solve problem
    # TreeNode.node_dict[prev_pos + 1] = node.val # O(n) space complexity
    if prev_pos + 1 == k: TreeNode.smallest = node.val # O(1) space complexity

    if TreeNode.smallest != None: return prev_pos + 1 # A shortstop for traversing

    return self.findKthSmallest(node.right, prev_pos + 1, k)



  ''' Retrieves the kth smallest node value from a BST.
  @type root: TreeNode
  @param root: the root of given BST.

  @type k: int
  @param k: the index of smallest element we want.

  @rtype: int
  @returns: a integer value representing smallest kth element in BST.
  '''
  def kthSmallest(self, root: TreeNode, k: int) -> int:
        

        self.findKthSmallest(root, 0, k)

        temp1 = TreeNode.node_dict.get(k)
        temp2 = TreeNode.smallest

        resetTreenodeStatics()
        return temp1, temp2
  

''' Function to reset static variables in given TreeNode class.
@returns: nothing
@type: None
'''
def resetTreenodeStatics():
    TreeNode.node_dict.clear()
    TreeNode.smallest = None

def testKthSmallest(soln, root, k, value):
  actual = soln.kthSmallest(root, k)
  print("MAP || #" + str(k) + " smallest element || " + str(actual[0]))
  print("INT || #" + str(k) + " smallest element || " + str(actual[1]) + "\n")
  assert(actual[0] == value)
  assert(actual[1] == value)

soln = Solution()



print("-------------------------------------- Case 1: Single node")
'''
          10
'''
root = TreeNode(10, None, None)


# Good tests
testKthSmallest(soln, root, 1, 10)

# Error tests
testKthSmallest(soln, root, 0, None)

print("-------------------------------------- Case 2: Left & single sub branch only")
'''
          10
         / 
        5    
  
'''
leftSub = TreeNode(5, None, None)
root = TreeNode(10, leftSub, None)

testKthSmallest(soln, root, 1, 5)
testKthSmallest(soln, root, 2, 10)

print("-------------------------------------- Case 3: Right & single sub branch only")
'''
          10
            \
             15 
'''
rightSub = TreeNode(15, None, None)
root = TreeNode(10, None, rightSub)

testKthSmallest(soln, root, 1, 10)
testKthSmallest(soln, root, 2, 15)

print("-------------------------------------- Case 4: Left/Right single sub branch")
'''
          10
         /  \
        5    15 
'''
leftSub = TreeNode(5, None, None)
rightSub = TreeNode(15, None, None)
root = TreeNode(10, leftSub, rightSub)

testKthSmallest(soln, root, 1, 5)
testKthSmallest(soln, root, 2, 10)
testKthSmallest(soln, root, 3, 15)


print("-------------------------------------- Case 5: Perfect BST")
leftSub = TreeNode(5, TreeNode(3, None, None), TreeNode(9, None, None))
rightSub = TreeNode(15, TreeNode(13, None, None), TreeNode(17, None, None))
root = TreeNode(10, leftSub, rightSub)

'''
          10
         /  \
        5    15 
       / \   / \
      3   9 13  17
'''
testKthSmallest(soln, root, 1, 3)
testKthSmallest(soln, root, 2, 5)
testKthSmallest(soln, root, 3, 9)
testKthSmallest(soln, root, 4, 10)
testKthSmallest(soln, root, 5, 13)
testKthSmallest(soln, root, 6, 15)
testKthSmallest(soln, root, 7, 17)

