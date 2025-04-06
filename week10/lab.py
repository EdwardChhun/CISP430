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

def main():
    array=[2, 0 ,5, 6, 1, 6, 2]
    quickSort(array,0,len(array)-1)
    print(array)
    
