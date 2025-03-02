class Stack:
    
    def __init__(self):
        self.top = -1
        self.items = []
        
    def is_empty(self):
        return self.top == -1

    def push(self, newItem):
        self.top += 1
        self.items.append(newItem)

    def pop(self):
        if self.is_empty():
            return None
        else:
            self.top -= 1
            return self.items.pop()

    def peek(self):
        if self.is_empty():
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
        return max(self.items)  # O(n) where it iterates through the stack. 

class Queue:
    # Queue implementation as a list
    def __init__(self):
        self._items = []
    
    def is_empty(self):
        # Check if the queue is empty
        return len(self._items) == 0
    
    def enqueue(self, item):
        # Add an item to the queue
        self._items.insert(0, item)
    
    def dequeue(self):
        # Remove an item from the queue
        return self._items.pop()
    
    def size(self):
        # Get the number of items in the queue
        return len(self._items)


# --- PART ONE ---
# ----------------

# This part evaluates the expression strictly left-to-right, ignoring operator precedence.
# We tokenize the input and use a queue to process the expression in order.

# Function to evaluate an expression left-to-right (no precedence)
def evaluate_expression_part1(expression):
    q = Queue()
    num = ""
    
    # Tokenizing the expression
    for char in expression:
        if char.isdigit():
            num += char
        else:
            if num:
                q.enqueue(int(num))
                num = ""
            if char in "+*()":
                q.enqueue(char)
    
    if num:
        q.enqueue(int(num))
    
    # Using stack and storing items in tuples,
    # keeping track of priority
    s = Stack()
    result = 0
    op = None
    
    while not q.is_empty():
        token = q.dequeue()
        
        if isinstance(token, int):
            if op is None:
                result = token
            elif op == "+":
                result += token
            elif op == "*":
                result *= token
            op = None
        
        elif token in "+*":
            op = token
        
        elif token == "(":
            s.push((result, op))
            result, op = 0, None
        
        elif token == ")":
            if not s.is_empty():
                prev_result, prev_op = s.pop()
                if prev_op == "+":
                    result = prev_result + result
                elif prev_op == "*":
                    result = prev_result * result
    
    return result


# --- PART TWO ---
# ----------------

# This part evaluates expressions where addition has precedence over multiplication.
# Addition is processed first, and multiplication is applied afterward.

# Function to process an expression, ensuring addition is done first
def process_queue(q):
    values = []
    op = None
    
    while not q.is_empty():
        token = q.dequeue()
        
        if isinstance(token, int):
            if op == "+":
                values[-1] += token
            else:
                values.append(token)
            op = None
        
        elif token == "+":
            op = "+"
        
        elif token == "*":
            op = "*"
    
    result = 1
    for val in values:
        result *= val
    
    return result

# Function to evaluate an expression where addition has precedence over multiplication
def evaluate_expression_part2(expression):
    q = Queue()
    num = ""
    
    # Tokenizing the expression
    for char in expression:
        if char.isdigit():
            num += char
        else:
            if num:
                q.enqueue(int(num))
                num = ""
            if char in "+*()":
                q.enqueue(char)
    
    if num:
        q.enqueue(int(num))
    
    s = Stack()
    result_queue = Queue()
    
    while not q.is_empty():
        token = q.dequeue()
        
        if token == "(":
            s.push(result_queue)
            result_queue = Queue()
        
        elif token == ")":
            sub_result = process_queue(result_queue)
            result_queue = s.pop()
            result_queue.enqueue(sub_result)
        
        else:
            result_queue.enqueue(token)
    
    return process_queue(result_queue)

# Reading input file and evaluating expressions
total_part1 = 0
total_part2 = 0
total_example1 = 0
total_example2 = 0
part1_example = [
    "1 + 2 * 3 + 4 * 5 + 6",
    "1 + (2 * 3) + (4 * (5 + 6))",
    "2 * 3 + (4 * 5)", 
    "5 + (8 * 3 + 9 + 3 * 4 * 3)", 
    "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 
    "(2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
]
part2_example = [
    "1 + 2 * 3 + 4 * 5 + 6",
    "1 + (2 * 3) + (4 * (5 + 6))", 
    "2 * 3 + (4 * 5)", 
    "5 + (8 * 3 + 9 + 3 * 4 * 3)", 
    "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 
    "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
]
with open("4.txt", "r") as f:
    for line in f:
        expression = line.strip()
        total_part1 += evaluate_expression_part1(expression)
        total_part2 += evaluate_expression_part2(expression)

# Examples

for x in part1_example:
    expression = x.strip()
    total_example1 += evaluate_expression_part1(expression)
    
for x in part2_example:
    expression = x.strip()
    total_example2 += evaluate_expression_part2(expression)    
    
print("Part 1 Example:", total_example1)
print("Part 1 Total:", total_part1)
print("Part 2 Example:", total_example2)
print("Part 2 Total:", total_part2)
