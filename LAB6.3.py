rows = int(input("Enter the number of rows:"))
prev = [1,1]
for i in range (0,rows):
    curr = []
    if (i == 0):
        f = " "*(rows - 1) + str(1)
        print(f)
    if(i >= 1):
        b = ''
        curr.append(1)
        for j in range(0,len(prev) - 1):
            sum = prev[j] + prev [j + 1]
            curr.append(sum)
            b = b + str(sum) + ' '
        curr.append(1)
        a = " "*(rows - i - 1) + str(1) + ' ' + b + str(1)
        print(a)
    prev = curr