#Program 2: Find the lowest number
#Create a program that ask 3 numbers. 
#Find the lowest number using only if-else statement.
#Display the lowest number


number1 = float(input("Give 1st Number: "))
number2 = float(input("Give 2nd number: "))
number3 = float(input("Give 3rd Number: "))

if number1 < number2 and number1 < number3:
    print(f"The lowest number is {number1}")
else:
    if number2 < number1 and number2 < number3:
        print(f"The Lowest number is {number2}")
    else:
        if number3 < number1 and number3 < number2:
            print(f"The Lowest number is {number3}")
            
print("Done")