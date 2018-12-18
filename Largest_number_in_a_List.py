def largest_num():
    flag = True
    while flag:
        flag = False
        try:
            count = 0
            our_list = []
            for i in range(0, 5):
                number = int(round(float(input('Please enter a number: '))))
                our_list.append(number)
                print(our_list)
        except ValueError:
            print("Enter a Valid Input")
            flag = True
        except IndexError:
            print("Enter a Valid Input")
            flag = True
    for x in our_list:
        our_list.sort()
        count += 1
        return our_list[4]
ln = largest_num()
print("The Largest Number in the List is", ln)
