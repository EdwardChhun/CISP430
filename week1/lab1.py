arr = [1, 2, 3, 4, 5]
arr2 = []

arr2 += arr

for num in arr:
    print(num, end=' ')
    
arr.insert(4, 8)

print(arr)

arr.pop(2)
arr.pop(4)

print(arr)

arr += arr2

print(arr)

f = open("1_file.txt", "r")
for num in f:
    arr.append(int(num))
    
print()
print(f"final step: {arr}")
