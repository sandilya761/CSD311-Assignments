def generateSquare(n):
 
    # 2-D array with all
    # slots set to 0
    magicSquare = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]  
 
    # initialize position of 1
    i = n / 2
    j = n - 1
 
    # Fill the magic square
    # by placing values
    temp = 1
    while temp <= (n * n):
        if i == -1 and j == n:  # 3rd condition
            j = n - 2
            i = 0
        else:
 
            # next number goes out of
            # right side of square
            if j == n:
                j = 0
 
            # next number goes
            # out of upper side
            if i < 0:
                i = n - 1
 
        if magicSquare[int(i)][int(j)]:  # 2nd condition
            j = j - 2
            i = i + 1
            continue
        else:
            magicSquare[int(i)][int(j)] = temp
            temp = temp + 1
 
        j = j + 1
        i = i - 1  # 1st condition
 
    # Printing magic square
    print("Magic Squre for n =", n)
    print("Sum of each row or column",
          15, "\n") #since n(n*n+1)/2 = 15 and n = 3
    # To display output
    # in matrix form
    print("   0, 1, 2")
    for count, row in enumerate(magicSquare):
        print(count, row)

generateSquare(3)
 
