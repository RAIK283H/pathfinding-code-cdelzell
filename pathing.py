import graph_data
import global_game_data
from numpy import random

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

    for i in range(0, len(path) - 2):
        node_info = graph[path[i]]
        if(not(path[i+1] in node_info[1])) :
            return False
    
    return True

def get_dfs_path():
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]
