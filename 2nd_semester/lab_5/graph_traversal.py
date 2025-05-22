from collections import deque


class GraphTraversal:
    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)
        self.reset()

    def reset(self):
        self.visited = [False] * self.n
        self.parent = [-1] * self.n
        self.queue = deque()
        self.stack = []
        self.current_vertex = -1
        self.traversal_type = None
        self.traversal_order = []
        self.traversal_tree = []
        self.started = False
        self.completed = False

    def find_start_vertex(self):
        for i in range(self.n):
            if any(self.matrix[i]) and not self.visited[i]:
                return i
        return -1

    def find_unvisited_vertex(self):
        for i in range(self.n):
            if not self.visited[i] and any(self.matrix[i]):
                return i
        return -1

    def init_bfs(self):
        self.reset()
        self.traversal_type = "BFS"
        start_vertex = self.find_start_vertex()
        if start_vertex != -1:
            self.queue.append(start_vertex)
            self.visited[start_vertex] = True
            self.current_vertex = start_vertex
            self.traversal_order.append(start_vertex)
            self.started = True
            self.completed = False
            return start_vertex
        return -1

    def init_dfs(self):
        self.reset()
        self.traversal_type = "DFS"
        start_vertex = self.find_start_vertex()
        if start_vertex != -1:
            self.stack.append(start_vertex)
            self.visited[start_vertex] = True
            self.current_vertex = start_vertex
            self.traversal_order.append(start_vertex)
            self.started = True
            self.completed = False
            return start_vertex
        return -1

    def get_unvisited_neighbors(self, vertex):
        return [
            i for i in range(self.n) if self.matrix[vertex][i] and not self.visited[i]
        ]

    def next_step(self):
        if not self.started or self.completed:
            return None

        if self.traversal_type == "BFS":
            return self.bfs_step()
        else:
            return self.dfs_step()

    def bfs_step(self):
        if not self.queue:
            start_vertex = self.find_unvisited_vertex()
            if start_vertex == -1:
                self.completed = True
                if self.completed:
                    self.print_traversal_tree_matrix()
                    self.print_renumbering()
                return None
            self.queue.append(start_vertex)
            self.visited[start_vertex] = True
            self.traversal_order.append(start_vertex)
            self.current_vertex = start_vertex
            return start_vertex

        current = self.queue[0]
        self.current_vertex = current

        neighbors = self.get_unvisited_neighbors(current)

        if neighbors:
            neighbor = neighbors[0]
            self.visited[neighbor] = True
            self.parent[neighbor] = current
            self.traversal_tree.append((current, neighbor))
            self.queue.append(neighbor)
            self.traversal_order.append(neighbor)
            self.current_vertex = neighbor
            return neighbor
        else:
            self.queue.popleft()
            return current

    def dfs_step(self):
        if not self.stack:
            start_vertex = self.find_unvisited_vertex()
            if start_vertex == -1:
                self.completed = True
                if self.completed:
                    self.print_traversal_tree_matrix()
                    self.print_renumbering()
                return None
            self.stack.append(start_vertex)
            self.visited[start_vertex] = True
            self.traversal_order.append(start_vertex)
            self.current_vertex = start_vertex
            return start_vertex

        current = self.stack[-1]
        self.current_vertex = current

        neighbors = self.get_unvisited_neighbors(current)

        if neighbors:
            neighbor = neighbors[0]
            self.visited[neighbor] = True
            self.parent[neighbor] = current
            self.traversal_tree.append((current, neighbor))
            self.stack.append(neighbor)
            self.traversal_order.append(neighbor)
            self.current_vertex = neighbor
            return neighbor
        else:
            self.stack.pop()
            return current

    def get_vertex_color(self, vertex):
        if vertex == self.current_vertex:
            return "red"
        if self.visited[vertex]:
            return "lightgreen"
        return "lightyellow"

    def print_traversal_tree_matrix(self):
        tree_matrix = [[0] * self.n for _ in range(self.n)]

        for child in range(self.n):
            parent = self.parent[child]
            if parent != -1:
                tree_matrix[parent][child] = 1

        print("\n=== Traversal Tree Adjacency Matrix ===")
        print("   " + " ".join(f"{i+1:2d}" for i in range(self.n)))
        print("  " + "-" * (self.n * 3 + 1))

        for i in range(self.n):
            if self.visited[i] or any(tree_matrix[i]):
                row_str = " ".join(f"{val:2d}" for val in tree_matrix[i])
                print(f"{i+1:2d}|{row_str}")

    def print_renumbering(self):
        print("\n=== Vertex Renumbering ===")
        print("Format: [original number] -> [new number in traversal order]")

        renumbering = {}
        for new_num, original_num in enumerate(self.traversal_order, 1):
            renumbering[original_num] = new_num

        for i in range(self.n):
            if i in renumbering:
                print(f"{i+1:2d} -> {renumbering[i]:2d}")
            else:
                print(f"{i+1:2d} -> Not reached in traversal")
