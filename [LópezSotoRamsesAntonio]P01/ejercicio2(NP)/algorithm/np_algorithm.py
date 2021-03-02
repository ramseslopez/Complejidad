from algorithm.graphs.graph import Graph
from algorithm.graphs.vertex import Vertex
import random

class NPAlgorithm():
    """
    Class where NP algorithm is applied 
    """

    def guessing_step(self, graph, num):
        """
        Guessing step of the algorithm

            Parameters:
                graph (grx): graph from which a Kn is obtain
                num (tr): number of vertexes

            Returns:
                graph2 (grx): nominee graph  
        """
        graph2 = Graph()
        vertexes = []
        random.shuffle(graph.vertexes)
        j = 0
        for v in graph.vertexes:
            if j < num:
                v.neighbors.clear()
                graph2.add(v)
                vertexes.append(v)
                j += 1
            else:
                break
        for v1 in vertexes:
            for v2 in vertexes:
                if not (v1.element == v2.element):
                        v1.neighbors.append(v2)
        print("Nominee " + str(graph2))
        return graph2


    def verification_step(self, graph, graph2):
        """
        Verification step of the algorithm

            Parameters:
                graph (grx): original graph
                graph2 (grx): graph of the guessingstep
        """
        boo = False
        for v1 in graph.vertexes:
            for v2 in graph2.vertexes:
                if v2.neighbors in v1.neighbors:
                    boo = True
        return boo


    def np_algorithm(self, graph, num):
        """
        NP- Algorithm

            Parameters:
                graph (grx): original graph

            Returns:
                stri (str): YES if the condition is satisfied, NO otherwise
        """
        graph_s = self.guessing_step(graph, num)
        ver_graph = self.verification_step(graph, graph)
        if ver_graph == False:
            return "NO"
        else: 
            return "YES"