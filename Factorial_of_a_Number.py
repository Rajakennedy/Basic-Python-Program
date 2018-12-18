def fac_of_num():
    global num
    factor = 1
    flag = True
    while flag:
        flag = False
        try:
            num = int(round(float(input("Enter the Number: "))))
            if num == 0:
                print("The Factorial of Zero is One")
                flag = True
            else:
                if num < 0:
                    print("The Number should be Positive")
                    flag = True
        except ValueError:
            print("Enter a Valid Input")
            flag = True
    if num > 0:
        for x in range(1, num + 1):
            factor = factor * x
    return factor

fac = fac_of_num()
print("The factorial of", num,"is",fac)