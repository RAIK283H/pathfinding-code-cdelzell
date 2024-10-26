'''
graph_data[a] = gives you graph at index a
graph_data[a][0] = start node of graph a
graph_data[a][length-1] = exit node of graph a
graph_data[a][b][0] = x-y coordinates as tuple of point b in graph a
graph_data[a][b][1] = adjacency list of point b in graph a

Only the start and exit nodes are dead ends (all other nodes have degree >= 2)
'''


graph_data = [

    [
        [(0, 0), [1]],
        [(200, -200), [0, 2]],
        [(200, -400), [1]]
    ],
    [
        [(0, 0), [1]],
        [(50, -200), [0, 2]],
        [(50, -300), [1, 3]],
        [(200, -500), [2]]
    ],
    [
        [(900, 45), [17, 21, 22]],
        [(70, 350), [2, 7, 19, 20]],
        [(140, 420), [1, 5, 9, 10, 20]],
        [(210, 70), [6, 8, 11, 22]],
        [(210, 210), [6, 7, 11, 12, 20]],
        [(210, 490), [2, 10, 21]],
        [(280, 140), [3, 4, 11, 20]],
        [(280, 280), [1, 4, 9, 12, 20]],
        [(350, 70), [3, 11]],
        [(350, 350), [2, 7, 10, 12, 13, 15]],
        [(350, 490), [2, 5, 9, 13, 14, 15]],
        [(420, 140), [3, 4, 6, 8, 12, 16, 17]],
        [(420, 280), [4, 7, 9, 11, 15, 17]],
        [(420, 420), [9, 10, 15]],
        [(490, 490), [10, 18, 15]],
        [(560, 420), [9, 10, 12, 13, 14, 17, 18]],
        [(630, 70), [11, 17]],
        [(630, 210), [11, 12, 15, 16, 18, 0]],
        [(700, 420), [14, 15, 17, 23]],
        [(70, 500), [1, 21]],
        [(70, 210), [1, 2, 4, 6, 7, 22]],
        [(450, 700), [5, 19, 0, 23]],
        [(45, 45), [0, 3, 20]],
        [(1225, 700), [18, 21]]
    ],
    [
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
        [(300, 300), [14,11]],
    ],
    [
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
    ],
    [
        [(45, 45), [1]],
        [(100, 245), [14, 0, 2]],
        [(200, 245), [1, 5, 3]],
        [(300, 245), [2, 6, 10, 11, 12]],
        [(500, 345), [13, 6, 9]],
        [(200, 345), [14, 2, 6, 8]],
        [(300, 345), [9, 5, 4, 3]],
        [(100, 545), [8, 14]],
        [(200, 445), [5, 7, 9]],
        [(300, 445), [4, 6, 8, 15]],
        [(200, 145), [3, 11]],
        [(300, 145), [3, 10, 12]],
        [(400, 145), [3, 11, 13]],
        [(500, 145), [4, 12]],
        [(100, 345), [1, 7, 5]],
        [(1200, 700), [9]],
    ],
    [
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
    ],
    [
        [(0, 0), [1]],
        [(20, 20), [0, 3, 2]],
        [(20, 40), [1]],
        [(60, 60), [1, 4]],
        [(80, 80), [3, 6, 5]],
        [(80, 140), [4]], 
        [(100, 100), [4, 7]],
        [(120, 120), [6, 9, 8]],
        [(120, 80), [7]], 
        [(140, 140), [7, 11, 10]],
        [(140, 240), [9]], 
        [(160, 160), [9, 12]], 
        [(180, 180), [11, 14, 13]],
        [(180, 100), [12]], 
        [(200, 200), [12, 15]],
        [(220, 220), [14]]
    ],
    [
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
    ],
    [
        [(0, 0), [1, 20]],
        [(10, 25), [0, 2]],
        [(50, 70), [1, 3, 13]],
        [(100, 50), [2, 13, 12, 7, 4]],
        [(100, 20), [3, 7, 6, 5]],
        [(100, 10), [4, 6]],
        [(120, 10), [4, 5, 7, 8]],
        [(130, 70), [4, 6, 8, 11, 10, 3]],
        [(160, 60), [6, 7, 10, 9]],
        [(190, 90), [8, 10, 16, 19]],
        [(160, 100), [7, 8, 9, 11, 16]],
        [(130, 120), [3, 7, 10, 16, 15, 12]],
        [(110, 140), [3, 11, 15, 14, 13]],
        [(100, 160), [2, 3, 12, 14]],
        [(160, 170), [13, 12, 15, 17]],
        [(180, 150), [11, 12, 14, 16, 17]],
        [(200, 140), [10, 11, 15, 18, 19]],
        [(200, 170), [14, 15, 18]],
        [(220, 180), [17, 15, 16, 19]],
        [(220, 150), [16, 9, 18]],
        [(25, 100), [0, 21]],
        [(50, 150), [20, 22]],
        [(75, 170), [21, 23]],
        [(125, 220), [22, 24]],
        [(160, 240), [23, 25]],
        [(180, 260), [24, 26]],
        [(220, 300), [25]]
    ],
    [
        [(0, 0), [1]],
        [(10, 10), [0, 2]],
        [(20, 20), [1, 3]],
        [(30, 30), [2, 4]],
        [(40, 40), [3]]
    ],
    [
        [(0, 0), [1, 2]],
        [(10, 10), [0, 3]],
        [(20, 20), [0, 4]],
        [(30, 30), [1, 5]],
        [(40, 40), [2, 5]],
        [(50, 50), [3, 4]]
    ],
    [
        [(0, 0), [1]],
        [(10, 10), [0, 2, 3]],
        [(50, 20), [1, 3, 4]], 
        [(30, 30), [1, 2, 4]],
        [(40, 40), [3]]
    ]

]

test_path = [
    [1, 2],
    [1, 2, 3],
    [22, 3, 11, 17, 18, 23],
    [1, 5, 6, 10, 11, 15],
    [1, 2, 5, 8, 9, 10],
    [1, 14, 5, 6, 9, 15],
    [1, 2, 5, 10],
    [1, 3, 4, 6, 7, 9, 11, 12, 14, 15],
    [1, 3, 5, 7, 9],
    [1, 20, 21, 22, 23, 24, 25, 26],
    [1, 2, 3, 4], 
    [1, 3, 5],
    [1, 2, 4]
]
