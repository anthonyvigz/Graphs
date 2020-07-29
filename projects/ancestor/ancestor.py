class Queue:
    def __init__(self):
        self.storage = []

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.storage.pop(0)
        else:
            return None

    def size(self):
        return len(self.storage)

class Graph:
    """ 
        Represent a graph as a dictionary of verts 
        mapping labels to edges 
    """
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
    
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise KeyError("That vertex does not exist!")
        
def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        graph.add_edge(pair[1], pair[0])
    q = Queue()
    q.enqueue([starting_node])
    max_path_length = 1
    earliest_ancestor = -1
    while q.size() > 0:
        path = q.dequeue()
        vert = path[-1]
        if (len(path) >= max_path_length and vert < earliest_ancestor) or (len(path) > max_path_length):
            earliest_ancestor = vert
            max_path_length = len(path)
        for neighbor in graph.vertices[vert]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)
    return earliest_ancestor