'''
Problem 1: Count Characters
Write a program that takes a string as input and counts the frequency of each character in the string. 
Print the results in a dictionary format.
'''

def count_cha(line):
    count={}

    for i in line:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

    return count

def main():
    line = input("Enter: ")
    result = count_cha(line)
    for key, val in result.items():
        print(f"'{key}' : {val}")
    
main()