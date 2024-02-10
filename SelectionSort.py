def SelectionSort(arr):
    n = len(arr)
    for i in range(0,n,1):
        
        smallest = i
        arr[smallest] = arr[i]
        
        for j in range(i,n,1):
            if(arr[j]<arr[smallest]):
                smallest = j
        
        temp = arr[i]
        arr[i] = arr[smallest]
        arr[smallest] = temp

    return arr

arr = [5,3,2,43,1,53,99,7]
print(SelectionSort(arr))

'''
Example: [5,3,2,43,1]

1st Pass: 
[->(5) , 3, 2] smallest = 5
[->(5) , (3) , 2] smallest = 3
[->5 , (3) , (2) , 43, 1] smallest = 2
[->5 , 3, (2) , (43) , 1] smallest = 2
[->5 , 3, (2) , 43, ->(1)] smallest = 1
[1,3,2,43,5]

2nd Pass: 
[1,->(3),2,43,5] smallest = 3
[1,->(3),(2),43,5] smallest = 2
[1,->3,(2),(43),5] smallest = 2
[1,->3,->(2),43,(5)] smallest = 2
[1,2,3,43,5]

3rd Pass:
[1,2,->(3),43,5] smallest = 3
[1,2,->(3),(43),5] smallest = 3
[1,2,->(3),43,(5)] smallest = 3
[1,2,3,43,5]

4th Pass:
[1,2,3,->(43),5] smallest = 43
[1,2,3,->(43),->(5)] smallest = 5
[1,2,3,5,43]

5th Pass:
[1,2,3,5,->(43)] smallest = 43
[1,2,3,5,43]

'''
