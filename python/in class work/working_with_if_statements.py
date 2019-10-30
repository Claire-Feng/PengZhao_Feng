string1 = "Vegetable"
string2 = "Vegetable"

print(string1 == string2)

print(string1 != string2)

if string1.lower() == string2.lower():
    print("The strings are equal")
else:
    print("The strings are not equal")


number1 = 25
number2 = 30


if number1 <= number2:
    print("number 1 is greater")


name_1 = "Stephen"
name_2 = "stephen"

number_1 = 45
number_2 = 50

if name_1.lower() == name_2.lower() and number_1 < number_2:
    print("We passed the test")