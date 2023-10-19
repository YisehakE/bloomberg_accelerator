
'''
# GENERAL NOTES
## It took me the 2-3 minutes to think and plan out strategy
  - First solution was the brute force approach: check all pairs
  - We want to traverse the linked nodes 

## It took me the rest of the time to code, BUT I found 3 solutions
  - No extra time was needed necessarily 

## I was able to walkthrough as I devised solutions 1 through 3

## Took 15 mins extra to figure out errors with solutions 2 & 3

###### TOTAL TIME: 30 min (+5 for this reflection) = 35 mins
---------------------------------------------------------------
# REFLECTIONS
  What went well:
    - I asked 2 assumptions and/or clarifying questions
      - Asked about modifying (prompt already answered)
      - 
    - I was able to devise a 3 solutions within 30 mins
    - I was able to grasp what needed to be done fast
    - I was able to visualize the tasks on the IPad clearly
    - I was able to continue even though I had a working solution
    - I waited to hit RUN & SUBMIT until the end


  What went wrong:
    - I didn't explained clearly as I transitioned to solutions 2 & 3 
      - Only how we want better than brute, not by really explaining HOW they're better
    - I ran into python errors with solutions 2 & 3
    - I didn't get a chance, besides for solutions 1, to explain the time and space complexities
      - Mentioned briefly about as the less time solutions took, the more space we're taking up
      - I didn't, however, explain the tradeoffs AND possible reasons why we'd want one over the other

'''
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

'''First solution I came up with.'''
def merging_linked_list_1(linkedListOne, linkedListTwo):
  if linkedListOne == None or linkedListTwo == None: return None

  temp_1 = linkedListOne
  temp_2 = linkedListTwo
  
  curr_node_1 = linkedListOne
  curr_node_2 = linkedListTwo
  
  while curr_node_1 != None:
      while curr_node_2 != None:
          if curr_node_1.value == curr_node_2.value:
              return curr_node_1;
          curr_node_2 = curr_node_2.next
      curr_node_2 = temp_2
      curr_node_1 = curr_node_1.next
      
  return None

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

''' Second solution I came up with.'''
def merging_linked_list_2(linkedListOne, linkedListTwo):
 # Self loop means intersection
  val_dict = {}

  curr_node_1 = linkedListOne
  while curr_node_1 != None:
      val_dict[curr_node_1.value] = True
      curr_node_1 = curr_node_1.next

  curr_node_2 = linkedListTwo
  while curr_node_2 != None:
      if val_dict.get(curr_node_2.value) != None:
          return curr_node_2
      curr_node_2 = curr_node_2.next

  return None




def merging_linked_list_3(linkedListOne, linkedListTwo):
  if linkedListOne == None or linkedListTwo == None: return None

  l1_dict = {}
  l2_dict = {}
  curr_node_1 = linkedListOne
  curr_node_2 = linkedListTwo
  
  while curr_node_1 != None and curr_node_2 != None:
      if curr_node_1.value == curr_node_2.value: 
          return curr_node_1 #CHANGED FROM VALUE TO NODE
      elif l2_dict.get(curr_node_1.value) != None:
          return curr_node_1 #CHANGED FROM VALUE TO NODE
      elif l1_dict.get(curr_node_2.value) != None:
          return curr_node_2
      else: 
          l1_dict[curr_node_1] = True
          l2_dict[curr_node_2] = True
          curr_node_1 = curr_node_1.next
          curr_node_2 = curr_node_2.next

  if curr_node_1 == None:
      while curr_node_2 != None:
          if l1_dict.get(curr_node_2.value) != None: return curr_node_2
          l2_dict[curr_node_2] = True
          curr_node_2 = curr_node_2.next
  
  if curr_node_2 == None:
      while curr_node_1 != None:
          if l2_dict.get(curr_node_1.value) != None: return curr_node_1
          l1_dict[curr_node_1] = True
          curr_node_1 = curr_node_1.next
          
  return None

