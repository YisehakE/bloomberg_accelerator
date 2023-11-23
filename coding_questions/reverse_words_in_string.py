
'''
Question(s)/Assumptions

Q: Can we assume that there can be white spaces at the beginning or end of string?
A: Yes you can assume that

Q: Can we assume that concatenating a string w/ += is inefficient? (i.e O(n^2))?
A: Yes you can assume that, consider utilizing arrays and .join() method

'''

from collections import deque

'''
:: SOLUTION 1 :: 
# Possible brute force solution
  - Passes all test cases!
  - Need to determine the space time complexity
    - May or may not be optimal
  - Hypothesized complexities as follows:
    - Time: O(N^2)
    - Space: O(N)

'''

def collect_from_que(que, rev_str, rev_i):
    while len(que) != 0:
        rev_str[rev_i] = que.pop()
        rev_i += 1
    return (que, rev_str, rev_i)

def reverseWordsInString_1(string):
    que = deque()
    rev_str, rev_i = [""]*len(string), 0 

    for i in range(len(string) - 1, -1, -1):
    
        if string[i] == " ":
            if len(que) != 0:
                que, rev_str, rev_i = collect_from_que(que, rev_str, rev_i)
                rev_str[rev_i] = " "

            rev_str[rev_i] = " "
            rev_i += 1
        else:
            que.append(string[i])

    if len(que) != 0: 
        que, rev_str, rev_i = collect_from_que(que, rev_str, rev_i)
             
    rev_str = "".join(rev_str)
    
    return rev_str



'''
:: SOLUTION 2:: 
# Attempt at optimizing solution 1
  - Haven't completed.
  - Attempt to solution of following complexities:
    - Time: O(N)
    - Space: O(N)

'''


def reverseWordsInString_2(string):
    que = deque()
    rev_str, rev_i = [""]*len(string), 0 

    
    for i in range(len(string) - 1, -1, -1):
       
        que.appendleft(string[i])

    rev_str = ""
    space_cnt = 0
    while len(que) != 0:

        if space_cnt != 0:
            rev_str[rev_i] = que.popleft()
        
        rev_i += 1
             
    rev_str = "".join(rev_str)
    return rev_str


'''
:: SOLUTION 3:: 
# Optimized 
  - Passes all test cases!
  - Developed with support from video explanation.
  - Proven complexities as follows:
    - Time: O(N)
    - Space: O(N)

'''

def reverseWordsInString_3(string):

    if len(string) < 2:
        return string 
    que = deque()
    word_arr = []

    word = ""
    start = 0
    for i in range(0, len(string)):
        if string[i] != " " and string[start] == " ":
            word_arr.append(" ")
        if string[i] == " ":
            word_arr.append(string[start:i])
            
        start = i

    if string[-1] != " ":
        word_arr.append(string[start:len(string)])
    else:
        word_arr.append(" ") 

    rev_arr = []
    for i in range(len(word_arr) - 1, -1, -1):
        rev_arr.append(word_arr[i])
            
    return "".join(rev_arr)


    '''
    TEST CASES: 1st Solution
    '''

tst_str_1 = "Algoexpert is the best!"
print(reverseWordsInString_3(tst_str_1))









'''
# GENERAL NOTES
* I gave myself 20 minutes to do this problem
## It took me the 5-10 minutes to think and plan out strategy
  - First solution was the brute force approach: check all pairs

## It took me the rest of the time to code: finished one solution and attempted another
  - No extra time was needed necessarily 

## I was NOT able to walkthrough an example with solution 1

## I was NOT able to deduce what the time complexity was 

## Took 20 minutes learning the given video solution and implementing

###### TOTAL TIME: 40 min (+5 for this reflection) = 45 minutes
---------------------------------------------------------------
# REFLECTIONS
  What went well:
    - I was able to spot the difficult of this problem versus just reversing a string
    - I was able to come up with a hacky solution at first
    - Stacks and queues immmediately popped to my mind as data structures to use
    - I was able to compartmentalize different functionalities in my main function
      to helpers easily


  What went wrong:
    - I was not sure on what the time complexity was for my solution
      - Even though I was aiming at linear, I wasn't sure
    - I may have been using an unnecessary structure even though it's still O(N) space complex
    - UPDATE
'''