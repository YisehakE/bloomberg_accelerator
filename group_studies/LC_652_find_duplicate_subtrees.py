# Problem link: https://leetcode.com/problems/find-duplicate-subtrees/



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
Breaking down problem

  Input is Binary tree
    - <= 2 children
    - Probably use recursion


  How to traverse from root
    - 

  How to build our recursive func
    Base case

    Recursive
      Traverse the tree

  How to spot a duplicate
    - The value of the children
    - The orientation of children


Easy base cases

  2


     2
    /
   1

    2
   / \ 
  1   1


'''
def findDuplicateSubtrees_1(root):
    """
    :type root: TreeNode
    :rtype: List[TreeNode]
    """

    duplicates = []
    trees_found = set()

    def traverse_tree(node, str_before):

        if node is None:
            return ""
        
        new_tree = 
        root_str = str(node.val)

        left_str = traverse_tree(node.left, root_str)
        right_str = traverse_tree(node.right)

        trees.found.add()

        # if left_str == "" and right_str:
        #     trees_found.add(root_str)
        #     if root_str in tree_found:
        #         duplicates.append(root_str)
        # elif left_str == "":
        #      root_str
        #      trees_found.add(root_str + right)
        # else:

        trees_found[]
        trees_found[node] = node_parent

    traverse_tree(root, "")
    
    pass

        
from collections import defaultdict 


'''
Solution 2: The correct and optimal function
Resources: Accelerator group, Neetcode.io video

Neetcode link: https://www.youtube.com/watch?v=kn0Z5_qPPzY&ab_channel=NeetCodeIO
'''
def findDuplicateSubtrees_2(root):
    

    duplicate_trees = []
    trees_found = defaultdict(list) # Value could either be list OR int

    def preorder_traverse(node):
        if not node:  return "N"

        # Traverse in preorder fashion
        left_str = preorder_traverse(node.left)
        right_str = preorder_traverse(node.right)

        # Build in preorderfashion
        tree_str = ",".join([str(node.val), str(left_str), str(right_str)])

        # ALTERNATE (Trees_Found -> Map<str, int> -> if trees_found[tree_str] == 1: {...})
        if len(trees_found[tree_str]) == 1: # Check if tree been seen exactly once before

            duplicate_trees.append(node) # We want to store the head of any duplicate trees
        
        # ALTERNATE (Trees_Found -> Map<str, int> -> trees_found[tree_str] += 1)
        trees_found[tree_str].append(node) # Add new instance of subtree root whether dup. or not

        return tree_str # Return the str that this subtree makes up

    preorder_traverse(root)
    return duplicate_trees
            
            

    
  