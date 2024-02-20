import math

a = float(input("Enter the side A of the triangle: "))
b = float(input("Enter the side B of the triangle: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The side C is {round(c, 2)}")

