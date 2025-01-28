# testing cases
arr = [1726,
        979,
        366,
        299,
        680,
        1456]

# using a complment
def solver2(arr):
    for num in arr:
        x = 2025 - num
        if x in arr:
            print(x * num)
            print(x, num)
            break
        
# three sum now
def solver(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            x = arr[i] + arr[j]
            if x < 2025:
                for k in range(j + 1, len(arr)):
                    if x + arr[k] == 2025:
                        print(arr[i] * arr[j] * arr[k])
                        print(arr[i], arr[j], arr[k])
                    
# I might be the goat

f = open("1.txt", "r")

arr1 = []

for num in f:
    arr1.append(int(num))

print()
solver2(arr1)
print()
solver(arr1)

        
    