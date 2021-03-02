
class Vertex():
    """
    Vertex class
    """

    def __init__(self, element):
        """
        Initializes the vertex

            Parameters:
                element (int): number that represents to the vertex
        """
        self.element = element
        self.neighbors = []


    def get_element(self):
        """
        Gets the element of the vertex

            Returns:
                element (int): number that represents to the vertex
        """
        return str(self.element)

    def set_element(self, element):
        """
        Assings a new name to the vertex

            Parameters:
                element (int): new number of the vertex
        """
        self.element = element

    def get_neighbors(self):
        """
        Gets the vertexs neighbors

            Returns:
                neighbors (list): list of vertexs neighbors
        """
        return self.neighbors

    def has_neighbors(self):
        """
        Verifies if the vertex has neighbors

            Returns:
                 (bool): true if the vertex has neighbors, false otherwise
        """
        return len(self.neighbors) == 0

    def __str__(self):
        """
        Shows the string representation of the vertex

            Retunrs:
                vertexstr (str): vertex representation
        """
        nv = ""
        for i in range(0, len(self.neighbors)):
            nv += "[v" + str(self.neighbors[i].element) + "]"
        vertex_str = "[[v" + str(self.element) + "], neighbors:[" + nv + "]]" 
        return vertex_str

  