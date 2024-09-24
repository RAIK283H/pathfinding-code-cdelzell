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


def get_random_path():
    return create_random_path()[0]

def create_random_path() :
    ##goes to random nodes
    ##keeps track of if it has hit the target
    ##if it has hit the target and is at the end node, it can exit
    ##otherwise, it will just keep going
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    start_node = graph[0]
    target = global_game_data.target_node[global_game_data.current_graph_index]
    target_reached = False
    end_node = graph[len(graph) - 1]
    current_node = start_node
    count_to_reach_target = 0
    path = [0]


    while(not target_reached or current_node != end_node) :
        options = current_node[1]
        random_choice = random.choice(options)
        path.append(int(random_choice))
        current_node = graph[path[len(path) - 1]]
        count_to_reach_target += 1

        if(random_choice == target) :
            target_reached = True
            print(target_reached is True and current_node == end_node)
        if(target_reached is True and current_node == end_node) :
            return path, count_to_reach_target
    
    return []



def get_dfs_path():
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]
