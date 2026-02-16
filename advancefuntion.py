num_1 = [1,2,3]
num_2 = [4,5,6]
result = map(lambda x, y: x + y, num_1, num_2)
print("addition of two lists")
print(list(result))
nums = [1,2,3,4,5]
def sq(n):
    return n*n
square = list(map(sq, nums))
print("squares of the list")
print(square)