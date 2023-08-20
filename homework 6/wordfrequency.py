def count_frequency():
    output = {}
    s_list = input("Enter the sentence: ").split()

    for word in s_list:
        if word not in output:
            #counting the word
            output[word] = 1
        else:
            output[word] += 1

    return output

def main():
    print(count_frequency())

main()



