from vertex import Vertex

class Edge():

    def __init__(self, v1, v2, w):
        """
        Initializes the edge
        """
        self.v1 = v1
        self.v2 = v2
        self.weight = w

    def eq(self, edge):
        """
        Verifies if a vertex is equal to a edge endpont
        """
        if self.v1.element == edge.v1.element and self.v2.element == edge.v2.element:
            return True
        elif self.v1.element == edge.v2.element and self.v2.element == edge.v1.element:
            return True
        else:
            return False

    def get_weight(self):
        """
        Returns the weight
        """
        return self.weight
    
    def set_weight(self, weight):
        """
        Assigns a new weight
        """
        self.weight = weight

    def ed_to_lst(self, e):
        s = []
        s.append(e.v1.element)
        s.append(e.v2.element)
        return s
    
    def __lt__(self, e):
        return self.weight < e.weight
    

    def imprime(self):
        return "(v" + str(self.v1.element) + ", v" + str(self.v2.element) + "):" + "$" + str(self.weight)
    
