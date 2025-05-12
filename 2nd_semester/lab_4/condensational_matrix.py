def transitive_closure(matrix):
    size = len(matrix)
    closure = [row[:] for row in matrix]
    for k in range(size):
        for i in range(size):
            for j in range(size):
                closure[i][j] = closure[i][j] or (closure[i][k] and closure[k][j])
    return closure


def strong_connectivity_matrix(matrix):
    n = len(matrix)
    R = transitive_closure(matrix)
    S = [[int(R[i][j] and R[j][i]) for j in range(n)] for i in range(n)]
    return S


def find_strongly_connected_components(matrix):
    size = len(matrix)
    S = strong_connectivity_matrix(matrix)
    components = []
    visited = [False] * size

    def dfs(v, component):
        visited[v] = True
        component.append(v)
        for i in range(size):
            if not visited[i] and S[v][i]:
                dfs(i, component)

    for v in range(size):
        if not visited[v]:
            component = []
            dfs(v, component)
            components.append(component)

    return components


def build_condensation_matrix(adj_matrix, components):
    n = len(components)
    cond_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if any(adj_matrix[u][v] for u in components[i] for v in components[j]):
                cond_matrix[i][j] = 1
    return cond_matrix


def get_condensation_params(adj_matrix, components):
    cond_matrix = build_condensation_matrix(adj_matrix, components)
    vertex = len(components)
    param = [f"C{i+1}" for i in range(vertex)]
    title = "Condensation Matrix"
    return cond_matrix, vertex, param, title
