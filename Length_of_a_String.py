def len_string():
    length = 0
    flag = 1
    while flag:
        flag = 0
        try:
            string = input("Enter the string: ")
            if string.isspace()or string.isnumeric():
                print("Enter a valid string")
                flag = 1
        except ValueError:
            print("Enter a Valid input")
            flag = 1
    for x in string:
        length += 1
    return length

str_length = len_string()
print("The length of the string is: ", str_length)