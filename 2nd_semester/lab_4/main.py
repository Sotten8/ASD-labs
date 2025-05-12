import random, math, tkinter as tk
from shared_data import n, k1, k2, labels
import shared_data
from graph_draw import create_graph_window
from condensational_matrix import *

random.seed(4322)


def tkinter_print():
    create_graph()
    root.destroy()
    create_graph_window()


def matrix_print(matrix, vertex, param, title):
    print(f"\n{title}\n")
    print("   ", " ".join(param[:vertex]))
    print("   " + "_" * (2 * vertex + 1))
    for row in range(vertex):
        print(
            f"{param[row]} |", " ".join(str(matrix[row][col]) for col in range(vertex))
        )


def set_k1():
    shared_data.k = k1
    k_label.config(text=f"Selected k1: {shared_data.k}")


def set_k2():
    shared_data.k = k2
    k_label.config(text=f"Selected k2: {shared_data.k}")


def get_degrees_undirected(matrix):
    return [sum(row) for row in matrix]


def get_degrees_directed(matrix):
    in_degree = [sum(row[col] for row in matrix) for col in range(len(matrix))]
    out_degree = [sum(row) for row in matrix]
    return in_degree, out_degree


def get_regular_degree(degrees):
    if isinstance(degrees, tuple) and len(degrees) == 2:
        in_deg, out_deg = degrees
        if all(deg == in_deg[0] for deg in in_deg) and all(
            deg == out_deg[0] for deg in out_deg
        ):
            return (in_deg[0], out_deg[0])
    elif isinstance(degrees, list):
        if all(deg == degrees[0] for deg in degrees):
            return degrees[0]
    return None


def find_isolated_vertices(matrix):
    return [i for i, row in enumerate(matrix) if sum(row) == 0]


def find_hanging_vertices(matrix):
    n = len(matrix)
    hanging = []
    for i in range(n):
        out_degree = sum(matrix[i])
        in_degree = sum(row[i] for row in matrix)
        if in_degree + out_degree == 1:
            hanging.append(i)
    return hanging


def format_vertices(indices):
    return ", ".join(f"({shared_data.numeric_labels[i]})" for i in indices)


def multiply_matrices(A, B):
    size = len(A)
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += A[i][k] * B[k][j]
    return result


def create_graph():
    shared_data.directed_matrix = [
        [math.floor(random.uniform(0, 2.0) * shared_data.k) for _ in range(n)]
        for _ in range(n)
    ]
    shared_data.undirected_matrix = [
        [
            max(shared_data.directed_matrix[i][j], shared_data.directed_matrix[j][i])
            for j in range(n)
        ]
        for i in range(n)
    ]

    print(f"\nCurrent k: {shared_data.k}")
    print(f"\nCurrent n: {n}")

    matrix_print(
        shared_data.directed_matrix, n, labels, "Directed Graph Adjancency Matrix"
    )
    matrix_print(
        shared_data.undirected_matrix, n, labels, "Undirected Graph Adjancency Matrix"
    )

    in_deg, out_deg = get_degrees_directed(shared_data.directed_matrix)
    print("\nVertex in the directed graph:")
    for i in range(n):
        print(f"({i + 1}): in = {in_deg[i]}, out = {out_deg[i]}")

    degrees_undirected = get_degrees_undirected(shared_data.undirected_matrix)
    print("\nVertex in the undirected graph:")
    for i, degree in enumerate(degrees_undirected):
        print(f"({i + 1}): {degree}")

    print("\nIs regular (undirected):")
    reg_deg = get_regular_degree(degrees_undirected)
    print(
        f"The graph is regular. Degree of regularity: {reg_deg}"
        if reg_deg
        else "The graph is not regular."
    )

    print("\nIs regular (directed):")
    reg_deg_directed = get_regular_degree((in_deg, out_deg))
    if reg_deg_directed:
        in_reg, out_reg = reg_deg_directed
        print(f"The graph is regular. In-degree: {in_reg}, Out-degree: {out_reg}")
    else:
        print("The graph is not regular.")

    print("\nIsolated vertices")
    isolated = find_isolated_vertices(shared_data.undirected_matrix)
    print(format_vertices(isolated) if isolated else "- None found")

    print("\nHanging vertices")
    hanging = find_hanging_vertices(shared_data.directed_matrix)
    print(format_vertices(hanging) if hanging else "- None found")

    print("\nPaths of length 2:")
    A2 = multiply_matrices(shared_data.directed_matrix, shared_data.directed_matrix)
    for i in range(n):
        for j in range(n):
            if A2[i][j] > 0:
                for k in range(n):
                    if (
                        shared_data.directed_matrix[i][k] > 0
                        and shared_data.directed_matrix[k][j] > 0
                    ):
                        print(f"{i + 1} -> {k + 1} -> {j + 1}")

    print("\nPaths of length 3:")
    A3 = multiply_matrices(A2, shared_data.directed_matrix)
    for i in range(n):
        for j in range(n):
            if A3[i][j] > 0:
                for k in range(n):
                    if (
                        shared_data.directed_matrix[i][k] > 0
                        and shared_data.directed_matrix[k][j] > 0
                    ):
                        for l in range(n):
                            if shared_data.directed_matrix[j][l] > 0:
                                print(f"{i + 1} -> {k + 1} -> {j + 1} -> {l + 1}")

    reachability_matrix = transitive_closure(shared_data.directed_matrix)
    matrix_print(reachability_matrix, n, labels, "Reachability Matrix")

    strong_matrix = strong_connectivity_matrix(shared_data.directed_matrix)
    matrix_print(strong_matrix, n, labels, "Strong Connectivity Matrix")

    print("\nStrongly Connected Components:")
    components = find_strongly_connected_components(shared_data.directed_matrix)
    for i, component in enumerate(components):
        print(f"Component {i+1}:", format_vertices(component))

    if components:
        cond_matrix, vertex, param, title = get_condensation_params(
            shared_data.directed_matrix, components
        )
        matrix_print(cond_matrix, vertex, param, title)


root = tk.Tk()
root.title("Select k")

canvas = tk.Canvas(root, width=250, height=20)
canvas.pack()

button_k1 = tk.Button(root, text="Use k1", command=set_k1)
button_k1.pack(pady=5)

button_k2 = tk.Button(root, text="Use k2", command=set_k2)
button_k2.pack(pady=5)

create_button = tk.Button(root, text="Create Graph", command=tkinter_print)
create_button.pack(pady=10)

k_label = tk.Label(root, text=f"Current k: {shared_data.k}")
k_label.pack()

root.mainloop()
