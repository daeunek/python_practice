# The program outputs the Eng pronunciation of the number.
def number_to_word(num):
    
    one_digit = { 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
                6: "six", 7: "seven", 8:"eight", 9:"nine", 0: "zero"}

    teens = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

    tens = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty',
            6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
    
    if 0 <= num <= 9:
        word = one_digit[num]
    elif 10 <= num <= 19:
        word = teens[num]
    elif 20 <= num <= 99:
        if num % 10 == 0:
            word = tens[num // 10]
        else:
            word = tens[num // 10] + "-" + one_digit[num %10]
    elif 100 <= num <= 999:
        if num % 100 == 0:
            word = one_digit[num // 100] + " hundred"
        elif num % 100 < 10:
            word = one_digit[num//100] + " hundred and " + one_digit[num % 100]
        elif num % 100 < 20:
            word = one_digit[num//100] + " hundred and " + teens[num % 100]
        elif (num % 100) % 10 == 0:
            word = one_digit[num//100] + " hundred and " + tens[(num%100)//10]
        else:
            word = one_digit[num//100] + " hundred and " + tens[(num%100)//10] + " " + one_digit[num%10]
        
    else:
        word ="I don't know."

    return word

num = int(input("Enter a number: "))
print(number_to_word(num))
