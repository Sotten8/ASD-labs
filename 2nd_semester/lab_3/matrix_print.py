import tkinter as tk, math, random

n1 = 4
n2 = 3
n3 = 2
n4 = 2

n = 10 + n3

random.seed(4322)

k = 1.0 - n3 * 0.02 - n4 * 0.05 - 0.25

directed_matrix = [
    [math.floor(random.uniform(0, 2.0) * k) for _ in range(n)] for _ in range(n)
]

undirected_matrix = [
    [max(directed_matrix[i][j], directed_matrix[j][i]) for j in range(n)]
    for i in range(n)
]

labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C"]


def matrix_print(matrix, vertex, param, title):
    print(f"\n    {title}:\n")
    print("   ", " ".join(labels))
    print("   _________________________")
    for row in range(vertex):
        print(
            f"{param[row]} |",
            " ".join(str(matrix[row][column]) for column in range(vertex)),
        )
