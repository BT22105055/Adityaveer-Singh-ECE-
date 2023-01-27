def pangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
    return True
string = input("Enter the string:")
if (pangram(string) == True):
    print("Yes, its a pangram")
else:
    print("No, not a pangram")