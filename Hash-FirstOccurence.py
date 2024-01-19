array = [1,5,4,3,2,5,7,8]

map = {}
def FindOccurences(array):

    for i in array:
        if i in map:
            return i
        else:
            map[i] = True
    return "Not Found!"

ans = FindOccurences(array)
print(ans)
print(map)
