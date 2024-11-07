import math
import unittest
import pathing
import global_game_data
import permutation


class TestPathFinding(unittest.TestCase):

    def test_initializeNodeInfo_happypath(self):
        graph = [
        [(0, 0), [1]],
        [(10, 10), [0, 2]],
        [(20, 20), [1]]
        ]

        expected = [[0, 1000, None, False], [1, 1000, None, False], [2, 1000, None, False]]
        result = pathing.initializeNodeInfo(graph)

        self.assertTrue(expected == result, "The lists were not the same")

    def test_initializeNodeInfo_empty_graph(self):
        graph = []

        expected = []
        result = pathing.initializeNodeInfo(graph)

        self.assertTrue(expected == result, "The lists were not the same")

    def test_highestPriority_proper_index_result(self):
        queue = [[0, 50, None, False], [1, 10, None, False], [2, 1, None, False]]

        expected = [2, 1, None, False]
        result = pathing.highestPriority(queue)

        self.assertTrue(expected == result, "The vertices were not the same")

    def test_highestPriority_duplicate_index_result(self):
        queue = [[0, 50, None, False], [1, 1, None, False], [2, 1, None, False]]

        expected = [1, 1, None, False]
        result = pathing.highestPriority(queue)

        self.assertTrue(expected == result, "The vertices were not the same")

    def test_calculateDistance_between_indices_zero_and_one(self):
        graph = [
        [(0, 0), [1]],
        [(1, 0), [0, 2]],
        [(20, 20), [1]]
        ]

        expected = 1
        result = pathing.calculateDistance(graph[0], graph[1])

        self.assertTrue(expected == result, result)

    def test_calculateDistance_between_indices_zero_and_one(self):
        graph = [
        [(0, 0), [1]],
        [(10, 10), [0, 2]],
        [(20, 20), [1]]
        ]

        expected = 14.142135623730951
        result = pathing.calculateDistance(graph[0], graph[1])

        self.assertTrue(expected == result, result)

    def test_getPathToNode_shortPath(self):
        nodeInfo = [
            [0, 1000, None, False], 
            [1, 1000, 0, False], 
            [2, 1000, 1, False]
        ]

        expected = [0, 1]
        parents = []
        result = pathing.getPathToNode(nodeInfo, parents, 2, 0)

        self.assertTrue(expected == result, result)

    def test_getPathToNode_shortPath(self):
        nodeInfo = [
            [0, 1000, None, False], 
            [1, 1000, 0, False], 
            [2, 1000, 0, False],
            [3, 1000, 0, False],
            [4, 1000, 2, False] 
        ]

        expected = [0, 2]
        parents = []
        result = pathing.getPathToNode(nodeInfo, parents, 4, 0)

        self.assertTrue(expected == result, result)

    def test_getFullPath_shortPath(self):
        graph = [1, 2, 3, 4, 5]
        target = 3
        nodeInfo = [
            [0, 1000, None, False], 
            [1, 1000, 0, False], 
            [2, 1000, 0, False],
            [3, 1000, 0, False],
            [4, 1000, 2, False] 
        ]

        expected = [0, 3]
        parents = []
        result = pathing.getFullPath(graph, target, nodeInfo, parents)

        self.assertTrue(expected == result, result)

    def test_getFullPath_shortPath(self):
        graph = [
        [(0, 0), [1, 2]],
        [(10, 10), [0, 3]],
        [(20, 20), [0, 4]],
        [(30, 30), [1, 5]],
        [(40, 40), [2, 5]],
        [(50, 50), [3, 4]]
        ]
        target = 3
        nodeInfo = [
            [0, 1000, None, False], 
            [1, 1000, 0, False], 
            [2, 1000, 0, False],
            [3, 1000, 1, False],
            [4, 1000, 2, False],
            [5, 1000, 3, False], 
        ]

        expected = [0, 1, 3, 5]
        parents = []
        result = pathing.getFullPath(graph, target, nodeInfo, parents)

        self.assertTrue(expected == result, result)

if __name__ == '__main__':
    unittest.main()