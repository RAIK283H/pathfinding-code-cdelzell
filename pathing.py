import graph_data
import global_game_data
from numpy import random
from collections import deque
import math

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())


def get_test_path():
    return graph_data.test_path[global_game_data.current_graph_index]

##goes to random nodes
##keeps track of if it has hit the target
##if it has hit the target and is at the end node, it can exit
##otherwise, it will keep generating nodes to visit
def get_random_path():

    # assert preconditions
    assert graph_data.graph_data is not None, "There is no graph data."
    assert global_game_data.current_graph_index is not None, "There is no graph index chosen."
    assert graph_data.graph_data[global_game_data.current_graph_index] is not None, "There is no graph chosen."

    graph = graph_data.graph_data[global_game_data.current_graph_index]
    start_node = graph[0]
    target = global_game_data.target_node[global_game_data.current_graph_index]
    target_reached = False
    end_node = graph[len(graph) - 1]
    current_node = start_node
    path = [0]


    while(not target_reached or current_node != end_node) :
        options = current_node[1]
        random_choice = random.choice(options)
        path.append(int(random_choice))
        current_node = graph[path[len(path) - 1]]

        if(random_choice == target) :
            target_reached = True
        

    ## test necessary post-conditions
    assert target in path, "This path does not contain the necessary target"
    assert path is not None, "This path does not contain any nodes"
    assert path[0] == 0, "This path does not start at the correct node"
    assert path[len(path) - 1] == len(graph) - 1, "This path does not end at the correct node"
    assert check_adjacent_nodes(path, graph), "This path is not a connected path"


    return path

## ensure that a path is made of sequential nodes all connected by edges
# (i.e there are no breaks in the path)
def check_adjacent_nodes(path, graph):

    for i in range(0, len(path) - 1):
        node_info = graph[path[i]]
        if(i == len(path) - 1):
            if(not(path[i-1] in node_info[1])):
                return False
        elif(not(path[i+1] in node_info[1])) :
            return False
    
    return True

def get_dfs_path():
    # assert preconditions
    assert graph_data.graph_data is not None, "There is no graph data."
    assert global_game_data.current_graph_index is not None, "There is no graph index chosen."
    assert graph_data.graph_data[global_game_data.current_graph_index] is not None, "There is no graph chosen."

    graph = graph_data.graph_data[global_game_data.current_graph_index]
    target = global_game_data.target_node[global_game_data.current_graph_index]
    start_node = 0
    end_node = len(graph) - 1

    #get path from start to target
    path = dfs_path_creation(graph, start_node, target)
    #remove last node of path so no duplication
    path.pop()
    #add path from target to end
    path.extend(dfs_path_creation(graph, target, end_node))

    ## test necessary post-conditions
    assert target in path, "This path does not contain the necessary target"
    assert path is not None, "This path does not contain any nodes"
    assert path[0] == 0, "This path does not start at the correct node"
    assert path[len(path) - 1] == len(graph) - 1, "This path does not end at the correct node"
    assert check_adjacent_nodes(path, graph), "This path is not a connected path"

    return path


# get path from start to target node using depth-first-search
def dfs_path_creation(graph, start, target):
    #initialize variables
    targetReached = False
    visited = [False] * len(graph)
    stack = []
    path = []

    #if nodes are the same, return path with start node only
    if(start == target):
        path.append(start)
        return path

    #set start node to visited and add to the stack
    visited[start] = True
    stack.append(start)

    #while the stack is not empty or the target not reached, pop the node and add its neighbors to the stack
    #if target is found, add the stack to the path and return
    while ((not len(stack) == 0) or (not targetReached)):
        node = stack.pop()
        adjList = graph[node][1]
        nodesAdjacent = [False] * len(adjList)
        for i in adjList:
            if(visited[i] == False):
                stack.append(node)
                visited[i] =True
                stack.append(i)
                if(i == target):
                    targetReached = True
                    path.extend(stack)
                break

    return path

                



def get_bfs_path():

    # assert preconditions
    assert graph_data.graph_data is not None, "There is no graph data."
    assert global_game_data.current_graph_index is not None, "There is no graph index chosen."
    assert graph_data.graph_data[global_game_data.current_graph_index] is not None, "There is no graph chosen."

    graph = graph_data.graph_data[global_game_data.current_graph_index]
    target = global_game_data.target_node[global_game_data.current_graph_index]
    start_node = 0
    end_node = len(graph) - 1

    #get path from start to target
    path = bfs_path_creation(graph, start_node, target)
    #remove end node so no duplication in the path
    path.pop()
    #get path from target to end
    path.extend(bfs_path_creation(graph, target, end_node))

    ## test necessary post-conditions
    assert target in path, "This path does not contain the necessary target"
    assert path is not None, "This path does not contain any nodes"
    assert path[0] == 0, "This path does not start at the correct node"
    assert path[len(path) - 1] == len(graph) - 1, "This path does not end at the correct node"
    assert check_adjacent_nodes(path, graph), "This path is not a connected path"

    return path


