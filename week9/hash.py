def hashFunc(word):
    current = 0
    for i in word:
        current += ord(i)
        current *= 17
        current %= 256
    return current
        

def createArr(file):
    arr = []
    curr = ""
    for i in file:
        if i == ",":
            arr.append(curr)
            curr = ""
        else:
            curr += i
     
    arr.append(curr) # So the last chunk gets appended, because it doesn't end with a comma    
       
    return arr

def hashmap(arr):
    # 1. hashFunc the letters before the =/- sign
    # 2. If = => add, if - => remove
    # 3. the number is its focal length
    # 4. Use the focusing power algo to determine answer
    
    box = {}
    
    for chunk in arr:
        if "=" in chunk:
            label, focal_length = chunk.split("=")
            focal_length = int(focal_length)
            index = hashFunc(label)
            
            box.setdefault(index, {})
            
            box[index][label] = focal_length
                
        elif "-" in chunk:
            label = chunk[:-1]
            index = hashFunc(label)
            
            # Delete the lens if found
            if index in box and label in box[index]:
                del box[index][label]
        
    return box
        
def cal_focus_power(box):
    total = 0
    
    for boxIndex, lens in box.items():
        for slotIndex, (label, focal_length) in enumerate(lens.items()):
            total += (boxIndex + 1) * (slotIndex + 1) * focal_length
            
    return total 

if __name__ == "__main__":
    # PART ONE
    testStr = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
    testArr = createArr(testStr)  
    
    with open("9.txt", "r") as f:
        arr = createArr(f.read().strip("\n"))
            
    total = 0
    for i in testArr:
        total += hashFunc(i)
        
    totalPartOne = 0 
    for i in arr:
        totalPartOne += hashFunc(i)
    
    
    print(f"part one test case: {total}")
    print(f"part one: {totalPartOne}")
    
    #PART TWO
    # 1. hashFunc the letters before the =/- sign
    # 2. If = => add, if - => remove
    # 3. the number is its focal length
    # 4. Use the focusing power algo to determine answer
    
    
    boxesTest = hashmap(testArr)
    totalPartTwoTest = cal_focus_power(boxesTest)
    
    boxes = hashmap(arr)
    totalPartTwo = cal_focus_power(boxes)
    
    print(f"part two test case: {totalPartTwoTest}")
    print(f"part two: {totalPartTwo}")
    
    
    
    
    
      
