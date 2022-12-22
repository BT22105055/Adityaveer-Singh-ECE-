side1 = float(input("Enter side 1:"))
side2 = float(input("Enter side 2:"))
side3 = float(input("Enter side 3:"))
if side1 >= side2 + side3:
    print("Yes")
elif side2 >= side1 +side3:
    print("Yes")
elif side3 >= side2 + side1:
    print("Yes")
else:
    print("No")