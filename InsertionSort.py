"""Simpler implementation using spice function

def InsertionSort(arr):
    n = len(arr)
    for i in range(n):
        if(arr[i]<arr[0]):
            #Move number to the first position
            arr[1:]
        else:
            #find where number should go
            for j in range(1,i,1):
                if(arr[i] > arr[j-1] and arr[i] < arr[j]):
                    arr... something... something
"""
                    
def InsertionSort(arr):
    
    for small in range(0,len(arr),1):     
        if(arr[small]<arr[small-1]):
            j = small-1

            while(arr[small]<arr[j]):
                j-=1
                
            temp = arr[small]
            for k in range(small, j,-1):
                  arr[k] = arr[k-1]
            
            arr[j+1] = temp 
            
            print("Array:",arr)

    return arr



arr = [5,8,6,2,4,1]
print(InsertionSort(arr))

'''
Steps:
1. Check if number less than prev(small-1) number 
2. go back finding the index of the value which is still greater(j) than the selected value (while loop)
3. Store the selected value
4. Shift elements from the index lesser than the selected number and shift it to the index of the slected number and keep doing until the position for the selected number is opened.
5. Place the selected number that is stored.
'''