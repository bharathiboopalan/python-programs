# Stack
# -----
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


# Queue
# -----
class Queue:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def enqueue(self, item):
         self.items.append(item)

     def dequeue(self):
         return self.items.pop(0)

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

# Graph
# -----
class Graph:
    def __init__(self):
        self.matrix = {}

    # add a node to the graph
    def add_node(self, node):
        if not node in self.matrix:
            self.matrix[node] = {}

    # add an edge to the graph
    def add_edge(self, node1, node2):
        # create nodes if necessary
        self.add_node(node1)
        self.add_node(node2)

        self.matrix[node1][node2] = 1
        self.matrix[node2][node1] = 1

    # delete a node and all its edges
    def del_node(self, node):
        sibling_nodes = matrix[node]

        for n in sibling_nodes:
            del self.matrix[n][node]

        del self.matrix[node]

    # delete a single edge
    def del_edge(self, node1, node2):
        del self.matrix[node1][node2]
        del self.matrix[node2][node1]

    # check if an edge exists
    def has_edge(self, node1, node2):
        return self.has_node(node1) and node2 in self.matrix[node1]

    # check if a node exists
    def has_node(self, node):
        return node in self.matrix

