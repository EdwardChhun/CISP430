from stackADT import Stack
from queueADT import Queue

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

with open("4.txt", "r") as f:
    for line in f:
        expression = line.strip()
        total_part1 += evaluate_expression_part1(expression)
        total_part2 += evaluate_expression_part2(expression)

print("Part 1 Total:", total_part1)
print("Part 2 Total:", total_part2)
