def missingNumbers(nums):
    # Write your code here.
    # first make a dictionary that has all the number as key and also 
    #has value of false for all of them then for loop to nums list and
    #change each numebr value that is in the list True at the end do another
    #for loop in dictionary and check which numbers are false and add them to 
    #output list
    output = []
    myHash = {}
    print("print of length of num = ", len(nums))
    for i in range (1, len(nums) + 3):
        myHash[i] = False
    print("print dictionary = ", myHash)
    for i in nums:
        if i in myHash:
            myHash[i] = True

    for i in myHash:
        if myHash[i] == False:
            output.append(i)
    return output
