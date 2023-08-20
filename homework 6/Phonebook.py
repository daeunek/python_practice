def phone_dicionaries():
    dic = {}

    while True:
        Name = input("ENterr name, or done to finish: ")
        if Name.lower() == "done":
            break

        Phone = input(" ENter phone number")
        dic[Name] = Phone
    return dic

def main():
    Result = phone_dicionaries()
    name = input("Name: ")
    print(f"Phone: {Result[name]}")

main()

    
