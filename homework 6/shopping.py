'''
Problem 2: Shopping List
Create a program that allows a user to input items and their quantities for a shopping list.
 Store this information in a dictionary and print the resulting dictionary.
'''
def create_shopping_list():
    s_list = {}

    while True:
        item = input("enter an item (or done to finish): ")
        if item.lower() == "done":
            break

        quantity = int(input("enter quantity: "))
        s_list[item] =  quantity
    return s_list

def main():
    s_list = create_shopping_list()
    # for item, quantity in s_list.items():
    #     print(f"'{item}' : {quantity}")
    print(s_list)

main()

    


