
## Date 
- October 19th, 2023


## Engineer tips
- cutting down input by half
- UPDATE

## My question
- When do we know what kind of traversal for BST that we are to use? (i.e pre, in, post order)"

- Answer:
  - The traversal doesn't really matter, as they accomplished


## Other questions
- Question: How do we understand how deep or what depth we should traverse a BST?
- Answer: Usually need to know grandparent, parent, and children hierarchy at most.


## Questions today
- Validate BST
- Reconstruct BST


## Validate BST
- We came up with a solid solution, but we were missing crucial point:
  - The values must uphold BST property for PREVIOUS parent values
- We came up with using minimum and maximum values passed in as parameters
- ---------------STILL STUCK ON HOW TO UTILIZE MIN AND MAX VALUES

## Reconstruct BST
- Identified the root node, the start of the leftsub tree, and right subtree elements
- Utilized a recursive helper function to 
  1) Section off left sub
  2) Section off right sub
  3) Build the left and right nodes respectively
- 

## Homework assigned
- 