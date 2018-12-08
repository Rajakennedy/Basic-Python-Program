import datetime
current_time = datetime.datetime.now()

name = str(input("Full Name is "))
if current_time.hour <= 12:
    print('"Good Morning,', name.split()[0] + '"')

elif 12 < current_time < 18:
        print('"Good AfterNoon,', name.split()[0] + '"')
else:
    print('"Good Night,', name.split()[0] + '"')


