def quickSort(arr,low,high):
    if low<high:
        pivotIndex = partition(arr,low,high)
        quickSort(arr,low,pivotIndex-1)
        quickSort(arr,pivotIndex+1,high)

def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
    
def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<pivot:
            i += 1
            swap(arr,i,j)
    swap(arr,i+1,high)
    return i+1

# =========
# MAIN CODE 
# =========

def foo(arr1, arr2):
    quickSort(arr1,0,len(arr1)-1)
    quickSort(arr2,0,len(arr2)-1)
    
    total = 0
    
    for i in range(len(arr1)):
        total += abs(arr1[i] - arr2[i])
          
    print(f"Total Difference is {total}\n")
    
def bar(arr1, arr2):
    total = 0
    
    for i in range(len(arr1)):
        total += round((arr2[len(arr2) - 1 - i] + arr1[i]) / 2)
          
    total /= len(arr2)
    print(f"Total Difference is {round(total)} \n")
    
# =========
# PART ONE
# =========

left = []
right = []

with open('10.txt', 'r') as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) == 2:
            left.append(int(parts[0]))
            right.append(int(parts[1]))

l1 = [3, 4, 2, 1, 3, 3]
r1 = [4, 3, 5, 3, 9, 3]

print("----PART ONE ----")
print("Test case: ")
foo(l1,r1)

print("Answer:")
foo(left, right)

# =========
# PART TWO
# =========

print("----PART TWO ----")
print("Test case:")
bar(l1, r1)

print("Answer: ")
bar(left, right)