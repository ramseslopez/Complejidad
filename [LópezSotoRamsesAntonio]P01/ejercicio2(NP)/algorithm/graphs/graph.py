from algorithm.graphs.vertex import Vertex
import random

class Graph():

    def __init__(self):
        """
        Initializes th graph
        """
        self.vertexes = []
        self.edges = 0

    def get_vertexes(self):
        """
        The list of the vertexes

            Returns:
                vertexes (list): list of the vertexes
        """
        return self.vertexes

    def add(self, new_vertex):
        """
        Adds vertexes to the given graph

            Parameters:
                new vertex (vtrx): vertex representation which is added to graph´s vertexes
        """
        if new_vertex == None or self.contains(new_vertex):
            return
        else:
            self.vertexes.append(new_vertex)

    def contains(self, vertex):
       """
       Verifies if the element is in the graph

        Parameters:
            vertex (vrtx): vertex representation which is found
       """
       if vertex == None:
           raise ValueError("vértice inválido")
       else:
           return vertex in self.vertexes

    def _neighbors(self, vertex1, vertex2):
        """
        Verifies if two vertexes are neighbors

            Parameters:
                vertex1 (int): vertex that represents to the element
                vertex2 (int): vertex that represents to the element

            Returns:
                 (bool): true if v2 is in v1 neighbors, false otherwise
        """
        if vertex1 == None or vertex2 == None:
            raise ValueError("vértices no válidos")
        else:
            return vertex2 in vertex1.neighbors

    def connects(self, vertex1, vertex2):
        """
        Connects two vertexes

            Parameters:
                vertex1 (vrtx): vertex that represents to the element
                vertex2 (vrtx): vertex that represents to the element
        """
        if vertex1 == None or vertex2 == None:
            raise ValueError("vértice inválido")
        if self._neighbors(vertex1, vertex2):
            raise AttributeError("ya son vecinos")
        vertex1.neighbors.append(vertex2)
        vertex2.neighbors.append(vertex1)
        self.edges += 1

    def dfs(self, vertex, visited):
        """
        Performs DFS startig from a vertex

            Parameters:
                vertex (vrtx): vertex that represents to the element
                visited (list): visited vertexes
        """
        if vertex not in visited:
            visited.append(vertex)
            for n_vertex in vertex.neighbors:
                self.dfs(n_vertex, visited)

    def is_connected(self,vertex):
        """
        Verifies if the graph is connected

            Returns:
             (bool): true if the graph is connected, false otherwise
        """
        visited = []
        self.dfs(vertex,visited)
        num_visited = len(visited)
        return num_visited == len(self.vertexes)

    def edge_gen(self):
        """
        Shows an edge

            Returns:
                (tpl): edge between two vertexes.
        """
        lis = self.vertexes
        random.shuffle(lis)
        pr = lis[0]
        sg = lis[1]
        if pr.element > sg.element:
            return (pr, sg)
        else:
            return (sg, pr)

    def __str__(self):
        """
        Shows the string representation of the graph

            Retunrs:
                graph_str (str): graph representation
        """
        tr = ""
        for i in range(0, len(self.vertexes)):
            tr += str(self.vertexes[i]) + "\n"
        graph_str =  "Graph: \n" + tr 
        return graph_str
