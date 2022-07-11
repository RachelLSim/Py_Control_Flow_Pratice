#########################################
# Nested if/else statement

print("Welcome to the rollercoaster?")
height = int(input("What is your height in cm?"))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        print("Please pay $5.00")
    elif age >= 12 & age <= 18:
        print("Please pay $7.00")
    else:
        print("Please pay $12.00")
else:
    print("Sorry, you're not quite tall enough to ride!")