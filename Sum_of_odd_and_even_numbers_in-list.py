def sum_odd_even_num():
    even_sum = 0
    odd_sum = 0
    flag = 1
    while flag:
        flag = 0
        try:
            our_list = []
            for i in range(0, 5):
                number = int(round(float(input("Please enter a number"))))
                our_list.append(number)
                print(our_list)
        except ValueError:
            print("Enter a Valid Input")
            flag = 1
    for x in our_list:
        if not x % 2:
            even_sum += x
        else:
            odd_sum += x
    print("The sum of even numbers is: ", even_sum)
    print("The sum of odd numbers is: ", odd_sum)
    return even_sum, odd_sum
sum_eve =sum_odd_even_num()
print("even_sum and odd_sum", sum_eve)
