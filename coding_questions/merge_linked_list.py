'''
# GENERAL NOTES
## It took me more than 2-3 minutes to understand the prompt.
  - I didn't really know where I was going w/ my logic
  - 

## It took me the rest of the time to code
  - Had no time to discuss optimization or trade offs, mostly b/c I couldn't devise my own solution

###### TOTAL TIME: 30 mins (+15 min to understand video): 45-1hr
---------------------------------------------------------------
# REFLECTIONS
  What went well:
    - I was able to get the base idea dowm for comparison
      - Only issue is I was trying to place nodes after

  What went wrong:
    - I did not think to utiilize a previous pointer.
    - I was getting buried in a series of .next references

'''


''' First & only solution I came up with.'''
def merge_linked_lists_1(headOne, headTwo):
  first = headOne
  second = headTwo

  prevOne = headOne
  prevSecond = headTwo
  
  while first is not None and second is not None:

      if second.next == None:
          second.next = first
          return headTwo
      if first.value > second.next.value:
          prevSecond = second.next
          second = second.next.next
  
      elif first.value <= second.next.value:
          temp = second.next
          second.next = first
          second.next.next = temp

          prevSecond = second.next
          second = second.next.next
          first = first.next

  if second is None:
      prevSecond.next = first
      return headTwo

  return headTwo



''' Final solution that I replicated from AlgoExpert video. '''
def merge_linked_lists_2(headOne, headTwo):
    first = headOne
    second = headTwo

    prev = None
    while first is not None and second is not None:
        if second.value < first.value:
            if prev is not None:
                prev.next = second
                prev = second
                second = second.next
                prev.next = first
            else:
                prev = second
                second = second.next
                prev.next = first
        else:
            prev = first
            first = first.next

    if first is None:
        prev.next = second

    if headTwo.value < headOne.value:
        return headTwo
    
    return headOne
