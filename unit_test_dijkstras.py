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

        expected = [[0, 100000, None, False], [1, 100000, None, False], [2, 100000, None, False]]
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

    def test_appendNeighborNodes_with_one_neighbor(self):
        graph = [
        [(0, 0), [1]],
        [(10, 10), [0, 2]],
        [(20, 20), [1]]
        ]

        nodeInfo = [
            [0, 0, None, False], 
            [1, 1000, None, False], 
            [2, 1000, None, False]
        ]

        neighborNodes = [1]
        vertex = [0, 0, None, False]
        queue = []

        expected = [[1, 14.142135623730951, 0, False]]
        result = pathing.appendNeighborNodes(neighborNodes, nodeInfo, queue, vertex, graph)

        self.assertTrue(expected == result, result)


    def test_appendNeighborNodes_with_two_neighbors(self):
        graph = [
        [(0, 0), [1]],
        [(10, 10), [0, 2]],
        [(20, 20), [1]]
        ]

        nodeInfo = [
            [0, 0, None, False], 
            [1, 14.142135623730951, 0, False], 
            [2, 1000, None, False]
        ]

        neighborNodes = [0, 2]
        vertex = [1, 14.142135623730951, 0, False]
        queue = []

        expected = [[2, 28.284271247461902, 1, False]]
        result = pathing.appendNeighborNodes(neighborNodes, nodeInfo, queue, vertex, graph)

        self.assertTrue(expected == result, result)


    def test_appendNeighborNodes_with_no_neighbors(self):
        graph = [
        [(0, 0), [1]],
        [(10, 10), [0, 2]],
        [(20, 20), [1]]
        ]

        nodeInfo = [
            [0, 0, None, False], 
            [1, 14.142135623730951, 0, False], 
            [2, 28.284271247461902, 1, False]
        ]

        neighborNodes = [1]
        vertex = [2, 28.284271247461902, 1, False]
        queue = []

        expected = []
        result = pathing.appendNeighborNodes(neighborNodes, nodeInfo, queue, vertex, graph)

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

if __name__ == '__main__':
    unittest.main()