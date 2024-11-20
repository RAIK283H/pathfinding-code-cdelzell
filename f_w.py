import pathing
import graph_data
import global_game_data

#Create an initial matrix given a graph with adjacency lists
def initialMatrix(graph):
    matrix = []

    for i in graph:
        arr = [None] * len(graph)
        for j in i[1]:
            distance = pathing.calculateDistance(i, graph[j])
            arr[j] = distance
        matrix.append(arr)
    
    return matrix

#Create an empty matrix given a graph with adjacency lists
def emptyMatrix(graph):
    matrix = []

    for i in graph:
        arr = [None] * len(graph)
        matrix.append(arr)
    
    return matrix

def globalFloydWarshall():
    # assert preconditions
    assert graph_data.graph_data is not None, "There is no graph data."
    assert global_game_data.current_graph_index is not None, "There is no graph index chosen."
    assert graph_data.graph_data[global_game_data.current_graph_index] is not None, "There is no graph chosen."

    graph = graph_data.graph_data[global_game_data.current_graph_index]
    target = global_game_data.target_node[global_game_data.current_graph_index]
    
    pathToTarget =  floydWarshall(graph, 0, target)
    targetToEnd = floydWarshall(graph, target, len(graph) - 1)
    targetToEnd = targetToEnd[1:]
    pathToTarget.extend(targetToEnd)

    return pathToTarget

#Get the path given a graph and the start and target nodes
def floydWarshall(graph, start, target):
    matrix = initialMatrix(graph)
    parentMatrix = emptyMatrix(graph)

    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                #implement null checks for matrix elements
                if matrix[i][k] is None or matrix[k][j] is None:
                    pass
                elif (matrix[i][k] is not None and matrix[k][j] is not None) and matrix[i][j] is None:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
                    parentMatrix[i][j] = k
                else:
                    if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                        matrix[i][j] = matrix[i][k] + matrix[k][j]
                        parentMatrix[i][j] = k
    
    #get the path from start to target
    path = getPath(parentMatrix, start, target)

    return path

#Get the path given a matrix of parents
def getPath(parents, start, target):
    path = []

    z = parents[start][target]

    if z == start:
        return [start, target]

    while z is not None:
        path.insert(0, z)
        z = parents[start][z]
    path.insert(0, start)
    path.append(target)

    return path

