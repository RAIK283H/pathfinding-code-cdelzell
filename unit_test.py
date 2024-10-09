import math
import unittest
import pathing
import global_game_data


class TestPathFinding(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('test'.upper(), 'TEST')

    def test_isupper(self):
        self.assertTrue('TEST'.isupper())
        self.assertFalse('Test'.isupper())

    def test_floating_point_estimation(self):
        first_value = 0
        for x in range(1000):
            first_value += 1/100
        second_value = 10
        almost_pi = 3.1
        pi = math.pi
        self.assertNotEqual(first_value,second_value)
        self.assertAlmostEqual(first=first_value,second=second_value,delta=1e-9)
        self.assertNotEqual(almost_pi, pi)
        self.assertAlmostEqual(first=almost_pi, second=pi, delta=1e-1)

    def test_check_adjacent_nodes_happy_path(self):
        graph = [
        [(0, 0), [1, 4]],
        [(0, 100), [0, 2, 5]],
        [(0, 200), [1, 3, 6]],
        [(0, 300), [2, 7]],
        [(100, 0), [5, 0, 8]],
        [(100, 100), [4, 6, 1, 9]],
        [(100, 200), [5, 7, 2, 10]],
        [(100, 300), [6, 3, 11]],
        [(200, 0), [9, 4, 12]],
        [(200, 100), [8, 10, 5, 13]],
        [(200, 200), [9, 11, 6, 14]],
        [(200, 300), [10, 7, 15]],
        [(300, 0), [13, 8]],
        [(300, 100), [12, 14, 9]],
        [(300, 200), [13, 15, 10]],
        [(300, 300), [14,11]]
        ]

        path = [0, 4, 8, 9, 10, 14]

        self.assertTrue(pathing.check_adjacent_nodes(path, graph)) 

    def test_check_adjacent_nodes_with_bad_path(self):
        graph = [
        [(0, 0), [1, 4]],
        [(0, 100), [0, 2, 5]],
        [(0, 200), [1, 3, 6]],
        [(0, 300), [2, 7]],
        [(100, 0), [5, 0, 8]],
        [(100, 100), [4, 6, 1, 9]],
        [(100, 200), [5, 7, 2, 10]],
        [(100, 300), [6, 3, 11]],
        [(200, 0), [9, 4, 12]],
        [(200, 100), [8, 10, 5, 13]],
        [(200, 200), [9, 11, 6, 14]],
        [(200, 300), [10, 7, 15]],
        [(300, 0), [13, 8]],
        [(300, 100), [12, 14, 9]],
        [(300, 200), [13, 15, 10]],
        [(300, 300), [14,11]]
        ]

        path = [0, 4, 8, 2, 10, 14]

        self.assertFalse(pathing.check_adjacent_nodes(path, graph))

    def test_check_adjacent_nodes_with_nonexistant_node(self):
        graph = [
        [(0, 0), [1, 4]],
        [(0, 100), [0, 2, 5]],
        [(0, 200), [1, 3, 6]],
        [(0, 300), [2, 7]],
        [(100, 0), [5, 0, 8]],
        [(100, 100), [4, 6, 1, 9]],
        [(100, 200), [5, 7, 2, 10]],
        [(100, 300), [6, 3, 11]],
        [(200, 0), [9, 4, 12]],
        [(200, 100), [8, 10, 5, 13]],
        [(200, 200), [9, 11, 6, 14]],
        [(200, 300), [10, 7, 15]],
        [(300, 0), [13, 8]],
        [(300, 100), [12, 14, 9]],
        [(300, 200), [13, 15, 10]],
        [(300, 300), [14,11]]
        ]

        path = [0, 2, 8, 2, 10, 20, 14]

        self.assertFalse(pathing.check_adjacent_nodes(path, graph))

    def test_dfs_path_creation_happy_path(self):
        graph = [
        [(45, 45), [1]],
        [(100, 245), [0, 2, 4]],
        [(200, 245), [1, 3, 5]],
        [(300, 145), [2, 6]],
        [(100, 345), [1, 5, 7]],
        [(200, 345), [2, 4, 6, 8]],
        [(300, 345), [3, 9]],
        [(100, 545), [4, 8]],
        [(200, 445), [5, 7, 9]],
        [(300, 445), [6, 8, 10]],
        [(1200, 700), [9]]
        ]

        expectedPath = [0, 1, 2]
        resultPath = pathing.dfs_path_creation(graph, 0, 2)

        self.assertTrue(expectedPath == resultPath)

    def test_dfs_path_creation_non_origin_start_node(self):
        graph = [
        [(0, 0), [1, 3]],
        [(30, 40), [0, 2]],
        [(70, 80), [1, 4, 5]],
        [(10, 100), [0]], 
        [(150, 200), [2, 5, 8]],
        [(120, 50), [2, 4, 6, 10]], 
        [(100, 150), [5, 7, 9]], 
        [(200, 40), [6, 9]], 
        [(125, 125), [4]], 
        [(200, 100), [6, 7]],
        [(150, 10), [5]]
        ]

        expectedPath = [8, 4, 2, 5, 10]
        resultPath = pathing.dfs_path_creation(graph, 8, 10)

        self.assertTrue(expectedPath == resultPath)

    def test_dfs_path_creation_same_start_and_target(self):
        graph = [
        [(0, 0), [1, 3]],
        [(30, 40), [0, 2]],
        [(70, 80), [1, 4, 5]],
        [(10, 100), [0]], 
        [(150, 200), [2, 5, 8]],
        [(120, 50), [2, 4, 6, 10]], 
        [(100, 150), [5, 7, 9]], 
        [(200, 40), [6, 9]], 
        [(125, 125), [4]], 
        [(200, 100), [6, 7]],
        [(150, 10), [5]]
        ]

        expectedPath = [8]
        resultPath = pathing.dfs_path_creation(graph, 8, 8)

        self.assertTrue(expectedPath == resultPath)

    def test_get_dfs_path_happy_path(self):
        global_game_data.current_graph_index = 6
        global_game_data.target_node = [0, 0, 0, 0, 0, 0, 8]

        expectedPath = [0, 1, 2, 4, 8, 4, 2, 5, 10]
        resultPath = pathing.get_dfs_path()

        self.assertTrue(expectedPath == resultPath, resultPath)

    def test_get_dfs_path_happy_path_two(self):
        global_game_data.current_graph_index = 5
        global_game_data.target_node = [0, 0, 0, 0, 0, 1]


        expectedPath = [0, 1, 14, 7, 8, 5, 2, 3, 6, 9, 15]
        resultPath = pathing.get_dfs_path()

        self.assertTrue(expectedPath == resultPath, resultPath)


    def test_bfs_path_creation_happy_path(self):
        graph = [
        [(45, 45), [1]],
        [(100, 245), [0, 2, 4]],
        [(200, 245), [1, 3, 5]],
        [(300, 145), [2, 6]],
        [(100, 345), [1, 5, 7]],
        [(200, 345), [2, 4, 6, 8]],
        [(300, 345), [3, 9]],
        [(100, 545), [4, 8]],
        [(200, 445), [5, 7, 9]],
        [(300, 445), [6, 8, 10]],
        [(1200, 700), [9]]
        ]

        expectedPath = [0, 1, 2]
        resultPath = pathing.bfs_path_creation(graph, 0, 2)

        self.assertTrue(expectedPath == resultPath)

    def test_bfs_path_creation_non_origin_start_node(self):
        graph = [
        [(0, 0), [1, 3]],
        [(30, 40), [0, 2]],
        [(70, 80), [1, 4, 5]],
        [(10, 100), [0]], 
        [(150, 200), [2, 5, 8]],
        [(120, 50), [2, 4, 6, 10]], 
        [(100, 150), [5, 7, 9]], 
        [(200, 40), [6, 9]], 
        [(125, 125), [4]], 
        [(200, 100), [6, 7]],
        [(150, 10), [5]]
        ]

        expectedPath = [8, 4, 5, 10]
        resultPath = pathing.bfs_path_creation(graph, 8, 10)
        print(resultPath)

        self.assertTrue(expectedPath == resultPath)

    def test_bfs_path_creation_same_start_and_target(self):
        graph = [
        [(0, 0), [1, 3]],
        [(30, 40), [0, 2]],
        [(70, 80), [1, 4, 5]],
        [(10, 100), [0]], 
        [(150, 200), [2, 5, 8]],
        [(120, 50), [2, 4, 6, 10]], 
        [(100, 150), [5, 7, 9]], 
        [(200, 40), [6, 9]], 
        [(125, 125), [4]], 
        [(200, 100), [6, 7]],
        [(150, 10), [5]]
        ]

        expectedPath = [8]
        resultPath = pathing.bfs_path_creation(graph, 8, 8)

        self.assertTrue(expectedPath == resultPath)

    def test_get_bfs_path_happy_path(self):
        global_game_data.current_graph_index = 6
        global_game_data.target_node = [0, 0, 0, 0, 0, 0, 7]

        expectedPath = [0, 1, 2, 5, 6, 7, 6, 5, 10]
        resultPath = pathing.get_bfs_path()

        self.assertTrue(expectedPath == resultPath, resultPath)

    def test_get_bfs_path_happy_path_two(self):
        global_game_data.current_graph_index = 2
        global_game_data.target_node = [0, 0, 5]


        expectedPath = [0, 21, 5, 21, 23]
        resultPath = pathing.get_bfs_path()

        self.assertTrue(expectedPath == resultPath, resultPath)



if __name__ == '__main__':
    unittest.main()
