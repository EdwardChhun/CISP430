# SLIDING WINDOW PROBLEM
# Read file
# Read each char and keep count of var "counter"
# make current chunk into set so check set(subStr) == 4, where subStr is the 4 chunk of letters
# if yes, return current count + 4
# if no, count + 1 and move the 4 slot window next

with open("2.txt", "r") as f:
    code = f.read()

for i in range(0, len(code) - 4 + 1):
    chunk = [code[i], code[i+1], code[i+2], code[i+3]]
    if len(set(chunk)) == 4 :
        print(f"First marker after character {i + 4} which is {''.join(chunk)}")
        break

# Part 2
for i in range(0, len(code) - 14 + 1):
    new_chunk = code[i:i+14]
    if len(set(new_chunk)) == 14 :
        print(f"First marker after character {i + 14} which is {''.join(new_chunk)}")
        break
    

