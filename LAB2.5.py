string = input("Enter your string: ")
a = string.find("name")
if a in range(0,len(string)+1):
    print("Yes")
else:
    print("No")
