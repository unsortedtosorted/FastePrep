"""

Find the minimum spanning tree of a connected, undirected graph with weighted edges.

1. start from a node, 
2. visted the edge with least wieght to node not yet visited.

"""

import heapq
from collections import defaultdict


class vertex:
    def __init__(self, id, visited):
        self.id = id
        self.visited = visited


class edge:
    def __init__(self, weight, visited, src, dest):
        self.weight = weight
        self.visited = visited
        self.src = src
        self.dest = dest


class graph:
    g = []  # vertices
    e = []  # edges

    def __init__(self, g, e):
        self.g = g
        self.e = e

    # This method returns the vertex with a given id if it
    # already exists in the graph, returns NULL otherwise
    def vertex_exists(self, id):
        for i in range(len(self.g)):
            if self.g[i].id == id:
                return self.g[i]
        return None

    # This method generates the graph with v vertices
    # and e edges
    def generate_graph(self, vertices, edges):
        # create vertices
        for i in range(vertices):
            v = vertex(i + 1, False)
            self.g.append(v)

        # create edges
        for i in range(len(edges)):
            src = self.vertex_exists(edges[i][1])
            dest = self.vertex_exists(edges[i][2])
            e = edge(edges[i][0], False, src, dest)
            self.e.append(e)

    # This method finds the MST of a graph using
    # Prim's Algorithm
    # returns the weight of the MST
    def find_min_spanning_tree(self):
        weight = 0
        # TODO: Write - Your - Code

        link = defaultdict(list)

        for x in self.e:
            print(x.src.id)
            link[x.src].append((x.weight, x.dest))

        start = self.g[0]
        toVisit = []
        heapq.heappush(toVisit, (0, start))
        seen = set()

        while len(toVisit) > 0:

            curr = heapq.heappop(toVisit)

            node = curr[1]
            # print (visited)
            if node in seen:
                continue

            seen.add(node)

            weight += curr[0]

            for x in link[node]:
                if x[1] not in seen:
                    heapq.heappush(toVisit, x)

        return weight

    def print_graph(self):
        for i in range(len(self.g)):
            print(str(self.g[i].id) + " " + str(self.g[i].visited) + "\n")

        for i in range(len(self.e)):
            print(str(self.e[i].src.id) + "->" + str(self.e[i].dest.id) + "[" + str(self.e[i].weight) + ", " + str(
                self.e[i].visited) + "]  ")

        print("\n")

    def print_mst(self, w):
        print("MST")
        for i in range(len(self.e)):
            if self.e[i].visited == True:
                print(str(self.e[i].src.id) + "->"
                      + str(self.e[i].dest.id))

        print("weight: " + str(w))
        print("\n")


##solution_1

def test_graph1():
    gr = []
    ed = []
    g = graph(gr, ed)
    v = 5
    e = [[1, 1, 2], [1, 1, 3], [2, 2,
                                3], [3, 2, 4], [3, 3, 5], [2, 4, 5]]

    g.generate_graph(v, e);
    print("Testing graph 1...")
    # g.print_graph()
    w = g.find_min_spanning_tree()
    g.print_mst(w);


def test_graph2():
    gr = []
    ed = []
    g = graph(gr, ed)
    v = 7
    e = [[2, 1, 4], [1, 1, 3], [2, 1,
                                2], [1, 3, 4], [3, 2, 4], [2, 3, 5], [2, 4, 7],
         [1, 5, 6], [2, 5, 7]]

    g.generate_graph(v, e)
    print("Testing graph 2...")
    # g.print_graph()
    w = g.find_min_spanning_tree()
    g.print_mst(w);


def main():
    test_graph1()
    test_graph2()
    print("Completed!")


main()
