print("Welcome to calculator")
print("Please type your first number:")
x = float(input())
print("What do you want to do?")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choose1 = float(input())

if choose1 == 1:
    print("Add your new number here:")
    y = float(input())
    print("Your total is:", x+y)
    x = x+y
elif choose1 == 2:
    print("Subtract your new number here:")
    y = float(input())
    print("Your total is:", x-y)
    x = x-y
elif choose1 == 3:
    print("Multiply your new number here:")
    y = float(input())
    print("Your total is:", x*y)
    x = x*y
elif choose1 == 4:
    print("Divide your new number here:")
    y = float(input())
    print("Your total is:", x/y)
    x = x/y
else:
    print("Error! That is not a valid calculation")
print("Do you want to continue?:")
print("1. Yes")
print("2. Nope")
continue_ = float(input())
while continue_ == 1:
    print("What do you want to do?")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choose1 = float(input())

    if choose1 == 1:
        print("Add your new number here:")
        y = float(input())
        print("Your total is:", x + y)
        x = x + y
    elif choose1 == 2:
        print("Subtract your new number here:")
        y = float(input())
        print("Your total is:", x - y)
        x = x - y
    elif choose1 == 3:
        print("Multiply your new number here:")
        y = float(input())
        print("Your total is:", x * y)
        x = x * y
    elif choose1 == 4:
        print("Divide your new number here:")
        y = float(input())
        print("Your total is:", x / y)
        x = x / y
    else:
        print("Error! That is not a valid calculation")
    print("Do you want to continue?:")
    print("1. Yes")
    print("2. Nope")
    continue_ = int(input())

print("Thank you for using the calculator")