from algorithm.graphs.graph import Graph
from algorithm.graphs.vertex import Vertex

class NPAlgorithm():
    """
    Class where NP algorithm is applied 
    """

    def guessing_step(self, graph):
        """
        Guessing strp of the algorithm

            Parameters:
                graph (grx): graph from which a tree is obtain

            Returns:
                tree (tr): tree build from a graph 
        """
        tree_ = self.tree(graph)
        print("Nominee:\n" + self.st(tree_) + "\n")
        return tree_

    def verification_step(self, graph, tree):
        """
        Verification step of the algorithm

            Parameters:
                graph (grx): original graph
                tree (tree): tree from guessin step

            Returns:
                 (bool): true if condition is satisfied, false otherwise
        """
        boo = self.verification_step_aux2(tree)
        boo_ = self.vertex_tree(graph, tree)
        return boo and boo_


    def np_algorithm(self, graph):
        """
        NP- Algorithm

            Parameters:
                graph (grx): oriinal graph

            Returns:
                stri (str): YES if the condition is satisfied, NO otherwise
        """
        tree_ = self.guessing_step(graph)
        ver_tree = self.verification_step(graph, tree_)
        if ver_tree == False:
            return "NO"
        else: 
            return "YES"
        

    def tree(self, graph):
        """
        Builds a tree

            Parameters:
                graph (grx): original graph

            Returns:
                tree (tr): gererated tree
        """
        tree = []
        while len(tree) != len(graph.vertexes) - 1:
            a = graph.edge_gen()
            if self.contains_edge(a, tree):
                pass
            else: 
                tree.append(a)
        return tree

    def contains_edge(self, edge, edges):
        """
        Verifies if a edge is in a edges list

            Parameters:
                edge (ed): edges to find
                edges (list): list of edges

            Returns:
                 (bool): true if edge is in edges, false otherwise
        """
        if edge == None:
            return
        else:
            return edge in edges

    def vertex_tree(self, graph, lists):
        """
        Verifies if a graph vertex is in egdes list
        """
        boo = True
        for v in graph.vertexes:
            var = self.vertex_edge_1(v, lists)
            if var == False:
                boo = False
                break
        return boo

    def vertex_edge_1(self, vertex, edges_list):
        """
        Verifies if a vertex  is in edges list
        """
        boo = True
        for e in edges_list:
                if not (vertex.element == e[0] or vertex.element == e[1]):
                    boo = False
                    break
        return boo

    def verification_step_aux(self, edge):
        """
        Auxiliar method
        """
        boo = False
        for a in edge[0].neighbors:
             if a.element == edge[0].element:
                 boo = True
                 break
        return boo

    def verification_step_aux2(self, edges_list):
        """
        Auxiliar method
        """
        boo = True
        for e in edges_list:
            val = self.verification_step_aux(e)
            if not val == False:
                boo = False
                break
        return boo

    
    def st(self, e_list):
        """
        Shows a edges list

            Parameters:
                e_list (list): edges list

            Returns:
                st (str): string representation of egdes
        """
        st ="["
        for n in e_list:
            st += "(" + str(n[0].element) + "," + str(n[1].element) + ")"
        st += "]"
        return st