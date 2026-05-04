class Node:
    def __init__(self, value):
        self.value = value
        # (neighbor_node, weight)
        self.neighbors: tuple[Node, int] = []

    def add_edge(self, neighbor, weight):
        self.neighbors.append((neighbor, weight))

    def __repr__(self):
        return f"Node({self.value})"

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = Node(value)

    def add_edge(self, from_value, to_value, weight):
        if from_value not in self.nodes:
            self.add_node(from_value)
        if to_value not in self.nodes:
            self.add_node(to_value)

        self.nodes[from_value].add_edge(
            self.nodes[to_value], weight
        )

    def get_node(self, value):
        return self.nodes.get(value)

class Student:
    def __init__(self, name, neitd):
        self.name = name
        self.neitd = neitd
    
    def __lt__(self, other):
        if isinstance(other, Student):
            return self.name < other.name
        return NotImplemented
    
def get_netid(student):
    return student.neitd

#students = [Student("John Doe", 1), Student("Jane Doe", 5)]
#students.sort()
#print(students[0].name,students[1].name)
#students.sort(key =get_netid)
#print(students[0].neitd,students[1].neitd)