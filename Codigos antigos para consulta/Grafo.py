import timeit
import time

class graph:
    
    def __init__(self) -> None:
        self.graph = dict()
        self.adj = list()
        self.labels = set()
    


    def adj_lists(self) -> None:
        for i in range(len(self.graph)):
            self.adj.append([0 for a in range(len(self.graph))])

        for key, value in self.graph.items():
            key = int(key)
            value = [int(values) for values in value]
            for edge in value:
                self.adj[key][edge] = 1


    def display_adj(self) -> None: 
        for i in range(len(self.adj)):
            for j in range(len(self.adj)):
                print(self.adj[j][i], end=' ')
            print()


    def find_cycle(self) -> int:
        adj =self.adj
        possibles = graph.combine(adj)
        cycles = 0
        for chance in possibles:
            if graph.check(adj, chance): cycles += 1
        return cycles


    def check(adj: list[list[int]], chance: list[int]) -> bool:
        node = chance.pop()
        for edge in chance:
            if adj[node][edge]:
                sup = chance.copy()
                sup.remove(edge)
                for new in sup:
                    if adj[edge][new]:
                        ap = sup.copy()
                        ap.remove(new)
                        if adj[ap[0]][new] and adj[ap[0]][node]: return True
        return False


    def combine(adj: list[list[int]]) -> list[list[int]]:
        possibles = []
        size = len(adj)
        if size < 4: return []
        for i in range(size):
            a = [i]
            for j in range(size):
                if j not in a:
                    a.append(j)
                    for k in range(size):
                        if k not in a:
                            a.append(k)
                            for l in range(size):
                                if l not in a:
                                    a.append(l)
                                    b = a.copy()
                                    b.sort()
                                    if adj[b[0]][b[1]] or adj[b[0]][b[2]]:
                                        if b not in possibles:
                                            possibles.append(b)
                                    a.pop()
                            a.pop()
                    a.pop()
        return possibles                   
        

    def add_node(self, node: int) -> None:
        if not node in self.labels:
            self.graph[node] = []
            self.labels.add(node)
        return


    def search(self, array: list, node: int, start: int) -> int:
        if len(array) == 0: return start
        size = len(array)//2
        if size > 0:
            if array[size] > node:
                return self.search(array[:size], node, start)
            else:
                return self.search(array[size:], node, size + start)
        else:
            if array[size] > node:
                return size + start
            else:
                return size + 1 + start


    def add_edge(self, node: int, edge: int) -> None:
        if  self.graph.get(node) != None and self.graph.get(edge) != None:
            node1: list = self.graph.get(node)
            pos = self.search(node1, edge, 0)
            node1.insert(pos, edge)
            self.graph[node] = node1
            node2: list = self.graph.get(edge)
            pos = self.search(node2, node, 0)
            node2.insert(pos, node)
            self.graph[edge] = node2
        return
    

    def display_graph(self) -> None:
        sup = list(self.labels)
        sup.sort()
        for key, values in self.graph.items():
            #print(f'{node}: {self.graph.get(node)}')
            for neighbour in values:
                print(f'\t{str(neighbour)}')
            print(self.graph.get(key))
            print()


    def order(self) -> int:
        return len(self.graph)

    
    def size(self) -> int:
        target = 0
        for values in self.graph.values():
            target += len(values)
        return target//2


    def degree(self, node: int) -> int:
        if self.graph.get(node):
            return len(self.graph.get(node))
        else: return -1


    def min(self) -> int:
        target = -2
        for key in self.graph.keys():
            grade = self.degree(key)
            if target == -2 or target > grade:
                target = grade
        return target


    def max(self) -> int:
        target = -2
        for key in self.graph.keys():
            grade = self.degree(key)
            if target < grade:
                target = grade
        return target


    def average(self) -> int:
        total = self.order()
        grades = self.size()*2
        return grades/total
        

    def degreelist(self) -> None:
        grade = []
        keys = list(self.labels)
        keys.sort()
        for key in keys:
            grade.append(int(self.degree(key)))
        print(f'Degree list: {grade}')
        return


    def neighbourlist(self) -> None:
        for key in range(len(self.labels)):
            print(f'{str(key)}: {self.graph.get(key)}')
        return
    

    def evaluate_edge(self, node, edge) -> bool:
        if self.graph.get(node) == None: return False
        else:
            if edge in self.graph.get(node): return True
            else: return False


    def copy(self):
        second = graph()
        second.adj = self.adj.copy()
        second.graph = self.graph.copy()
        second.labels = self.labels.copy()
        return second


    def remove_edge(self, node: int, noh: int) -> None:
        self.graph[node].remove(noh)
        self.graph[noh].remove(node)
        return


    def remove_node(self, node: int) -> None:
        for noh in self.graph.get(node):
            self.remove_edge(noh, node)
        self.labels.discard(node)
        self.graph.pop(node)
        return


    def sequence(self) -> list[int]:
        i = self.size()
        #print(f'i = {i}')
        sequel = list()
        while(i > 1):
            leafs = set()
            for key in self.labels:
                if self.degree(key) == 1:
                    leafs.add(key)
            leaf = min(leafs)
            dad = self.graph.get(leaf)
            sequel.append(dad[0])
            self.remove_node(leaf)
            i -= 1
        return sequel
            
    
    def seq_build(self, sequence: list[int]) -> None:
        i = len(sequence)
        nodes = set(range(i + 2))
        for node in nodes:
            self.add_node(node)
        while(i > 0):
            node = min(nodes - set(sequence))
            noh = sequence.pop(0)
            self.add_edge(node, noh)
            nodes.remove(node)
            i -= 1
        node, noh = list(nodes)
        self.add_edge(node, noh)
        return

def teste(qnt, tree, abacaxi):
    quantidade = int(qnt)
    grafo = graph()
    for i in range(quantidade):
        aresta = str(tree[i]).split()
        grafo.add_node(int(aresta[0]))
        grafo.add_node(int(aresta[1]))
        grafo.add_edge(int(aresta[0]), int(aresta[1]))
    #grafo.neighbourlist()
    sequence = grafo.sequence()
    # for sequel in sequence:
    #     print(sequel, end=' ')
    # print()
    sequence = str(abacaxi).split()
    sequence = list(map(int, sequence))
    grafo = graph()
    grafo.seq_build(sequence)
    #grafo.neighbourlist()

def main():
    quantidade = int(input())
    grafo = graph()
    for i in range(quantidade):
        aresta = str(input()).split()
        grafo.add_node(int(aresta[0]))
        grafo.add_node(int(aresta[1]))
        grafo.add_edge(int(aresta[0]), int(aresta[1]))
    #grafo.neighbourlist()
    sequence = grafo.sequence()
    for sequel in sequence:
        print(sequel, end=' ')
    print()
    sequence = str(input()).split()
    sequence = list(map(int, sequence))
    grafo = graph()
    grafo.seq_build(sequence)
    grafo.neighbourlist()


qntd = 9
tre = ["0 6", "0 9", "1 9", "2 4", "2 5", "3 7", "5 8", "6 8", "7 9"]
sql = "5 8 9 7 0 1 2 3"
main_time: list[float] = timeit.repeat(stmt='teste(qnt = qntd, tree = tre, abacaxi = sql)', number=1000, globals=globals(), repeat= 5)

print(f'tempo: {round(min(main_time), 4)}s')

    
