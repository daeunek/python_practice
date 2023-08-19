teens = ["ten","eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
units = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def num_to_word(num):
    s = [int(i) for i in str(num)]
    F = s[0]
    # S = s[1]
    # T = s[2]

    if num > 999:
        word = "I don't know."
    else:
        if 0 < num < 10:
            word = f"{units[F -1]}"
        
        
        elif num < 20:
            word = teens[s[1] - 1]
        elif num < 100:
            word = tens[s[0] - 2]
            if s[1] != 0:
                word += "-" + units[s[1] - 1]
        elif num < 1000:
            word = units[s[0] - 1] + " hundred"
            if s[1] != 0:
                word += " and "
                if s[1] == 1:
                    word += teens[s[2] - 1]
                else:
                    word += tens[s[1] - 2]
                    if s[2] != 0:
                        word += "-" + units[s[2] - 1]

    return word

num = int(input("Enter a number: "))
print(num_to_word(num))
