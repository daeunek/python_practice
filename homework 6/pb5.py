# This progam will combine notes:
def note_change(money):
    notes = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
    count = {}

    for i in notes:
        if money >= i:
            count[i] = money // i
            money = money % i

    return count

def main():
    money = int(input("Enter the amount: "))
    result = note_change(money)
    for key, val in result.items():
        if 20 <= key <= 1000:
            print(f"{key}-Baht notes: {val} ")

        else:
            print(f"{key}-Baht coins: {val} ")
main()


    


