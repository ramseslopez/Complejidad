from vertex import Vertex
from edge import Edge
from graph import Graph

class TSP():

    def prim(self, graph):
        """
        Builds the minimum spanning tree

            Parameters:
                graph (grx): an inpunt graph

            Returns:
                tree (list): the mininum spannin tree
        """
        tree = []
        ls = [graph.vertexes[0]]
        while len(tree) != len(graph.vertexes)-1:
            arr = self.vtx(ls, graph.edges)
            for e in arr:
                if not self.f_edge(tree, e) and self.new(ls, e):
                    tree.append(e)
                    if not self.exists(ls, e.v1):
                        ls.append(e.v1)
                    elif not self.exists(ls, e.v2):
                        ls.append(e.v2)
                    break
        return tree


    def edges_end(self, list_e, v):
        """
        Gets the endpoint vertes of edges list

            Parameters:
                list_e (list): edges list
                v (vtx): a vertex

            Returns:
                lst (list): edges list
        """
        lst = []
        for e in list_e:
            if v.element == e.v1.element:
                lst.append(e)
            elif v.element == e.v2.element:
                lst.append(e)
        return lst

    def vtx(self, list_v, list_e):
        """
        Gets an endpoints list

            Parameters:
                list_v (list): vertexes list
                list_e (list): edges list

            Returns:
                lst (list): an ordered endpoints list
        """
        lst = []
        for v in list_v:
            lst += self.edges_end(list_e, v)
        lst.sort()
        return lst

    def endpoint(self, vertex , edge):
        """
        Verifies if a vetex is edge's endpoint

            Parameters:
                vertex (vtx): a vertex
                edge (edg): an edge

            Returns:
                 (bool): True if so, False otherwise
        """
        if edge.v1.element == vertex.element or edge.v2.element == vertex.element:
            return True
        return False

    def f_edge(self, list_e, e):
        """
        Finds an edge in a edges list

            Parameters:
                list_e (list): edges list
                e (edg): an edge

            Returns:
                 (bool): True if so, False otherwise
        """
        for d in list_e:
            if e.v1.element == d.v1.element and e.v2.element == d.v2.element:
                return True
        return False

    def exists(self, list_v, vertex):
        """
        Finds a vertes in a vertexes list

            Parameters:
                list_v (list): vertexes list
                vertex (vtx): a vertex

            Returns:
                 (bool): True if so, False otherwise
        """
        for v in list_v:
            if v.element == vertex.element:
                return True
        return False


    def new(self, list_v, e):
        """
        Verifies if a edge's endpoint is in a vertexes list

            Parameters:
                list_v (list): vertexes list
                e (edg): an edge

            Returns:
                 (bool): True if so, False otherwise
        """
        return not self.exists(list_v, e.v1) or not self.exists(list_v, e.v2)

    def ed_to_lst(self, e):
        """
        Adds the elements edge's endpoints in a int list

            Parameters:
                e (edg): an edge
            
            Returns:
                s (list): int list
        """
        s = []
        s.append(e.v1.element)
        s.append(e.v2.element)
        return s

    def odd_vertex(self, tree):
        """
        Gets the tree's odd vertex list 

            Parameters:
                tree (list): edges list

            Returns:
                m (list): odd vertex list
        """
        el = []
        for t in tree: 
            el += self.ed_to_lst(t) 
        el.sort()
        arr = []
        for elm in el:
            if el.count(elm)%2 != 0:
                arr.append(elm)
        m = list(set(arr))
        m.sort()
        return m

    def vetex(self, vertexes, listi):
        """
        Adds vertexes into a list

            Parameters:
                vetexes (list): vertexes list
                listi (list): int list

            Returns:
                s (list): vertexes list
        """
        s = []
        for v in vertexes:
            if v.element in listi:
                s.append(v)
        return s

    #def remove_even_vertex(self, graph):
        #es = self.prim(graph)
        #w = self.even_vertex(es)
        #for i in range(len(graph.get_vertexes()) - 1, - 1, - 1):
            #for j in range(len(graph.get_edges()) - 1, - 1, -1):
            #        if self.endpoint(graph.vertexes[i], graph.edges[j]):
            #            graph.edges.pop(j)
            #        if graph.vertexes[i].element in w:
            #            graph.vertexes.pop(i)
        #for v in graph.get_vertexes():
        #    print("-v" + str(v.element))
        #    if v.element in w:
        #        print("v"+str(v.element))
        #        graph.vertexes.remove(v)
        #        for e in graph.edges:
        #            if self.endpoint(v, e):
        #                graph.edges.remove(e)
        #return graph

    #def remove_even_edge(self, graph):
    #    es = self.prim(graph)
    #    w = self.even_vertex(es)
    #    for i in range(len(graph.edges) - 1, - 1):
    #        if graph.edges[i].v1.element or graph.edges[i].v2.element in w:
    #            graph.edges.pop(i)
    #    return graph 

    def build_new_graph(self, graph):
        """
        Builds a new graph

            Parameters:
                graph (grx): an input graph

            Returns:
                graph (grx): a result graph
        """
        g = Graph()
        es = self.prim(graph)
        w = self.odd_vertex(es)
        for i in w:
            v = Vertex(i)
            g.add(v)
            for e in graph.edges:
                if e.v1.element in w and e.v2.element in w:
                    g.add_edge(e)
        for v1 in g.vertexes:
            for v2 in g.vertexes:
                if v2 not in v1.neighbors:
                    v1.neighbors.append(v2)
        return g

    def matching(self, graph):
        """
        Builds a matching

            Parameters:
                graph (grx): an input graph

            Returns:
                ls (list): edges list
        """
        s = graph.get_edges()
        s.sort()
        vtx = []
        ls = []
        for e in s:
            if not e.v1.element in vtx and not e.v2.element in vtx:
                ls.append(e)
                vtx.append(e.v1.element)
                vtx.append(e.v2.element)
        return ls

    def matching_u_tree(self, match, tree):
        """
        Unifies a match and a tree

            Parameters:
                match (list): a matching
                tree (list): a minimun spanning tree
            
            Returns:
                mut (list): an ordered list
        """
        mut = match + tree
        mut.sort()
        return mut

    def print_edges(self, edges):
        s = "["
        for e in edges:
            s += e.__str__()
        s += "]"
        return s