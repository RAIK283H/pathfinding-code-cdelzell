
# get all the permutations of nodes in a graph
def getPermutations(graph):
    mobileNums = []
    permutations = []
    for i in range(1, len(graph)+1):
        #if positive, points left, if negative, points right
        mobileNums.append(i)
    permutations.append(getPositiveValueOfList(mobileNums))

    while(checkForMobile(mobileNums)):
        largestMobile, swapIndex = getLargestMobile(mobileNums)
        temp = mobileNums[swapIndex]
        mobileNums[swapIndex] = mobileNums[largestMobile]
        mobileNums[largestMobile] = temp
        reverseDirection(mobileNums[largestMobile], mobileNums)
        print(mobileNums[largestMobile])

        permutations.append(getOriginalNodeValuesofList(getPositiveValueOfList(mobileNums)))
    
    return permutations

# Get the largest mobile number from a list
#list = [1, 2, 3]
def getLargestMobile(list):
    maxMobile = -1000
    maxIndex = -100
    swapIndex = -100
    for i in range(len(list)):
        if (list[i] > 0 and i != 0):
            if(abs(list[i]) - abs(list[i - 1]) > 0 and abs(list[i]) > maxMobile):
                maxMobile, maxIndex, swapIndex = getMaxAndSwap(list, i, False)
        if (list[i] < 0 and i != len(list) - 1):
            if(abs(list[i]) - abs(list[i + 1]) > 0 and abs(list[i]) > maxMobile):
                maxMobile, maxIndex, swapIndex = getMaxAndSwap(list, i, True)

    return maxIndex, swapIndex

# Get the new max value and index and new swap index
def getMaxAndSwap(list, i, positive):
    maxMobile = abs(list[i])
    maxIndex = i
    if(positive):
        swapIndex = i+1
    else:
        swapIndex = i-1

    return maxMobile, maxIndex, swapIndex

# Check if there are any mobile numbers in a given list
def checkForMobile(list):
    mobile = [False] * len(list)

    for i in range(len(list)):
        if (list[i] > 0 and i != 0):
            if(list[i] - list[i - 1] > 0):
                mobile[i] = True
        if (list[i] < 0 and i != len(list) - 1):
            if(list[i] - list[i + 1] > 0):
                mobile[i] = True
    
    if True in mobile:
        return True
    
    return False

#reverses the sign (+ or -) for all values in the list that are larger than the absolute value of the given integer
def reverseDirection(largestMobile, list):
    for i in range(len(list)):
        if(abs(list[i]) > abs(largestMobile)):
            list[i] = -list[i]
    return list


#Gets all positive values (because + and - signs are used for direction purposes)
def getPositiveValueOfList(list):
    positiveList = list.copy()
    
    for i in range(len(list)):
        if(positiveList[i] < 0):
            positiveList[i] = positiveList[i] * -1
    
    return positiveList

#Also moves all values back one to take into account for moving all values forward one
#in the getPermutations method (so that there is no 0 in the list, 0 cannot take on a direction) 
def getOriginalNodeValuesofList(list):
    originalNodes = list.copy()
    
    for i in range(len(list)):
        originalNodes[i] = originalNodes[i] - 1
    
    
    return originalNodes




# Initialize the first permutation with <1 <2 ... <n
# while there exists a mobile integer
#   find the largest mobile integer k
#   swap k and the adjacent integer it is looking at
#   reverse the direction of all integers larger than k