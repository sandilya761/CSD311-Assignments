def generateSquare(n):
 
    # initially all the grids are set to 0
    magicSquare = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]  
 
    # first we fit the position of 1
    i = n / 2
    j = n - 1
 
    # Filling the magic square from the conditions
    
    temp = 1
    while temp <= (n * n):
        if i == -1 and j == n:  
            j = n - 2
            i = 0
        else:
 
            # if the next number goes out of range
            
            if j == n:
                j = 0
 
            # condition if the next number goes out of range in upper side
            
            if i < 0:
                i = n - 1
 
        if magicSquare[int(i)][int(j)]:  
            j = j - 2
            i = i + 1
            continue
        else:
            magicSquare[int(i)][int(j)] = temp
            temp = temp + 1
 
        j = j + 1
        i = i - 1  
 
    # Printing magic square
    print("Magic Squre for n=3 whose sum is 15 in each row and column")#since n(n*n+1)/2 = 15 and n = 3
    
    print("   0, 1, 2")
    for count, row in enumerate(magicSquare):
        print(count, row)

generateSquare(3)
 
