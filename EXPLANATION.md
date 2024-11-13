**Random Pathing Algorithm:**

This algorithm keeps track of the current node and whether the target has been reached or not. If the target has not been reached, it will take a random node from the adjacency list of the current node and travel to that node. If this node is the target, it will update target\_reached to be true. After the target has been reached, the random algorithm will continue to draw random nodes and traveling to them until it gets to the end node, at which the path will end. If it visits the end node prior to reaching the target, it will simply continue to draw random nodes.

**Statistic:**

I added the “Vertices Visited Before Target” statistic. It relies on a method (update\_trips\_to\_target) that counts how many vertices were visited before the target was reached. This could be used in the future to test how efficient each algorithm is in reaching the target the quickest.

~also included the extra 25 node graph~

~Included A-Start functionality to the Dijkstra function for extra credit~