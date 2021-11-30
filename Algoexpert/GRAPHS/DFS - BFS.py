# O(v + E )| time
# O(V) | Space

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def addChild(self, name):
        self.children.append(Node(name))
        return self
#Recusive way

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            #print(array, child.name)
            child.depthFirstSearch(array)
        return array

# famous graph searching algorithm
# O(V+E) Time | O(V) Space
# we only loop through as many as edges we have and they we append the array names as many as vertices we have (TIME)
# we are storing only number of vertices
    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array





graph = Node("A")
graph.addChild("B").addChild("C")
graph.children[0].addChild("D").addChild("E")
print(graph.depthFirstSearch([]))
print(graph.breadthFirstSearch([]))
"""
graph.addChild("B").addChild("C").addChild("D")
graph.children[0].addChild("E").addChild("F")
graph.children[2].addChild("G").addChild("H")
graph.children[0].children[1].addChild("I").addChild("J")
graph.children[2].children[0].addChild("K")
print (graph.depthFirstSearch([]))
"""
"""
Time and space complexity

The time complexity can be expressed as O ( | V | + | E | ) {\displaystyle O(|V|+|E|)} O(|V|+|E|),
since every vertex and every edge will be explored in the worst case.
| V | {\displaystyle |V|} |V| is the number of vertices and | E | {\displaystyle |E|} |E| is the number of edges in the graph. 
Note that O ( | E | ) {\displaystyle O(|E|)} O(|E|) may vary between O ( 1 ) {\displaystyle O(1)} O(1) and 
O ( | V | 2 ) {\displaystyle O(|V|^{2})} O(|V|^{2}), depending on how sparse the input graph is.[9]

When the number of vertices in the graph is known ahead of time, and additional data structures are used to determine
which vertices have already been added to the queue, the space complexity can be expressed as O ( | V | ) {\displaystyle O(|V|)} O(|V|),
where | V | {\displaystyle |V|} |V| is the number of vertices. This is in addition to the space required for the graph itself, 
which may vary depending on the graph representation used by an implementation of the algorithm.
 
"""

"""'''Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. 
The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and 
explores as far as possible along each branch before backtracking. '''
"""