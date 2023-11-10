

'''
    # Move if no boundaries are hit: #

 1  IF Beginning OR just zigzagged up:
      Go right # Uphold boundaries here
      Ziz zag downwards

 2  ELIF just zigzagged down:
      Go down # Uphold boundaries here
      Zig zag upward
      

    # Moves when boundaries are hit:# 
    
    For 1   IF you can't go right, 
                go down first 
            Proceed zig zag downwards
    
    For 2   IF you can't go down:
                go right first
            Proceed zig zag upwards 
    
'''

def is_cell_within_boundaries(y, x, row_sz, col_sz):
    is_within_row = 0 <= y < row_sz
    is_within_col = 0 <= x < col_sz

    return is_within_row and is_within_col

def zigzagTraverse(array):
    last_move = "zig_down"
    row_sz = len(array)
    col_sz = len(array[0])
    cell_x, cell_y = 0, 0
    
    output = []
    output.append(array[cell_y][cell_x])

    while cell_x < len(array[0]) and cell_y < len(array):
        if (cell_x == 0 and cell_y == 0) or (last_move == "zig_down"):
            if is_cell_within_boundaries(cell_y + 1, cell_x, row_sz, col_sz):
                cell_y += 1
            elif is_cell_within_boundaries(cell_y, cell_x + 1, row_sz, col_sz):
                  cell_x += 1
            else:
                break
                
            output.append(array[cell_y][cell_x])
            while is_cell_within_boundaries(cell_y - 1, cell_x + 1, row_sz, col_sz):
                cell_x += 1
                cell_y -= 1
                output.append(array[cell_y][cell_x])

            last_move = "zig_up"
        elif last_move == "zig_up":
            
            if is_cell_within_boundaries(cell_y, cell_x + 1, row_sz, col_sz):
                cell_x += 1
            elif is_cell_within_boundaries(cell_y + 1, cell_x, row_sz, col_sz):
                cell_y += 1
            else:
                break
            output.append(array[cell_y][cell_x])

            while is_cell_within_boundaries(cell_y + 1, cell_x - 1, row_sz, col_sz):
                cell_x -= 1
                cell_y += 1
                output.append(array[cell_y][cell_x])
            last_move = "zig_down"
      
        
    if output[-1] != array[len(array) - 1][len(array[0]) - 1]:
        output.append(array[-1][-1])

    return output




'''
# GENERAL NOTES
* I gave myself 30 minutes to do this problem
  - I went over about 40 minutes

## I took 10 minutes to think about problem and write up pseudo

## It took me the rest of the time to code and finished one solution
  - No extra time was needed necessarily 

## I was able to walkthrough an example when coming up with the pseduocode

## I did NOT have time to deduce what the time complexity was 

## I was able to impplement solution without hints or video help

###### TOTAL TIME: 40 min (+5 for this reflection) = 45 minutes
---------------------------------------------------------------
# REFLECTIONS
  What went well:
    - I was able to suprisingly break down this problem easily
      - I did this by just following the zig zag pattern
    - I was able to come up with pseudocodd
    - I recognized that I wasn't speaking for the first 15 minutes all too much
      - I started correcting it a little after that
    - I was able not to get bogged down in details at first
      - I have a problem with this, and it runs down the clock + makes me confused
    - I was able to spot out logical errors on my own
      - For example, remembering what down and up is in a 2D array
      - Fixing the incremenents for zig zagging down and up respectively

  What went wrong:
    - I was not talking as much in the first 12 minutes
      - It's kind of hard to speak when doing it by myself
      - These are the crucial moments to speak
    - I could've broke down some of the functionality into other functions
    - I didn't give myself time to explain the complexity
  
  What did I learn
    - That this hard problem wasn't all too bad
'''