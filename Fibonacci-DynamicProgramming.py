print("\n------ Dynamic Programming -----")
#Using Dynamic Programming, Time Complexity: O(n)
calculations_dynamic = 0
def MemoizedFibonacciIndex():

    cache = {}

    def FibonacciIndex(n):
        global calculations_dynamic
        calculations_dynamic+=1
        
        if(n not in cache):
            if(n<2):
                return n
            else:
                cache[n] = FibonacciIndex(n-1)+FibonacciIndex(n-2)
                return cache[n]
        else:
            return cache[n]
        
    return FibonacciIndex

memoized = MemoizedFibonacciIndex()
n_dynamic = 7
n_dynamic_2 = 10
print("1. Fibonacci Number at index ",n_dynamic,":",memoized(n_dynamic))
print("\tNumber of calculations performed:",calculations_dynamic)
calculations_dynamic = 0
print("\n2. Fibonacci Number at index ",n_dynamic_2,":",memoized(n_dynamic_2))
print("\tNumber of calculations performed:",calculations_dynamic)

print("\n------ Plain Recursive Function -----")

#Using Recursive Functions, Time Complexity: O(2^n)
calculations = 0
def FibonacciIndex(n):
    global calculations #Use of global keyword to access global variable without returning or using parameters
    calculations += 1
    if(n<2):
        return n
    else:
        return FibonacciIndex(n-1)+FibonacciIndex(n-2)

n=7
n_2 = 10
print("1. Fibonacci Number at index ",n,":",FibonacciIndex(n))
print("\tNumber of calculations performed:",calculations)
calculations = 0
print("\n2. Fibonacci Number at index ",n_2,":",FibonacciIndex(n_2))
print("\tNumber of calculations performed:",calculations)

