class Graph:

    def __init__(self):
        self.number_of_nodes = 0
        self.adjacency_list = {}

    def add_vertex(self,node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []
            self.number_of_nodes += 1
        else:
            print("Node Already Exists!")
    
    def add_edge(self, node1, node2):
        if(node1 in self.adjacency_list):
            self.adjacency_list[node1].append(node2)
        else:
            self.add_vertex(node1)
            self.adjacency_list[node1].append(node2)

        if(node2 in self.adjacency_list):
            self.adjacency_list[node2].append(node1)
        else:
            self.add_vertex(node2)
            self.adjacency_list[node2].append(node1)

    def show_connections(self):
        for key,value in self.adjacency_list.items():
            print(key,": ",value)

my_graph = Graph()
my_graph.add_vertex('0')
my_graph.add_vertex('1')
my_graph.add_vertex('2')
my_graph.add_vertex('3')
my_graph.add_vertex('4')
my_graph.add_vertex('5')
my_graph.add_vertex('6')

my_graph.add_edge('0','1')
my_graph.add_edge('0','2')

my_graph.add_edge('1','2')
my_graph.add_edge('1','3')

my_graph.add_edge('2','4')

my_graph.add_edge('3','4')

my_graph.add_edge('4','5')

my_graph.add_edge('5','6')

my_graph.show_connections()