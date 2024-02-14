# Input = 4
# FibonacciSeries = 0,1,1,2,3,5,8,13,21,...
# Output = 3

def IterativeFibonacciIndex(n):
    arr = [0,1]
    for i in range(2,n+1,1):
        arr.append(arr[i-1]+arr[i-2])
    return arr[n]

# def IterativeFibonacciIndex(n):
#     next = 1
#     prev = 0
#     count = 2
#     if(n==0):
#         return 0
#     elif(n==1):
#         return 1
#     else:
#         while(count<=n):
#             new = next + prev
#             prev = next
#             next = new
#             count+=1
#     return new


def RecursiveFibonacciIndex(n): 
    if(n<2):
        return n
    
    return RecursiveFibonacciIndex(n-1) + RecursiveFibonacciIndex(n-2)
# Recursive Algorithm takes Exponential Time i.e. O(2^n)
# Since, fib(7)
#       /      \
#     fib(6)   fib(5)
#     /    \   /    \
    
print("Iterative: ",IterativeFibonacciIndex(8))
print("Recursive: ",RecursiveFibonacciIndex(8))
