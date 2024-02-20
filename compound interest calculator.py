principle = float(input("Enter the principle amount: "))
while principle <= 0:
    print("Principle amount can't be zero or less")
    float(input("Enter the principle amount: "))
rate = int(input("Enter the rate of interest: "))
while rate <= 0:
    print("Rate of interest can't be zero or less")
    float(input("Enter rate of interest: "))
time = int(input("Enter the time in years: "))
while time <= 0:
    print("Time can't be zero or less")
    float(input("Enter the time in years: "))
total = principle * pow((1 + (rate/100)),time)
print(f"balance after {time} year/s: Rs.{total:.2f}")
