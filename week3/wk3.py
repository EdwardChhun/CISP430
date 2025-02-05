# --- PART ONE ---
# ----------------

# There is no delimeter, the only thing that separates is if one pair is made
# if one chunk stops, the next chunk (if any) can immediately start

# Do i have an unclosed chunk saved into a stack, so that where I can pop and push the items to check the current
# index of chunk to be found a pair or not

from lab import Stack

# Init a stack for the open chunk 
# For each open stack, push into this and
# keep track of the top most with peek().

# After each chunk iteration, 
# check if the next chunk is the closed version of the topmost in the stack

# If openChunk.size() != 0, means that it is a corrupted chunk
# Using an extra list to keep track of the items can help with visualization, 
# but for space complexity, we can just pertain to using the openChunk to shoot out our corrupted chunk (probably scratch this for simplicity)

# Function to define a closed chunk
def foundClosedChunk(opened, closed) -> bool:
    return (opened == "(" and closed == ")") or \
           (opened == "[" and closed == "]") or \
           (opened == "{" and closed == "}") or \
           (opened == "<" and closed == ">")

# Function to find expected
def findExpected(myList) :
    for i in range(len(myList)):
        # If a mismatched closed was found
        if myList[i] == ")" or myList[i] == "}" or myList[i] == "]" or myList[i] == ">":
            
            return myList[i]
        

# Function to return the value of illegal character:
def illegalCharValue(i):
    if i == ")": return 3
    if i == "]": return 57
    if i == "}": return 1197
    if i == ">": return 25137 
    return 0

def checkForCorruption(string):          
    openChunk = Stack()

    # If there is a closed chunk inside the list, then the chunk behind it is the one who's missing a closed one 
    # supposedly that's missing a pair, so it's expected should be considered (makes sense to me, sorry)
    testChunk = string
    myList = []

    for i in testChunk:
        # Comparing the top most of stack with the current chunk (being iterated through the string)
        if not openChunk.is_empty() and foundClosedChunk(openChunk.peek(), i):
                openChunk.pop()
                myList.pop()
        # If not a paired chunk, then add the unclosed chunk to the stack
        else:
            openChunk.push(i)
            myList.append(i)
        
        # Uncomment this to see how the stack builds up each iteration
        # print(test)
        
    return findExpected(myList)

# If the length is odd, then return that it is an incomplete string right away
# ): 3 points.
# ]: 57 points.
# }: 1197 points.
# >: 25137 points
totalSyntaxScore = 0

with open("3.txt", "r") as f:
    for line in f:
        found = checkForCorruption(line.strip()) 
        totalSyntaxScore += illegalCharValue(found)
    
print(totalSyntaxScore) #294195


# --- PART TWO ---
# ----------------