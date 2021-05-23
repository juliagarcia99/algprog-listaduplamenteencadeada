class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
####

class listaduplamenteencadeada
    def __init__ (self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = None(data)
            ponto = self.head
            while ponto.next:
                ponto = ponto.next
            new_node.prev = ponto
            new_node.next = None

    def printlista(self):
        ponto = self.head
        while ponto:
            print(ponto.data)
            ponto = ponto.next
    
    def inverter(self):
        temp = None
        ponto = self.head
        while ponto is not None:
            ponto = ponto.prev
            ponto.prev = ponto.next
            ponto.next = temp
            ponto = ponto.prev
        if temp is not None:
            self.head = temp.prev
        


        
