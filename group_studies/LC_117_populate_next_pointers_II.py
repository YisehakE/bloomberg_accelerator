
'''
U - Understand what interview 
M - Match the problem to algorithm and/or data structure
P - Plan out what you want to do (i.e pseudocode, helper functions, skeleton code)
I - Implement the code!
R - Run specific examples/test cases
E - Explain space and time complexities
'''


''' SIMPLE CASES
Just the root
        1 -> null
---------------------------------
Just left sub tree
        1 -> null
      / 
    2 -> null
---------------------------------
Just right sub tree
       1 -> null
        \ 
         2 -> null
---------------------------------
Perfect tree (depth 2)
        1 -> null
       /  \ 
      2 ->  3 -> null
---------------------------------
Example 1 tree (depth 3)
          1 -> N
        /  \ 
       2 ->  3 -> N
      / \     \ 
    4 -> 5 ->N 7 -> N
'''


from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
        
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        self.traverse_tree(root)
    
    def traverse_tree(node):
        que = deque()
        que.append(node)

        que_list = list(que)
        curr = que[0]

        for i in range(len(que_list)):
            curr.next = que[i + 1]
            curr = curr.next

        while len(que) != 0:
            curr_node = que.popleft()

            left_child = curr_node.left 
            right_child = curr_node.right
            
            if left_child is not None:
                # if right_child is not None:
                #     left_child.next = right_child
                # else:
                #     left_child.next = None
                que.append(left_child)
            
       
            if right_child is not None: # TODO: consider case where we're at depth > 1
                # right_child.next = None

                que.append(right_child)
