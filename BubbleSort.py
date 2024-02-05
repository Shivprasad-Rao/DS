def BubbleSort(arr):
    j = 0
    for i in range(0,len(arr),1):
        for j in range(1, len(arr),1):
            if arr[j-1] > arr[j]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
    
    return arr



arr = [32,51,89,74,31,6]
print("BubbleSort: ",BubbleSort(arr))

"""
    #Sets the highest number at the end of the array in each iteration - making it O(n^2)
1st Pass:
{32 51} 89 74 31 6
32 {51 89} 74 31 6
32 51 {89 74} 31 6
32 51 74 {89 31} 6
32 51 74 31 {89 6}
32 51 74 31 6 89

2nd Pass:
{32 51} 74 31 6 89
32 {51 74} 31 6 89
32 51 {74 31} 6 89
32 51 31 {74 6} 89
32 51 31 6 {74 89}
32 51 31 6 74 89

3rd Pass:
{32 51} 31 6 74 89
32 {51 31} 6 74 89
32 31 {51 6} 74 89
32 31 6 {51 74} 89
32 31 6 51 {74 89}
32 31 6 51 74 89

4th Pass:
{32 31} 6 51 74 89
31 {32 6} 51 74 89
31 6 {32 51} 74 89
31 6 32 {51 74} 89
31 6 32 51 {74 89}
31 6 32 51 74 89

5th Pass:
{31 6} 32 51 74 89
6 {31 32} 51 74 89
6 31 {32 51} 74 89
6 31 32 {51 74} 89
6 31 32 51 {74 89}
6 31 32 51 74 89

6th Pass:
{6 31} 32 51 74 89
6 {31 32} 51 74 89
6 31 {32 51} 74 89
6 31 32 {51 74} 89
6 31 32 51 {74 89}
6 31 32 51 74 89

*Sorted in 5th pass, however, 6th pass will occur since its one element may not be sorted yet in some sitation. Making it O(n^2)*
"""