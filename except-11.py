#!/usr/bin/python3

while True:
    try:
        print("Let's divide x by y!")
        x = int(input("WHat is the value of x? "))
        y = int(input("What is the value of y? "))
        print("The value of x/y is:", x/y)
    except ZeroDivisionError:
        print("You cannot divide by zero!")
    except ValueError:
        print("You seem to be giving a non-numerical value, Let's try again")

#    except Exception as err:
#        print(err)
