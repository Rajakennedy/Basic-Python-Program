flag = 1
while flag:
    flag = 0
    try:
        number = int(input("Enter the num: ")) - 1
        if number <= 0:
          print("Prime number should be Greater than Zero")
          flag = 1
    except ValueError:
        print("Enter a Valid number")
        flag = 1

def nextPrime(number):
    for i in range(2,number):
        if number%i == 0:
            return False
        sqr=i*i
        if sqr>number:
           break
    return True

while(True):
    res=nextPrime(number)
    if res:
        print("The next number number is: ",number)
        break
    number += -1