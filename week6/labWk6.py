# Part 1

# Although it is not explicitly stated, what is the base case for writeSub()? 	
# Answer: The base case would be when the current node pointed at is a null node. Therefore the recursive case would terminate and print nothing

# What is the base case for insertEndSub()? 	
# Answer: If the next node exist, therefore it will continue moving towards the next node to find a node that doesn't exist as a terminal point.

# If you wanted to print the list backwards, how would you modify writeSub()? Why?
# Answer: Intuition is to do a reverse slice and introduce an extra list in python so i can do mylist[::-1] and just print that, which would be backwards.
#         I would need to initialize a mylist = [] variable outside writeSub and inside the if statement I would replace print(..) with mylist.append(node.data)

#         I would make it that it would print when traversing back the recursive stack, I would change the print statement with the recursive statement
#         such that it would find the end of the list and then print.

