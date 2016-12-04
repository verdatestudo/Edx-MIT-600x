'''
MIT6002 edX - week 1

Last Updated: 2016-Nov-09
First Created: 2016-Nov-07
Python 3.5
Chris
'''

def powerSet(items):
    '''
    Generates all combos of N items. Provided by question.
    '''
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            print("{0:b}".format(i), (i >> j))
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
            print(i, items[j], j, (i >> j) % 2, combo)
        yield combo

def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as
      a list of which item(s) are in each bag.

      Written by user.
    """
    N = len(items)
    # enumerate the 3**N possible combinations
    for i in range(3**N):
        combo = []
        combo2 = []
        for j in range(N):
            if (i // (3 ** j)) % 3 == 1:
                combo.append(items[j])
            elif (i // (3 ** j)) % 3 == 2:
                combo2.append(items[j])
            print(i, j, (i // (3 ** j)), combo, combo2)
            #print("{0:b}".format(i), (i >> j), i, items[j], ' ... ', (i >> j) % 3, (i // (3 ** j)) % 3, ' ... ', combo, combo2)
        yield (combo, combo2)

#a = list(yieldAllCombos(['a', 'b']))
# -*- coding: utf-8 -*-
"""
lecture3segment2.py
Created on Tue Jul 12 15:04:56 2016

@author: guttag
"""

class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()

class WeightedEdge(Edge):
    '''
    My code, added for exercise 7.
    '''
    def __init__(self, src, dest, weight):
        # Your code here
        Edge.__init__(self, src, dest)
        self.weight = weight
    def getWeight(self):
        # Your code here
        return self.weight
    def __str__(self):
        # Your code here
        return Edge.__str__(self) + ' (%d)' % (self.getWeight())

class Digraph(object):
    """edges is a dict mapping each node to a list of
    its children"""
    def __init__(self):
        self.edges = {}
    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.edges
    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '->'\
                         + dest.getName() + '\n'
        return result[:-1] #omit final newline

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)


def buildCityGraph(graphType):
    g = graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'): #Create 7 nodes
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g

def ex2_lecture3():
    '''
    Exercise 2 Lecture 3 from week 1.
    '''
    nodes = []
    nodes.append(Node("ABC")) # nodes[0]
    nodes.append(Node("ACB")) # nodes[1]
    nodes.append(Node("BAC")) # nodes[2]
    nodes.append(Node("BCA")) # nodes[3]
    nodes.append(Node("CAB")) # nodes[4]
    nodes.append(Node("CBA")) # nodes[5]

    g = Graph()

    for n in nodes:
        g.addNode(n)

    # my code below

    for n in nodes:
        node_name = n.getName()
        # generate possible names based on rule of only one swap, must be next to each other.
        # start + switch + end e.g ABCDE switching C and D: str(AB + D + C + E)
        pos_names = [str(node_name[:x] + node_name[x + 1] + node_name[x] + node_name[x+2:]) for x in range(len(node_name) - 1)]

        # get other nodes that this current node is already connected to. if we're already connected, remove from possibilities to avoid duplicates.
        for child_node in g.childrenOf(g.getNode(node_name)):
            if str(child_node) in pos_names:
                pos_names.remove(str(child_node))

        # now we only have new possiblities in the pos_names list, we can add the edge to the graph.
        for pos in pos_names:
            pot_edge = Edge(g.getNode(node_name), g.getNode(pos))
            g.addEdge(pot_edge)

    return g

def DFS(graph, start, end, path, shortest):
    '''
    DFS - exercise 4
    '''

    path = path + [start]

    if start == end:
        return path

    # making sure start, end and node are all string format while computing
    for node in graph.childrenOf(graph.getNode(start)):
        #print(start, node, '...', type(start), type(end), type(node.getName()), '...', path)
        if node.getName() not in path: # avoid cycles (i.e nodes already visited)
            if shortest == None or len(path) < len(shortest):
                new_path = DFS(graph, node.getName(), end, path, shortest)
                if new_path != None:
                    shortest = new_path

    return shortest


def ex4():
    '''
    Exercise 4
    '''

    '''
    graph = {}
    nodes['ABC'] = ['BAC', 'ACB']
    nodes['ACB'] = ['CAB', 'ABC']
    nodes['BAC'] = ['ABC', 'BCA']
    nodes['BCA'] = ['CBA', 'BAC']
    nodes['CAB'] = ['CBA', 'ACB']
    nodes['CBA'] = ['BCA', 'CAB']
    '''

    #nodes.append(Node("ABC")) # nodes[0]
    #nodes.append(Node("ACB")) # nodes[1]
    #nodes.append(Node("BAC")) # nodes[2]
    #nodes.append(Node("BCA")) # nodes[3]
    #nodes.append(Node("CAB")) # nodes[4]
    #nodes.append(Node("CBA")) # nodes[5]

    graph = ex2_lecture3() # nodes are same as previous exercise, so we can just build the graph from there.

    # note: answers below don't solve the question asked. Did not bother as learning to write DFS was more important than creating a special set of nodes just for one question.

    print(DFS(graph, 'ABC', 'CAB', [], None), 'q1 shortest')
    print(DFS(graph, 'CAB', 'ACB', [], None), 'q2 shortest')
    print(DFS(graph, 'ACB', 'ACB', [], None), 'q3 shortest')
    print(DFS(graph, 'BAC', 'CAB', [], None), 'q4 shortest')
    print(DFS(graph, 'BAC', 'BCA', [], None), 'q5 shortest')
    print(DFS(graph, 'BCA', 'ACB', [], None), 'q6 shortest')


#print(buildCityGraph(Graph))
#print(ex2_lecture3())
#ex4()
