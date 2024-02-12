def MergeSort(arr):
    n = len(arr)

    # Divide the array
    middle = int(n/2)
    left = arr[:middle]
    right = arr[middle:]

    if(n == 1):
        return arr
    
    # merge function for comparing and returning
    return merge(MergeSort(left), MergeSort(right))

def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    while(left_index < len(left) and right_index < len(right)): #while indexes dont go out of bound
        if(left[left_index] < right[right_index]):
            result.append(left[left_index]) # Push Left
            left_index += 1
        else:
            result.append(right[right_index]) # Push Right
            right_index += 1

     # If any number is remaining in the left or/and right array after the index pointer, those elements will be added to the result
    result = result+left[left_index:]+right[right_index:]
    return result

arr = [6,4,8,2,48,65,21,86]
print(MergeSort(arr))
