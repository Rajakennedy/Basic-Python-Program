flag = 1
while flag:
    flag = 0
    try:
        number = int(input("Enter a number: "))
        if number <= 0:
          print("Prime number should be Greater than Zero")
          flag = 1
    except ValueError:
        print("Enter a Valid number")
        flag = 1

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

