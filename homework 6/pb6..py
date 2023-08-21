'''
Write a function to return an integer
whose digits are in the reversed order of the given integer.
'''
def reverse(num):
    num_s = str(num)
    rev = num_s[::-1]

    rev = int(rev)
    return rev

num = int(input("Enter an integer: "))
result = reverse(num)
print(f" reverse of {num} returns {result}")
print(type(result))

