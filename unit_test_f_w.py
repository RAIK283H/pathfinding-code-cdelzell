import math
import unittest
import pathing
import global_game_data
import permutation
import graph_data
import f_w


class TestPathFinding(unittest.TestCase):

    def test_matrix(self):
        graph = [
        [(0, 0), [1]],
        [(10, 10), [0, 2, 3]],
        [(50, 20), [1, 3, 4]], 
        [(30, 30), [1, 2, 4]],
        [(40, 40), [3]]
        ]

        expected = [
                    [None, 14.142135623730951, None, None, None], 
                    [14.142135623730951, None, 41.23105625617661, 28.284271247461902, None], 
                    [None, 41.23105625617661, None, 22.360679774997898, 22.360679774997898], 
                    [None, 28.284271247461902, 22.360679774997898, None, 14.142135623730951], 
                    [None, None, None, 14.142135623730951, None]
                    ]
        result = f_w.initialMatrix(graph)

        self.assertTrue(expected == result, result)

    def test_emptyMatrix(self):
        graph = [
        [(0, 0), [1]],
        [(10, 10), [0, 2, 3]],
        [(50, 20), [1, 3, 4]], 
        [(30, 30), [1, 2, 4]],
        [(40, 40), [3]]
        ]

        expected = [
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None]
                    ]
        result = f_w.emptyMatrix(graph)

        self.assertTrue(expected == result, result)

    def test_floydWarshall(self):
        graph = [
        [(0, 0), [1]],
        [(10, 10), [0, 2, 3]],
        [(50, 20), [1, 3, 4]], 
        [(30, 30), [1, 2, 4]],
        [(40, 40), [3]]
        ]

        expected = [0, 1, 3, 4]
        result = f_w.floydWarshall(graph, 0, 4)

        self.assertTrue(expected == result, result)

    def test_floydWarshall_first_small_graph(self):
        graph = [
        [(0, 0), [1]],
        [(10, 10), [0, 2]],
        [(20, 20), [1, 3]],
        [(30, 30), [2, 4]],
        [(40, 40), [3]]
        ]

        expected = [0, 1, 2, 3, 4]
        result = f_w.floydWarshall(graph, 0, 4)

        self.assertTrue(expected == result, result)

    def test_floydWarshall_second_small_graph(self):
        graph = [
        [(0, 0), [1]],
        [(10, 10), [0, 2]],
        [(20, 20), [1, 3]],
        [(30, 30), [2, 4]],
        [(40, 40), [3]]
        ]

        expected = [0, 1, 2, 3, 4]
        result = f_w.floydWarshall(graph, 0, 4)

        self.assertTrue(expected == result, result)

    def test_floydWarshall_large_graph(self):
        graph = [
        [(150, 0), [1, 2]],
        [(130, 30), [0, 3]],
        [(170, 30), [0, 4]],
        [(120, 80), [1, 5]], 
        [(180, 80), [2, 6]],
        [(130, 160), [3, 7]], 
        [(170, 160), [4, 8]], 
        [(140, 120), [5, 9]], 
        [(160, 120), [6, 9]], 
        [(150, 100), [7, 8]],
        ]

        expected = [0, 1, 3, 5, 7, 9]
        result = f_w.floydWarshall(graph, 0, 9)

        self.assertTrue(expected == result, result)

    def test_floydWarshall_global_version(self):
        global_game_data.current_graph_index = 12
        global_game_data.target_node = [0,0,0,0,0,0,0,0,0,0,0,0,3]

        expected = [0, 1, 3, 4]
        result = f_w.globalFloydWarshall()

        self.assertTrue(expected == result, result)

    def test_getPath_happy_path(self):
        parents = [
        [None, None, 1, 2, 3],
        [None, None, None, 2, 3],
        [None, None, None, None, 3],
        [None, None, None, None, None],
        [None, None, None, None, None],
        ]

        expected = [0, 1, 2, 3, 4]
        result = f_w.getPath(parents, 0, 4)

        self.assertTrue(expected == result, result)

    def test_getPath_two(self):
        parents = [
        [None, 3, 3, 0, None,],
        [1, None, 3, 0, None, 3],
        [1, None, 3, None, 2],
        [1, 3, 3, None, None],
        [1, 3, 3, 4, None]
        ]

        expected = [0, 3]
        result = f_w.getPath(parents, 0, 3)

        self.assertTrue(expected == result, result)

if __name__ == '__main__':
    unittest.main()