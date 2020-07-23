"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if self.vertices.get(v1) == None or self.vertices.get(v2) == None:
            raise IndexError(f"{v1} is not in the graph, bruh. try running add_vertex({v1} first.) ")
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if self.vertices.get(vertex_id) == None:
            raise IndexError(f"{vertex_id} is not in the graph, mah dood.")
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #instantiate queue and define starting vertex. 
        q = Queue()
        q.enqueue(starting_vertex)
        #create a way to track visted vertices.
        visited = []
        #print initial node
        print(f"BFT")
        print(f"{starting_vertex}")

        while q.size() > 0:
            #pop current node off the queue and add it to visited
            current_node = q.dequeue()
            visited.append(current_node)
            #check the node for neighbors.
            for i in self.get_neighbors(current_node):
                #if neighbors were visited skip it.
                #if they werent, add to the queue and to visited.
                if not i in visited:
                    if i is not None:
                        q.enqueue(i)
                        visited.append(i)
                    print(f"{i}")

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #instantiate stack and define starting vertex. 
        st = Stack()
        st.push(starting_vertex)
        #create a way to track visted vertices.
        visited = []
        #print initial node
        print(f"DFT")

        while st.size() > 0:
            #pop current node off the stack and add it to visited
            current_node = st.pop()
            visited.append(current_node)
            #check the node for neighbors.
            for i in self.get_neighbors(current_node):
                #if neighbors were visited skip it.
                #if they werent, add to the stack and to visited.
                if not i in visited:
                    st.push(i)
                    visited.append(i)
            print(f"{current_node}")

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        #when we reach the end, return up the chain
        if not starting_vertex:
            return
        #first pass? if so, instantiate the list, and print title
        if not visited:
            visited=[starting_vertex]
            print('Recursive DFT')
        #if not, add node to visited 
        else:
            visited.append(starting_vertex)
        #print node
        print(starting_vertex)
        #if passed in node's neighbors are not in visited, call recursive DFT on them
        for i in self.vertices.get(starting_vertex):
            if not i in visited:
                self.dft_recursive(i, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
         #instantiate queue and define starting vertex. 
        q = Queue()
        q.enqueue(starting_vertex)
        #create a way to track visted vertices.
        visited = []
        #create a way to track the overall path
        current_path = {
            starting_vertex: '1',
        }
        print(f"breadth first search")
        while q.size() > 0:
            #pop current node off the queue and add it to visited
            current_node = q.dequeue()
            #are we done searching?
            if current_node == destination_vertex:
                #start with an empty string
                path = f''
                #loop through the current path and generate overall path
                while current_path.get(current_node) is not '1':
                    path = f'{current_node} {path}'
                    current_node = current_path.get(current_node)
                #return the result
                return f'{starting_vertex} {path}'
            #if not done searching,
            else:
                #check the node for neighbors.
                for i in self.get_neighbors(current_node):
                    #enqueue the neighbors, assuming we havent visited
                    if i not in visited:
                        q.enqueue(i)
                        visited.append(i)
                    #if you havent reached the end or the target, mark your progress
                    if not current_path.get(i):
                        current_path[i] = current_node

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        #instantiate stack and define starting vertex. 
        st = Stack()
        st.push(starting_vertex)
        #create a way to track visted vertices.
        visited = []
        #create a way to track the overall path
        current_path = {
            starting_vertex: '1',
        }
        print(f"depth first search")

        while st.size() > 0:
            #pop current node off the stack and add it to visited
            current_node = st.pop()
            #are we done searching?
            if current_node == destination_vertex:
                #start with an empty string
                path = f''
                #loop through the current path and generate overall path
                while current_path.get(current_node) is not '1':
                    path = f'{current_node} {path}'
                    current_node = current_path.get(current_node)
                #return the result
                return f'{starting_vertex} {path}'
            #if not done searching,
            else: 
                #check the node for neighbors.
                for i in self.get_neighbors(current_node):
                    if not i in visited:
                        st.push(i)
                        visited.append(i)
                    if not current_path.get(i):
                        current_path[i] = current_node

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        
        if starting_vertex == destination_vertex:
            return path
        
        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                new_path = self.dfs_recursive(child_vert, destination_vertex, visited, path)
                if new_path:
                    return new_path
        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
