def MemoizationAddto80():
    cache = {}

    def Addto80(n):
        if(n not in cache):
            print("Consider huge/complex calculation")
            cache[n] = n + 80
            return cache[n]
        else:
            return cache[n]

    return Addto80


memoized = MemoizationAddto80()

print(memoized(5),"\n")
print(memoized(6),"\n")
print(memoized(5),"\n")
print(memoized(8),"\n")
print(memoized(6),"\n")
print(memoized(8),"\n")