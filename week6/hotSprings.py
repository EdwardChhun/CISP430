# (.) Operational
# (#) Damaged
# (?) Unknown

# Part One
# --------
def ifSpringsAndCountsAgree(row) -> bool:
    """Function that takes in a row indicating a row of "springs" and 
    the its count such that "." means operational and "#" means damaged
  
    Ex: #.#.### 1,1,3

    Args:
        row (str): takes in a row of springs and counts

    Returns:
        bool: returns (true) if the springs and counts agree, (false) if they don't
    """
    
    # Split the row of springs and count into 2 separate strings
    damaged, count = row.split(" ", 1)
    # Keeping current counts of the damaged springs
    # to later verify if matches the input
    currentDamaged = 0
    currentCount = []
    
    for i in damaged:
        if i == "#": 
            currentDamaged += 1
        else: 
            if currentDamaged:
                currentCount.append(currentDamaged)
            currentDamaged = 0 
    
    if currentDamaged:
        currentCount.append(currentDamaged)

    # If the current count is equal to the original count
    return ",".join(map(str,currentCount)) == count
 
 
# Part Two
# --------
def count_arrangements(row: str) -> int:
    """
    Function that takes a row indicating a sequence of "springs" and the expected counts,
    then counts valid arrangements considering unknown springs.
    
    Args:
        row (str): A string containing the spring sequence and the expected counts.
    
    Returns:
        int: The number of valid arrangements.
    """
    springs, counts_str = row.split(" ", 1)
    
    def count_valid_arrangements(index: int, current: str) -> int:
        # Base case:
        # If we reach the end of the string and process all of the springs,
        # exit and traverse back up the recursive stack
        if index == len(springs):
            return 1 if ifSpringsAndCountsAgree(f"{current} {counts_str}") else 0
        
        # Recursive case:
        # If the current index of the spring is unknown, we create two different branches to find valid arrangements
        if springs[index] == '?':
            return count_valid_arrangements(index + 1, current + '#') + count_valid_arrangements(index + 1, current + '.')
        else:
            return count_valid_arrangements(index + 1, current + springs[index])
    
    return count_valid_arrangements(0, "")

if __name__ == "__main__":
    
    sum1 = 0
    sum2 = 0
    sum3 = 0 
    sum4 = 0
    
    myListAllTrue = [
        "#.#.### 1,1,3",
        ".#...#....###. 1,1,3",
        ".#.###.#.###### 1,3,1,6",
        "####.#...#... 4,1,1",
        "#....######..#####. 1,6,5",
        ".###.##....# 3,2,1"
    ]
    
    myListAllFalse = [
        "#.##.## 1,1,3",
        ".#...#.#..###. 1,1,3",
        ".#.##..#.###### 1,3,1,6",
        "###..#...#... 4,1,1",
        "#....######..####.. 1,6,5",
        ".##..##....# 3,2,1" 
    ]
    
    unknownCases = [
        "..##.##########.##.# 2,10,2",
        "###############..#. 15,1",
        "#####...#....#... 5,1,1",
        "#####.##.##.###.##.# 5, 2, 2, 3, 1, 1"
    ]
    
    part2Cases = [
        "??????????#????????? 2,10,2",
        "??????#????????????? 15,1",
        "????????????????? 5,1,1",
        "????????????????#??? 5,2,2,3,1,1"
    ]
    
    for i in myListAllTrue:
        if ifSpringsAndCountsAgree(i):
            sum1 += 1
    
    for i in myListAllFalse:
        if ifSpringsAndCountsAgree(i):
            sum2 += 1
            
    for i in unknownCases:
        if ifSpringsAndCountsAgree(i):
            sum3 += 1
            
    for i in part2Cases:
        sum4 += count_arrangements(i)
            
    print(f"Test case 1: {sum1}")
    print(f"Test case 2: {sum2}")
    print(f"Answer part 1: {sum3}")
    print(f"Answer part 2: {sum4}")
    
    