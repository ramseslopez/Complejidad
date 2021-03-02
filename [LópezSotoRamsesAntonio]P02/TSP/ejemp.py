from tsp import TSP
from edge import Edge
from vertex import Vertex
from graph import Graph

if __name__ == "__main__":
    g = Graph()
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    v4 = Vertex(4)
    v5 = Vertex(5)
    v6 = Vertex(6)
    v7 = Vertex(7)
    v8 = Vertex(8)
    v9 = Vertex(9)
    v10 = Vertex(10)

    g.add(v1)
    g.add(v2)
    g.add(v3)
    g.add(v4)
    g.add(v5)
    g.add(v6)
    g.add(v7)
    g.add(v8)
    g.add(v9)
    g.add(v10)

    v1.neighbors.append(v2)
    v1.neighbors.append(v3)
    v1.neighbors.append(v4)
    v1.neighbors.append(v5)
    v1.neighbors.append(v6)
    v1.neighbors.append(v7)
    v1.neighbors.append(v8)
    v1.neighbors.append(v9)
    v1.neighbors.append(v10)

    v2.neighbors.append(v1)
    v2.neighbors.append(v3)
    v2.neighbors.append(v4)
    v2.neighbors.append(v5)
    v2.neighbors.append(v6)
    v2.neighbors.append(v7)
    v2.neighbors.append(v8)
    v2.neighbors.append(v9)
    v2.neighbors.append(v10)

    v3.neighbors.append(v1)
    v3.neighbors.append(v2)
    v3.neighbors.append(v4)
    v3.neighbors.append(v5)
    v3.neighbors.append(v6)
    v3.neighbors.append(v7)
    v3.neighbors.append(v8)
    v3.neighbors.append(v9)
    v3.neighbors.append(v10)

    v4.neighbors.append(v1)
    v4.neighbors.append(v2)
    v4.neighbors.append(v3)
    v4.neighbors.append(v5)
    v4.neighbors.append(v6)
    v4.neighbors.append(v7)
    v4.neighbors.append(v8)
    v4.neighbors.append(v9)
    v4.neighbors.append(v10)

    v5.neighbors.append(v1)
    v5.neighbors.append(v2)
    v5.neighbors.append(v3)
    v5.neighbors.append(v4)
    v5.neighbors.append(v6)
    v5.neighbors.append(v7)
    v5.neighbors.append(v8)
    v5.neighbors.append(v9)
    v5.neighbors.append(v10)

    v6.neighbors.append(v1)
    v6.neighbors.append(v2)
    v6.neighbors.append(v3)
    v6.neighbors.append(v4)
    v6.neighbors.append(v5)
    v6.neighbors.append(v7)
    v6.neighbors.append(v8)
    v6.neighbors.append(v9)
    v6.neighbors.append(v10)

    v7.neighbors.append(v1)
    v7.neighbors.append(v2)
    v7.neighbors.append(v3)
    v7.neighbors.append(v4)
    v7.neighbors.append(v5)
    v7.neighbors.append(v6)
    v7.neighbors.append(v8)
    v7.neighbors.append(v9)
    v7.neighbors.append(v10)

    v8.neighbors.append(v1)
    v8.neighbors.append(v2)
    v8.neighbors.append(v3)
    v8.neighbors.append(v4)
    v8.neighbors.append(v5)
    v8.neighbors.append(v6)
    v8.neighbors.append(v7)
    v8.neighbors.append(v9)
    v8.neighbors.append(v10)

    v9.neighbors.append(v1)
    v9.neighbors.append(v2)
    v9.neighbors.append(v3)
    v9.neighbors.append(v4)
    v9.neighbors.append(v5)
    v9.neighbors.append(v6)
    v9.neighbors.append(v7)
    v9.neighbors.append(v8)
    v9.neighbors.append(v10)

    v10.neighbors.append(v1)
    v10.neighbors.append(v2)
    v10.neighbors.append(v3)
    v10.neighbors.append(v4)
    v10.neighbors.append(v5)
    v10.neighbors.append(v6)
    v10.neighbors.append(v7)
    v10.neighbors.append(v8)
    v10.neighbors.append(v9)

    print("Choose a number")
    print("1                      2                      3                      4                      5")

    inp = int(input("input a number> "))

    if inp == 1:
        e1 = Edge(v1, v2, 2)
        e2 = Edge(v1, v3, 3)
        e3 = Edge(v1, v4, 2)
        e4 = Edge(v1, v5, 3)
        e5 = Edge(v1, v6, 2)
        e6 = Edge(v1, v7, 3)
        e7 = Edge(v1, v8, 2)
        e8 = Edge(v1, v9, 3)
        e9 = Edge(v1, v10, 2)
        e10 = Edge(v2, v3, 3)
        e11 = Edge(v2, v4, 2)
        e12 = Edge(v2, v5, 3)
        e13 = Edge(v2, v6, 2)
        e14 = Edge(v2, v7, 3)
        e15 = Edge(v2, v8, 2)
        e16 = Edge(v2, v9, 3)
        e17 = Edge(v2, v10, 2)
        e18 = Edge(v3, v4, 3)
        e19 = Edge(v3, v5, 2)
        e20 = Edge(v3, v6, 3)
        e21 = Edge(v3, v7, 2)
        e22 = Edge(v3, v8, 3)
        e23 = Edge(v3, v9, 2)
        e24 = Edge(v3, v10, 3)
        e25 = Edge(v4, v5, 2)
        e26 = Edge(v4, v6, 3)
        e27 = Edge(v4, v7, 2)
        e28 = Edge(v4, v8, 3)
        e29 = Edge(v4, v9, 2)
        e30 = Edge(v4, v10, 3)
        e31 = Edge(v5, v6, 2)
        e32 = Edge(v5, v7, 3)
        e33 = Edge(v5, v8, 2)
        e34 = Edge(v5, v9, 3)
        e35 = Edge(v5, v10, 2)
        e36 = Edge(v6, v7, 3)
        e37 = Edge(v6, v8, 2)
        e38 = Edge(v6, v9, 3)
        e39 = Edge(v6, v10, 2)
        e40 = Edge(v7, v8, 3)
        e41 = Edge(v7, v9, 2)
        e42 = Edge(v7, v10, 3)
        e43 = Edge(v8, v9, 2)
        e44 = Edge(v8, v10, 3)
        e45 = Edge(v9, v10, 2)

        g.add_edge(e1)
        g.add_edge(e2)
        g.add_edge(e3)
        g.add_edge(e4)
        g.add_edge(e5)
        g.add_edge(e6)
        g.add_edge(e7)
        g.add_edge(e8)
        g.add_edge(e9)
        g.add_edge(e10)
        g.add_edge(e11)
        g.add_edge(e12)
        g.add_edge(e13)
        g.add_edge(e14)
        g.add_edge(e15)
        g.add_edge(e16)
        g.add_edge(e17)
        g.add_edge(e18)
        g.add_edge(e19)
        g.add_edge(e20)
        g.add_edge(e21)
        g.add_edge(e22)
        g.add_edge(e23)
        g.add_edge(e24)
        g.add_edge(e25)
        g.add_edge(e26)
        g.add_edge(e27)
        g.add_edge(e28)
        g.add_edge(e29)
        g.add_edge(e30)
        g.add_edge(e31)
        g.add_edge(e32)
        g.add_edge(e33)
        g.add_edge(e34)
        g.add_edge(e35)
        g.add_edge(e36)
        g.add_edge(e37)
        g.add_edge(e38)
        g.add_edge(e39)
        g.add_edge(e40)
        g.add_edge(e41)
        g.add_edge(e42)
        g.add_edge(e43)
        g.add_edge(e44)
        g.add_edge(e45)

        print(g)

        q = g.p_edges()

        print("edges \n" + q)

        print("num_edges " + str(len(g.edges)) + "\n")

        tsp = TSP()
        t = tsp.prim(g)
        s = "["
        suma  = 0
        for e in t:
            s += "(v" + str(e.v1.element) + ", v" + str(e.v2.element) + "):$" + str(e.weight) + ","
            suma += e.weight
        s += "] -> $" + str(suma)
        print("gen_tree " + str(s) + "\n")

        a = tsp.odd_vertex(t)

        print("odd_vertex "+ str(a) + "\n")

        ger = tsp.build_new_graph(g)

        print("Induced " + str(ger))

        r = "["
        for e in ger.edges:
            r += "(v" + str(e.v1.element) + ", v" + str(e.v2.element) + "):$" + str(e.weight) + ","
        r += "]" 

        print("edges \n" + r + "\n")

        print("num_edges " + str(len(ger.edges)) + "\n")

        ss = tsp.matching(ger)
        aa = "["
        for a in ss:
            aa += "(v" + str(a.v1.element) + ", v" + str(a.v2.element) + "):$" + str(a.weight) + ", "
        aa += "]"
        print("matching \n" + aa + 
        "\n")

        mut = tsp.matching_u_tree(t, ss)

        h = "["
        for a in mut:
            h += "(v" + str(a.v1.element) + ", v" + str(a.v2.element) + "):$" + str(a.weight) + ", "
        h += "]"

        print("union \n" + h + "\n")
    elif inp == 2:
        e1 = Edge(v1, v2, 502)
        e2 = Edge(v1, v3, 523)
        e3 = Edge(v1, v4, 534)
        e4 = Edge(v1, v5, 522)
        e5 = Edge(v1, v6, 588)
        e6 = Edge(v1, v7, 545)
        e7 = Edge(v1, v8, 566)
        e8 = Edge(v1, v9, 512)
        e9 = Edge(v1, v10, 578)
        e10 = Edge(v2, v3, 523)
        e11 = Edge(v2, v4, 520)
        e12 = Edge(v2, v5, 560)
        e13 = Edge(v2, v6, 550)
        e14 = Edge(v2, v7, 555)
        e15 = Edge(v2, v8, 582)
        e16 = Edge(v2, v9, 543)
        e17 = Edge(v2, v10, 535)
        e18 = Edge(v3, v4, 579)
        e19 = Edge(v3, v5, 531)
        e20 = Edge(v3, v6, 534)
        e21 = Edge(v3, v7, 562)
        e22 = Edge(v3, v8, 580)
        e23 = Edge(v3, v9, 549)
        e24 = Edge(v3, v10, 518)
        e25 = Edge(v4, v5, 536)
        e26 = Edge(v4, v6, 593)
        e27 = Edge(v4, v7, 548)
        e28 = Edge(v4, v8, 537)
        e29 = Edge(v4, v9, 514)
        e30 = Edge(v4, v10, 577)
        e31 = Edge(v5, v6, 565)
        e32 = Edge(v5, v7, 590)
        e33 = Edge(v5, v8, 509)
        e34 = Edge(v5, v9, 500)
        e35 = Edge(v5, v10, 528)
        e36 = Edge(v6, v7, 556)
        e37 = Edge(v6, v8, 531)
        e38 = Edge(v6, v9, 585)
        e39 = Edge(v6, v10, 563)
        e40 = Edge(v7, v8, 594)
        e41 = Edge(v7, v9, 569)
        e42 = Edge(v7, v10, 528)
        e43 = Edge(v8, v9, 505)
        e44 = Edge(v8, v10, 517)
        e45 = Edge(v9, v10, 530)

        g.add_edge(e1)
        g.add_edge(e2)
        g.add_edge(e3)
        g.add_edge(e4)
        g.add_edge(e5)
        g.add_edge(e6)
        g.add_edge(e7)
        g.add_edge(e8)
        g.add_edge(e9)
        g.add_edge(e10)
        g.add_edge(e11)
        g.add_edge(e12)
        g.add_edge(e13)
        g.add_edge(e14)
        g.add_edge(e15)
        g.add_edge(e16)
        g.add_edge(e17)
        g.add_edge(e18)
        g.add_edge(e19)
        g.add_edge(e20)
        g.add_edge(e21)
        g.add_edge(e22)
        g.add_edge(e23)
        g.add_edge(e24)
        g.add_edge(e25)
        g.add_edge(e26)
        g.add_edge(e27)
        g.add_edge(e28)
        g.add_edge(e29)
        g.add_edge(e30)
        g.add_edge(e31)
        g.add_edge(e32)
        g.add_edge(e33)
        g.add_edge(e34)
        g.add_edge(e35)
        g.add_edge(e36)
        g.add_edge(e37)
        g.add_edge(e38)
        g.add_edge(e39)
        g.add_edge(e40)
        g.add_edge(e41)
        g.add_edge(e42)
        g.add_edge(e43)
        g.add_edge(e44)
        g.add_edge(e45)

        print(g)

        q = g.p_edges()

        print("edges \n" + q)

        print("num_edges " + str(len(g.edges)) + "\n")

        tsp = TSP()
        t = tsp.prim(g)
        s = "["
        suma  = 0
        for e in t:
            s += "(v" + str(e.v1.element) + ", v" + str(e.v2.element) + "):$" + str(e.weight) + ","
            suma += e.weight
        s += "] -> $" + str(suma)
        print("gen_tree " + str(s) + "\n")

        a = tsp.odd_vertex(t)

        print("odd_vertex "+ str(a) + "\n")

        ger = tsp.build_new_graph(g)

        print("Induced " + str(ger))

        r = "["
        for e in ger.edges:
            r += "(v" + str(e.v1.element) + ", v" + str(e.v2.element) + "):$" + str(e.weight) + ","
        r += "]" 

        print("edges \n" + r + "\n")

        print("num_edges " + str(len(ger.edges)) + "\n")

        ss = tsp.matching(ger)
        aa = "["
        for a in ss:
            aa += "(v" + str(a.v1.element) + ", v" + str(a.v2.element) + "):$" + str(a.weight) + ", "
        aa += "]"
        print("matching \n" + aa + 
        "\n")

        mut = tsp.matching_u_tree(t, ss)

        h = "["
        for a in mut:
            h += "(v" + str(a.v1.element) + ", v" + str(a.v2.element) + "):$" + str(a.weight) + ", "
        h += "]"

        print("union \n" + h + "\n")
    elif inp == 3:
        e1 = Edge(v1, v2, 578)
        e2 = Edge(v1, v3, 543)
        e3 = Edge(v1, v4, 566)
        e4 = Edge(v1, v5, 555)
        e5 = Edge(v1, v6, 501)
        e6 = Edge(v1, v7, 513)
        e7 = Edge(v1, v8, 534)
        e8 = Edge(v1, v9, 567)
        e9 = Edge(v1, v10, 568)
        e10 = Edge(v2, v3, 597)
        e11 = Edge(v2, v4, 519)
        e12 = Edge(v2, v5, 562)
        e13 = Edge(v2, v6, 552)
        e14 = Edge(v2, v7, 558)
        e15 = Edge(v2, v8, 561)
        e16 = Edge(v2, v9, 524)
        e17 = Edge(v2, v10, 549)
        e18 = Edge(v3, v4, 550)
        e19 = Edge(v3, v5, 560)
        e20 = Edge(v3, v6, 547)
        e21 = Edge(v3, v7, 542)
        e22 = Edge(v3, v8, 539)
        e23 = Edge(v3, v9, 564)
        e24 = Edge(v3, v10, 563)
        e25 = Edge(v4, v5, 558)
        e26 = Edge(v4, v6, 565)
        e27 = Edge(v4, v7, 539)
        e28 = Edge(v4, v8, 568)
        e29 = Edge(v4, v9, 556)
        e30 = Edge(v4, v10, 559)
        e31 = Edge(v5, v6, 548)
        e32 = Edge(v5, v7, 577)
        e33 = Edge(v5, v8, 572)
        e34 = Edge(v5, v9, 588)
        e35 = Edge(v5, v10, 599)
        e36 = Edge(v6, v7, 590)
        e37 = Edge(v6, v8, 592)
        e38 = Edge(v6, v9, 585)
        e39 = Edge(v6, v10, 586)
        e40 = Edge(v7, v8, 555)
        e41 = Edge(v7, v9, 561)
        e42 = Edge(v7, v10, 585)
        e43 = Edge(v8, v9, 568)
        e44 = Edge(v8, v10, 542)
        e45 = Edge(v9, v10, 560)

        g.add_edge(e1)
        g.add_edge(e2)
        g.add_edge(e3)
        g.add_edge(e4)
        g.add_edge(e5)
        g.add_edge(e6)
        g.add_edge(e7)
        g.add_edge(e8)
        g.add_edge(e9)
        g.add_edge(e10)
        g.add_edge(e11)
        g.add_edge(e12)
        g.add_edge(e13)
        g.add_edge(e14)
        g.add_edge(e15)
        g.add_edge(e16)
        g.add_edge(e17)
        g.add_edge(e18)
        g.add_edge(e19)
        g.add_edge(e20)
        g.add_edge(e21)
        g.add_edge(e22)
        g.add_edge(e23)
        g.add_edge(e24)
        g.add_edge(e25)
        g.add_edge(e26)
        g.add_edge(e27)
        g.add_edge(e28)
        g.add_edge(e29)
        g.add_edge(e30)
        g.add_edge(e31)
        g.add_edge(e32)
        g.add_edge(e33)
        g.add_edge(e34)
        g.add_edge(e35)
        g.add_edge(e36)
        g.add_edge(e37)
        g.add_edge(e38)
        g.add_edge(e39)
        g.add_edge(e40)
        g.add_edge(e41)
        g.add_edge(e42)
        g.add_edge(e43)
        g.add_edge(e44)
        g.add_edge(e45)

        print(g)

        q = g.p_edges()

        print("edges \n" + q)

        print("num_edges " + str(len(g.edges)) + "\n")

        tsp = TSP()
        t = tsp.prim(g)
        s = "["
        suma  = 0
        for e in t:
            s += "(v" + str(e.v1.element) + ", v" + str(e.v2.element) + "):$" + str(e.weight) + ","
            suma += e.weight
        s += "] -> $" + str(suma)
        print("gen_tree " + str(s) + "\n")

        a = tsp.odd_vertex(t)

        print("odd_vertex "+ str(a) + "\n")

        ger = tsp.build_new_graph(g)

        print("Induced " + str(ger))

        r = "["
        for e in ger.edges:
            r += "(v" + str(e.v1.element) + ", v" + str(e.v2.element) + "):$" + str(e.weight) + ","
        r += "]" 

        print("edges \n" + r + "\n")

        print("num_edges " + str(len(ger.edges)) + "\n")

        ss = tsp.matching(ger)
        aa = "["
        for a in ss:
            aa += "(v" + str(a.v1.element) + ", v" + str(a.v2.element) + "):$" + str(a.weight) + ", "
        aa += "]"
        print("matching \n" + aa + 
        "\n")

        mut = tsp.matching_u_tree(t, ss)

        h = "["
        for a in mut:
            h += "(v" + str(a.v1.element) + ", v" + str(a.v2.element) + "):$" + str(a.weight) + ", "
        h += "]"

        print("union \n" + h + "\n")
    elif inp == 4:
        e1 = Edge(v1, v2, 555)
        e2 = Edge(v1, v3, 543)
        e3 = Edge(v1, v4, 567)
        e4 = Edge(v1, v5, 560)
        e5 = Edge(v1, v6, 556)
        e6 = Edge(v1, v7, 532)
        e7 = Edge(v1, v8, 560)
        e8 = Edge(v1, v9, 541)
        e9 = Edge(v1, v10, 569)
        e10 = Edge(v2, v3, 542)
        e11 = Edge(v2, v4, 534)
        e12 = Edge(v2, v5, 532)
        e13 = Edge(v2, v6, 569)
        e14 = Edge(v2, v7, 531)
        e15 = Edge(v2, v8, 537)
        e16 = Edge(v2, v9, 509)
        e17 = Edge(v2, v10, 502)
        e18 = Edge(v3, v4, 506)
        e19 = Edge(v3, v5, 500)
        e20 = Edge(v3, v6, 600)
        e21 = Edge(v3, v7, 568)
        e22 = Edge(v3, v8, 542)
        e23 = Edge(v3, v9, 565)
        e24 = Edge(v3, v10, 578)
        e25 = Edge(v4, v5, 598)
        e26 = Edge(v4, v6, 586)
        e27 = Edge(v4, v7, 540)
        e28 = Edge(v4, v8, 544)
        e29 = Edge(v4, v9, 545)
        e30 = Edge(v4, v10, 550)
        e31 = Edge(v5, v6, 555)
        e32 = Edge(v5, v7, 575)
        e33 = Edge(v5, v8, 531)
        e34 = Edge(v5, v9, 543)
        e35 = Edge(v5, v10, 578)
        e36 = Edge(v6, v7, 563)
        e37 = Edge(v6, v8, 609)
        e38 = Edge(v6, v9, 559)
        e39 = Edge(v6, v10, 572)
        e40 = Edge(v7, v8, 578)
        e41 = Edge(v7, v9, 577)
        e42 = Edge(v7, v10, 532)
        e43 = Edge(v8, v9, 548)
        e44 = Edge(v8, v10, 556)
        e45 = Edge(v9, v10, 599)

        g.add_edge(e1)
        g.add_edge(e2)
        g.add_edge(e3)
        g.add_edge(e4)
        g.add_edge(e5)
        g.add_edge(e6)
        g.add_edge(e7)
        g.add_edge(e8)
        g.add_edge(e9)
        g.add_edge(e10)
        g.add_edge(e11)
        g.add_edge(e12)
        g.add_edge(e13)
        g.add_edge(e14)
        g.add_edge(e15)
        g.add_edge(e16)
        g.add_edge(e17)
        g.add_edge(e18)
        g.add_edge(e19)
        g.add_edge(e20)
        g.add_edge(e21)
        g.add_edge(e22)
        g.add_edge(e23)
        g.add_edge(e24)
        g.add_edge(e25)
        g.add_edge(e26)
        g.add_edge(e27)
        g.add_edge(e28)
        g.add_edge(e29)
        g.add_edge(e30)
        g.add_edge(e31)
        g.add_edge(e32)
        g.add_edge(e33)
        g.add_edge(e34)
        g.add_edge(e35)
        g.add_edge(e36)
        g.add_edge(e37)
        g.add_edge(e38)
        g.add_edge(e39)
        g.add_edge(e40)
        g.add_edge(e41)
        g.add_edge(e42)
        g.add_edge(e43)
        g.add_edge(e44)
        g.add_edge(e45)

        print(g)

        q = g.p_edges()

        print("edges \n" + q)

        print("num_edges " + str(len(g.edges)) + "\n")

        tsp = TSP()
        t = tsp.prim(g)
        s = "["
        suma  = 0
        for e in t:
            s += "(v" + str(e.v1.element) + ", v" + str(e.v2.element) + "):$" + str(e.weight) + ","
            suma += e.weight
        s += "] -> $" + str(suma)
        print("gen_tree " + str(s) + "\n")

        a = tsp.odd_vertex(t)

        print("odd_vertex "+ str(a) + "\n")

        ger = tsp.build_new_graph(g)

        print("Induced " + str(ger))

        r = "["
        for e in ger.edges:
            r += "(v" + str(e.v1.element) + ", v" + str(e.v2.element) + "):$" + str(e.weight) + ","
        r += "]" 

        print("edges \n" + r + "\n")

        print("num_edges " + str(len(ger.edges)) + "\n")

        ss = tsp.matching(ger)
        aa = "["
        for a in ss:
            aa += "(v" + str(a.v1.element) + ", v" + str(a.v2.element) + "):$" + str(a.weight) + ", "
        aa += "]"
        print("matching \n" + aa + 
        "\n")

        mut = tsp.matching_u_tree(t, ss)

        h = "["
        for a in mut:
            h += "(v" + str(a.v1.element) + ", v" + str(a.v2.element) + "):$" + str(a.weight) + ", "
        h += "]"

        print("union \n" + h + "\n")
    elif inp == 5:
        e1 = Edge(v1, v2, 500)
        e2 = Edge(v1, v3, 501)
        e3 = Edge(v1, v4, 502)
        e4 = Edge(v1, v5, 503)
        e5 = Edge(v1, v6, 504)
        e6 = Edge(v1, v7, 505)
        e7 = Edge(v1, v8, 506)
        e8 = Edge(v1, v9, 507)
        e9 = Edge(v1, v10, 508)
        e10 = Edge(v2, v3, 509)
        e11 = Edge(v2, v4, 510)
        e12 = Edge(v2, v5, 511)
        e13 = Edge(v2, v6, 512)
        e14 = Edge(v2, v7, 513)
        e15 = Edge(v2, v8, 514)
        e16 = Edge(v2, v9, 515)
        e17 = Edge(v2, v10, 516)
        e18 = Edge(v3, v4, 517)
        e19 = Edge(v3, v5, 518)
        e20 = Edge(v3, v6, 519)
        e21 = Edge(v3, v7, 520)
        e22 = Edge(v3, v8, 521)
        e23 = Edge(v3, v9, 522)
        e24 = Edge(v3, v10, 523)
        e25 = Edge(v4, v5, 524)
        e26 = Edge(v4, v6, 525)
        e27 = Edge(v4, v7, 526)
        e28 = Edge(v4, v8, 527)
        e29 = Edge(v4, v9, 528)
        e30 = Edge(v4, v10, 529)
        e31 = Edge(v5, v6, 530)
        e32 = Edge(v5, v7, 531)
        e33 = Edge(v5, v8, 532)
        e34 = Edge(v5, v9, 533)
        e35 = Edge(v5, v10, 534)
        e36 = Edge(v6, v7, 535)
        e37 = Edge(v6, v8, 536)
        e38 = Edge(v6, v9, 537)
        e39 = Edge(v6, v10, 538)
        e40 = Edge(v7, v8, 539)
        e41 = Edge(v7, v9, 540)
        e42 = Edge(v7, v10, 541)
        e43 = Edge(v8, v9, 542)
        e44 = Edge(v8, v10, 543)
        e45 = Edge(v9, v10, 543)

        g.add_edge(e1)
        g.add_edge(e2)
        g.add_edge(e3)
        g.add_edge(e4)
        g.add_edge(e5)
        g.add_edge(e6)
        g.add_edge(e7)
        g.add_edge(e8)
        g.add_edge(e9)
        g.add_edge(e10)
        g.add_edge(e11)
        g.add_edge(e12)
        g.add_edge(e13)
        g.add_edge(e14)
        g.add_edge(e15)
        g.add_edge(e16)
        g.add_edge(e17)
        g.add_edge(e18)
        g.add_edge(e19)
        g.add_edge(e20)
        g.add_edge(e21)
        g.add_edge(e22)
        g.add_edge(e23)
        g.add_edge(e24)
        g.add_edge(e25)
        g.add_edge(e26)
        g.add_edge(e27)
        g.add_edge(e28)
        g.add_edge(e29)
        g.add_edge(e30)
        g.add_edge(e31)
        g.add_edge(e32)
        g.add_edge(e33)
        g.add_edge(e34)
        g.add_edge(e35)
        g.add_edge(e36)
        g.add_edge(e37)
        g.add_edge(e38)
        g.add_edge(e39)
        g.add_edge(e40)
        g.add_edge(e41)
        g.add_edge(e42)
        g.add_edge(e43)
        g.add_edge(e44)
        g.add_edge(e45)

        print(g)

        q = g.p_edges()

        print("edges \n" + q)

        print("num_edges " + str(len(g.edges)) + "\n")

        tsp = TSP()
        t = tsp.prim(g)
        s = "["
        suma  = 0
        for e in t:
            s += "(v" + str(e.v1.element) + ", v" + str(e.v2.element) + "):$" + str(e.weight) + ","
            suma += e.weight
        s += "] -> $" + str(suma)
        print("gen_tree " + str(s) + "\n")

        a = tsp.odd_vertex(t)

        print("odd_vertex "+ str(a) + "\n")

        ger = tsp.build_new_graph(g)

        print("Induced " + str(ger))

        r = "["
        for e in ger.edges:
            r += "(v" + str(e.v1.element) + ", v" + str(e.v2.element) + "):$" + str(e.weight) + ","
        r += "]" 

        print("edges \n" + r + "\n")

        print("num_edges " + str(len(ger.edges)) + "\n")

        ss = tsp.matching(ger)
        aa = "["
        for a in ss:
            aa += "(v" + str(a.v1.element) + ", v" + str(a.v2.element) + "):$" + str(a.weight) + ", "
        aa += "]"
        print("matching \n" + aa + 
        "\n")

        mut = tsp.matching_u_tree(t, ss)

        h = "["
        for a in mut:
            h += "(v" + str(a.v1.element) + ", v" + str(a.v2.element) + "):$" + str(a.weight) + ", "
        h += "]"

        print("union \n" + h + "\n")
    else:
        print("invalid input :(")


    