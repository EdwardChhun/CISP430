class Stack:
    
    def __init__(self):
        self.top = -1
        self.items= []
        
    def is_empty(self):
        return (self.top == -1);

    def push(self,newItem):
        self.top+=1
        self.items.append(newItem);

    def pop(self):
        if (self.is_empty()):
            return None
        else:
            self.top-=1
            return self.items.pop()

    def peek(self):
        if (self.is_empty()):
            return None
        else:
            return self.items[self.top]

    def size(self):
        return len(self.items)
    
    # Trying the max method with O(n) solution
    def max_method(self) -> int:
        """
        Input: Stack
        Output: Integer
        """
        if self.is_empty():
            return None
        return max(self.items) # O(n) where it iterates through the stack. 
    
# --- PART ONE ---
# ----------------

# There is no delimeter, the only thing that separates is if one pair is made
# if one chunk stops, the next chunk (if any) can immediately start

# Do i have an unclosed chunk saved into a stack, so that where I can pop and push the items to check the current
# index of chunk to be found a pair or not

# IMPORTANT - I am using the Stack ADT from Lab
# ---------------------------------------------

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

def checkForCorruption(string) -> str:          
    openChunk = Stack()

    # If there is a closed chunk inside the list, then the chunk behind it is the one who's missing a closed one 
    # supposedly that's missing a pair, so it's expected should be considered (makes sense to me, sorry)

    for i in string:
        # Comparing the top most of stack with the current chunk (being iterated through the string)
        if not openChunk.is_empty() and foundClosedChunk(openChunk.peek(), i):
                openChunk.pop()
        # If not a paired chunk, then add the unclosed chunk to the stack
        else:
            openChunk.push(i)
        
        # Uncomment this to see how the stack builds up each iteration
        # print(myList)
        
    return findExpected(openChunk.items)

def checkForCorruption_list(string) -> list | None:          
    openChunk = Stack()

    # If there is a closed chunk inside the list, then the chunk behind it is the one who's missing a closed one 
    # supposedly that's missing a pair, so it's expected should be considered (makes sense to me, sorry)
    for i in string:
        if i in "([{<":
            openChunk.push(i)
        elif not openChunk.is_empty() and foundClosedChunk(openChunk.peek(), i):
            openChunk.pop()
        else:
            return None  # Corrupted line, ignore it in Part Two

    return openChunk.items if not openChunk.is_empty() else None


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

print("Part 1")
print(totalSyntaxScore) #294195

print()

# --- PART TWO ---
# ----------------

# Throw away the corrupted and jjust have the incomplete ones 
# The checkForCorruption(str) still works and outputs the unclosed chunks
# create a function that reverses its order and add the scores
# ): 1 point.
# ]: 2 points.
# }: 3 points.
# >: 4 points.
# Reverse list to add up the missing chars
def foo(chunk) -> int:
    chunk = chunk[::-1]
    total_missing_score = 0
    
    for i in chunk:
        total_missing_score *= 2
        if i == "(": total_missing_score +=  1
        if i == "[": total_missing_score +=  2
        if i == "{": total_missing_score +=  3
        if i == "<": total_missing_score +=  4
    
    return total_missing_score
    
print("Part 2")
incomplete_scores = []

with open("3.txt", "r") as f:
    for line in f:
        chunk = checkForCorruption_list(line.strip())
        if chunk is not None: 
            incomplete_scores.append(foo(chunk))
            
print(max(incomplete_scores)) #112689

# Printing Test Cases

test1 = [
    "{([(<{}[<>[]}>{[]{[(<()>",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
]

test2 = [
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "(((({<>}<{<{<>}{[]{[]{}",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "<{([{{}}[<[[[<>{}]]]>[]]"
    
]

print()

test1_total = 0
for i in test1:
    test1_found = checkForCorruption(i.strip())
    test1_total += illegalCharValue(test1_found)

print(f"Test Case Part 1: {test1_total}")

incomplete_chunk_total = []
for i in test2:
    test2_chunk = checkForCorruption_list(i.strip())
    if test2_chunk is not None: 
            incomplete_chunk_total.append(foo(test2_chunk))
            
print(f"Test Case Part 2: {max(incomplete_chunk_total)}")
	
