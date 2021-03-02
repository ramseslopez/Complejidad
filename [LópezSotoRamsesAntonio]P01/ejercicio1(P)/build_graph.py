from algorithm.graphs.graph import Graph
from algorithm.graphs.vertex import Vertex
from algorithm.np_algorithm import NPAlgorithm
import random

class BuildGraph():
    
    def random_graph(self):
        """
        Builds a random graph

            Returs:
                graph (str): graph built with random values
        """
        num = random.randint(10, 20)
        graph = Graph()
        vertexes = []
        for i in range(1, num + 1):
            vertex = Vertex(i)
            graph.add(vertex)
        vertexes = graph.vertexes
        for v1 in vertexes:
            for v2 in vertexes:
                if v2 not in v1.neighbors:
                    b = bool(random.getrandbits(1))
                    if b and not(v1.element == v2.element):
                        v1.neighbors.append(v2)
        return graph

        

if __name__ == "__main__": 

    print("\nGenerator Tree")
    b = BuildGraph()
    np = NPAlgorithm()
    g = b.random_graph()
    print(g)
    alg = np.np_algorithm(g)
    print(alg)
