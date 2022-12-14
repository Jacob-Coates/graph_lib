# All Graphs will use the Adjacency List format

import heapq

class Graph:
    def __init__(self,vertex_count, directed=True) -> None:
        self.vertex_count = vertex_count
        self.vertices = range(1, vertex_count + 1)
        self.directed = directed
        self.seen = []
        self.adj_list = {vertex : set() for vertex in self.vertices}

    def add_edge(self, node1: int, node2: int, cost=1) -> False:
        self.adj_list[node1].add((node2,cost))
        if not self.directed:
            self.adj_list[node2].add((node1,cost))

    def print_list(self):
        for i, (node,adj_list) in enumerate(self.adj_list.items()):
            print(node, " : ", [x for x in adj_list])

    def dfs(self, start_node: int = 1, node_list = []) -> None:
        if start_node in node_list:
            return node_list
        else:
            node_list.append(start_node)
            for (node,_) in sorted(self.adj_list[start_node]):
                self.dfs(node,node_list)
            return node_list

    def bfs(self, start_node: int = 1) -> None:
        node_list = []
        q = [start_node]
        seen = {start_node}
        while q:
            curr = q.pop(0)
            node_list.append(curr)
            for (node,_) in sorted(self.adj_list[curr]):
                if node not in seen:
                    q.append(node)
                    seen.add(node)
        return node_list

    def minimum_spanning_tree(self,start_node: int = 1):
        return self.prims(start_node)

    def prims(self, start_node: int = 1):
        new_g = Graph(self.vertex_count,self.directed)
        pq = []
        been = {start_node}
        heapq.heapify(pq)
        start_edges = list(self.adj_list[start_node])
        for (n,c) in start_edges:
            heapq.heappush(pq,(c,start_node,n))
        # Now pop off heap until tree made
        while pq:
            # get next avalible node
            (cost,seen_node,next_node) = heapq.heappop(pq)
            if next_node in been:
                continue
            new_g.add_edge(seen_node,next_node,cost)
            for (n,c) in list(self.adj_list[next_node]):
                if n not in been:
                    heapq.heappush(pq,(c,next_node,n))
            been.add(next_node)
        return new_g
    
    def dijkstra(self,source:int=1):
        dist = {}
        prev = {}
        dist[source] = 0

        q = []
        heapq.heapify(q)


        for v in self.vertices:
            if v != source:
                dist[v] =  float('inf')
                prev[v] = None
            heapq.heappush(q,(dist[v],v))

        while q:
            (dis,u) = heapq.heappop(q)
            for (v,edge_cost) in self.adj_list[u]:
                alt = dist[u] + edge_cost
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    heapq.heappush(q,(alt,v))
        return (dist,prev)

    def isBipartite(self) -> bool:
        red_q = [1]
        blue_q = []
        red = {1}
        blue = set()
        while red_q or blue_q:
            while red_q:
                curr = red_q.pop(0)
                for (node,_) in sorted(self.adj_list[curr]):
                    if node not in blue:
                        blue_q.append(node)
                        blue.add(node)
                    if node in red:
                        return False
            while blue_q:
                curr = blue_q.pop(0)
                for (node,_) in sorted(self.adj_list[curr]):
                    if node not in red:
                        red_q.append(node)
                        red.add(node)
                    if node in blue:
                        return False
        return True

    def minColours(self) -> int:
        max_colour = 1
        q = [1]
        coloured = {1:1}
        while q:
            curr = q.pop(0)
            for (node,_) in sorted(self.adj_list[curr]):
                if node not in coloured:
                    q.append(node)
                    coloured[node] = 2 if coloured[curr] == 1 else 1
                    max_colour = max(max_colour,2)
                else:
                    if coloured[node] == coloured[curr]:
                        if coloured[node] > 2:
                            coloured[node] += 1
                            max_colour = max(max_colour,coloured[node])
                        else:
                            coloured[node] = 3
                            max_colour = max(max_colour,3)
        return max_colour
            



# g = Graph(7,False)
# g.add_edge(1,2,4)
# g.add_edge(1,3,5)
# g.add_edge(1,4,6)
# g.add_edge(2,3)
# g.add_edge(2,5)
# g.add_edge(2,6)
# g.add_edge(2,7)
# g.print_list()
# print("------------")
# print(g.dfs())
# print("------------")
# print(g.bfs())
# print("------------")
# g.prims().print_list()
# print("------------")
# print("------------")
# print("------------")
# print(g.dijkstra(5))
# print(g.isBipartite())

# d = Graph(6,False)
# # K_6 graph
# d.add_edge(1,2)
# d.add_edge(1,3)
# d.add_edge(1,4)
# d.add_edge(1,5)
# d.add_edge(1,6)
# d.add_edge(2,3)
# d.add_edge(2,4)
# d.add_edge(2,5)
# d.add_edge(2,6)
# d.add_edge(3,4)
# d.add_edge(3,5)
# d.add_edge(3,6)
# d.add_edge(4,5)
# d.add_edge(4,6)
# d.add_edge(5,6)
# d.print_list()
# print(d.isBipartite())
# print(d.minColours())