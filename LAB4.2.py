x=int(input("Enter the year to be analyzed--"))
if x%4==0:
    print("The given year is a leap year")
elif x%100==0 and x%400==0:
    print("The given year is a leap year")
else:
    print("The given year is not a leap year")
