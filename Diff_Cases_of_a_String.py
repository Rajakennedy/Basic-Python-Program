def upper_case():
    global string
    flag = 1
    while flag:
        flag = 0
        try:
            string = input("Enter the string: ")
            length = 0
            if string.isnumeric() or string.isspace():
                print("Enter a Valid String")
                flag = 1

            elif set('[0987654321]+$').intersection(string):
                    print("Enter a Valid String")
                    flag = 1
        except ValueError:
            print("Enter a Valid String")
            flag = 1

        if set('[~!@#$%^&*()_+{}":;\']+$').intersection(string):
            print("Invalid entry.")
            flag = 1
        else:
             new_string = string.upper()
             length += 1
    return new_string

UC = upper_case()
print("The upper case of the String is:", UC)

def lower_case():
    global string
    flag = 1
    while flag:
        flag = 0
        try:
            string = input("Enter the string: ")
            length = 0
            if string.isnumeric() or string.isspace():
                print("Enter a Valid String")
                flag = 1

            elif set('[0987654321]+$').intersection(string):
                    print("Enter a Valid String")
                    flag = 1
        except ValueError:
            print("Enter a Valid String")
            flag = 1

        if set('[~!@#$%^&*()_+{}":;\']+$').intersection(string):
            print("Invalid entry.")
            flag = 1
        else:
             new_string = string.lower()
             length += 1
    return new_string
lc = lower_case()
print("The Lower Case of the String is", lc)

def camel_case():
    global string
    flag = 1
    while flag:
        flag = 0
        try:
            string = input("Enter the string: ")
            length = 0
            if string.isnumeric() or string.isspace():
                print("Enter a Valid String")
                flag = 1

            elif set('[0987654321]+$').intersection(string):
                    print("Enter a Valid String")
                    flag = 1
        except ValueError:
            print("Enter a Valid String")
            flag = 1

        if set('[~!@#$%^&*()_+{}":;\']+$').intersection(string):
            print("Invalid entry.")
            flag = 1
        else:
             new_string = string.capitalize()
             length += 1
    return new_string
cc = camel_case()
print("The Camel Case of the string is", cc)

