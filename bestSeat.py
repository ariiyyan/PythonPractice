def bestSeat(seats):
    # Write your code here.
    print("array of seats is = " , seats)
    bestSeat = -1
    maxSpace = 0

    left = 0
    while left < len(seats):
        right = left + 1
        while right < len(seats) and seats[right] == 0:
            right += 1

        space = right - left -1
        if space > maxSpace:
            maxSpace = space
            bestSeat = (left + right) // 2
            
        left = right
    print("print the best seat index = ", bestSeat , " and also print the space = ", maxSpace)
    return bestSeat