# get path from start to target node using depth-first-search
def bfs_path_creation(graph, start, target):
    #initialize variables
    targetReached = False
    visited = [False] * len(graph)
    parent = [0] * len(graph)
    parent[0] = -1
    queue = []
    path = []

    #if nodes are the same, return path with start node only
    if(start == target):
        path.append(start)
        return path

    #set start to visited and add to queue
    visited[start] = True
    queue.append(start)

    #while the queue is not empty or the target not reached, pop the node and add its neighbors to the queue
    #if target is found, recursivley get the path with the helper function, reverse it, and return
    while ((not len(queue) == 0) or (not targetReached)):
        node = queue.pop(0)
        adjList = graph[node][1]
        nodesAdjacent = [False] * len(adjList)
        for i in adjList:
            if(visited[i] == False):
                visited[i] = True
                parent[i] = node
                queue.append(i)
                if(i == target):
                    targetReached = True
                    get_parents(path, parent, start, i)
                    break
                
    #reverse path and return
    path.reverse()
    return path


#Get the path of the node to the start node by identifying the parents
#returns path of nodes with the first node being the child node index and the final
#node in the list being the start node index
#   path -> the path to add nodes to
#   parents -> the parent for each node, stored as a list
#   start -> the start node index of the path we are tracing back
#   node -> the end node index of the path we are tracing back
def get_parents(path, parents, start, node):
    #base case, if at start node append start node
    if(node == start):
        return path.append(node)
    else: #else append the node and pass in its parent to the function again
        path.append(node)
        get_parents(path, parents, start, parents[node])

    return path

def get_dijkstra_path():

    # assert preconditions
    assert graph_data.graph_data is not None, "There is no graph data."
    assert global_game_data.current_graph_index is not None, "There is no graph index chosen."
    assert graph_data.graph_data[global_game_data.current_graph_index] is not None, "There is no graph chosen."

    graph = graph_data.graph_data[global_game_data.current_graph_index]

    #initialize list of all nodes with distance of infinity (Essentially), no parent, and unsolved
    nodeInfo = initializeNodeInfo(graph)

    #set start node distance to zero
    nodeInfo[0][1] = 0

    queue = []
    queue.append(nodeInfo[0])

    while len(queue) > 0 :
        vertex = highestPriority(queue)
        
        nodeInfo[vertex[0]][3] = True

        neighborNodes = graph[vertex[0]][1]

        for neighbor in neighborNodes:
            distance = nodeInfo[vertex[0]][1] + calculateDistance(graph[vertex[0]], graph[neighbor])
            if nodeInfo[neighbor][3] is False and distance < nodeInfo[neighbor][1]:
                nodeInfo[neighbor][1] = distance
                nodeInfo[neighbor][2] = vertex[0]
                queue.append(nodeInfo[neighbor])
    
    parents = []
    
    target = global_game_data.target_node[global_game_data.current_graph_index]

    parents = getFullPath(graph, target, nodeInfo, parents)

    return parents

#initialize list of nodes, including index, distance, parent, and unsolved status
def initializeNodeInfo(graph):
    nodeInfo = []

    for i in range(len(graph)):
        nodeInfo.append([i, 1000, None, False])

    return nodeInfo

#Get the lowest distance node from a queue and return/remove it from the queue
def highestPriority(queue):
    min = 1000
    minVertexIndex = -1

    for v in range(len(queue)):
        if queue[v][1] < min :
            min = queue[v][1]
            minVertexIndex = v

    vertex = queue[minVertexIndex]
    del queue[minVertexIndex]

    return vertex

def calculateDistance(v1, v2):
    x1 = v1[0][0]
    y1 = v1[0][1]

    x2 = v2[0][0]
    y2 = v2[0][1]

    return math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))

def getPathToNode(nodeInfo, parents, startIndex, targetIndex):
    if nodeInfo[startIndex][2] == targetIndex:
        parents.append(targetIndex)
    else:
        getPathToNode(nodeInfo, parents, nodeInfo[startIndex][2], targetIndex)
        parents.append(nodeInfo[startIndex][2])
        

    return parents

def getFullPath(graph, target, nodeInfo, parents):

    parents = getPathToNode(nodeInfo, parents, target, 0)
    getPathToNode(nodeInfo, parents, len(graph) - 1, target)
    parents.append(len(graph) - 1)

    return parents