unit = input("Is the temperature in celsius or fahrenheit(C/F)?: ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = (temp * (9/5) + 32)
    print(f"The temperature in fahrenheit is {round(temp, 2)}F")
elif unit == "F":
    temp = (temp - 32) * (5/9)
    print(f"The temperature incelsius is {round(temp, 2)}C")
else:
    print(f"{unit} is an Invalid unit of measurement")

