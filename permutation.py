import pathing

# get all the permutations of nodes in a graph
def getPermutations(graph):
    mobileNums = []
    permutations = []

    if(len(graph) == 0):
        return []

    for i in range(1, len(graph)+1):
        #if positive, points left, if negative, points right
        mobileNums.append(i)
    permutations.append(getOriginalNodeValuesofList(getPositiveValueOfList(mobileNums)))

    while(checkForMobile(mobileNums)):
        largestMobileIndex, swapIndex = getLargestMobile(mobileNums)
        
        mobileNums[largestMobileIndex], mobileNums[swapIndex] = mobileNums[swapIndex], mobileNums[largestMobileIndex]

        reverseDirection(mobileNums[swapIndex], mobileNums)

        permutations.append(getOriginalNodeValuesofList(getPositiveValueOfList(mobileNums)))
    
    return permutations

# Get the largest mobile number from a arr
#arr = [1, 2, 3]
def getLargestMobile(arr):
    maxMobile = -1000
    maxIndex = -100
    swapIndex = -100
    for i in range(len(arr)):
        if (arr[i] > 0 and i != 0):
            if(abs(arr[i]) - abs(arr[i - 1]) > 0 and abs(arr[i]) > maxMobile):
                maxMobile, maxIndex, swapIndex = getMaxAndSwap(arr, i, False)
        if (arr[i] < 0 and i != len(arr) - 1):
            if(abs(arr[i]) - abs(arr[i + 1]) > 0 and abs(arr[i]) > maxMobile):
                maxMobile, maxIndex, swapIndex = getMaxAndSwap(arr, i, True)

    return maxIndex, swapIndex

# Get the new max value and index and new swap index
def getMaxAndSwap(arr, i, positive):
    maxMobile = abs(arr[i])
    maxIndex = i
    if(positive):
        swapIndex = i+1
    else:
        swapIndex = i-1

    return maxMobile, maxIndex, swapIndex

# Check if there are any mobile numbers in a given arr
def checkForMobile(arr):

    for i in range(len(arr)):
        if (arr[i] > 0 and i != 0):
            if(arr[i] - arr[i - 1] > 0):
                return True
        if (arr[i] < 0 and i != len(arr) - 1):
            if(arr[i] - arr[i + 1] > 0):
                return True
    
    return False

#reverses the sign (+ or -) for all values in the arr that are larger than the absolute value of the given integer
def reverseDirection(largestMobile, arr):
    for i in range(len(arr)):
        if(abs(arr[i]) > abs(largestMobile)):
            arr[i] = -arr[i]
    return arr


#Gets all positive values (because + and - signs are used for direction purposes)
def getPositiveValueOfList(arr):
    positiveList = arr.copy()
    
    for i in range(len(arr)):
        if(positiveList[i] < 0):
            positiveList[i] = positiveList[i] * -1
    
    return positiveList

#Also moves all values back one to take into account for moving all values forward one
#in the getPermutations method (so that there is no 0 in the arr, 0 cannot take on a direction) 
def getOriginalNodeValuesofList(arr):
    originalNodes = arr.copy()
    
    for i in range(len(arr)):
        originalNodes[i] = originalNodes[i] - 1
    
    
    return originalNodes

#Get all hamiltonian cycles in a graph
#so this is actually checking for hamiltonian paths, not cycles, big difference!
def getHamiltonian(graph):
    permutations = getPermutations(graph)
    validCycles = []
    for path in permutations:
        if(pathing.check_adjacent_nodes(path, graph)):
            validCycles.append(path)
    
    if (validCycles == None) :
        return False
    
    return validCycles

# remove the 0 and len(graph) - 1 nodes from the list
# check if it is a valid path
# check if every node (1 - (len(graph) - 1)) is visited //actually this should be a given,\
# no need to check if the permutation method is working correctly all nodes will be in each permutation
# check if the last node has the first node in its adjacency list

def findHamiltonian(graph):
    permutations = getPermutations(graph)
    print(permutations)
    validCycles = []
    exitNode = len(graph) - 1

    for path in permutations:
        path.remove(0)
        path.remove(exitNode)

        if(pathing.check_adjacent_nodes(path, graph) and checkIfInAdjacencyList(path[len(path)-1], path[0], graph)):
            validCycles.append(path)

    return validCycles

def checkIfInAdjacencyList(nodeIndex, adjacentNodeIndex, graph):
    node = graph[nodeIndex]

    if(adjacentNodeIndex in node[1]):
        return True
    
    return False

