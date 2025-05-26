import random
import math

n1 = 4
n2 = 3
n3 = 2
n4 = 2

n = 10 + n3

random.seed(4322)

k = 1.0 - n3 * 0.01 - n4 * 0.005 - 0.05

directed_matrix = [
    [1 if random.uniform(0, 2.0) * k >= 1.0 else 0 for _ in range(n)] for _ in range(n)
]

undirected_matrix = [
    [max(directed_matrix[i][j], directed_matrix[j][i]) for j in range(n)]
    for i in range(n)
]

B = [[random.uniform(0, 2.0) for _ in range(n)] for _ in range(n)]
C = [
    [math.ceil(b * 100 * undirected_matrix[i][j]) for j, b in enumerate(row)]
    for i, row in enumerate(B)
]
D = [[1 if c > 0 else 0 for c in row] for row in C]
H = [[1 if D[i][j] == D[j][i] else 0 for j in range(n)] for i in range(n)]
Tr = [[1 if i < j else 0 for j in range(n)] for i in range(n)]

W = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            W[i][j] = 0
        else:
            weight = (D[i][j] * H[i][j] * Tr[i][j]) * C[i][j]
            W[i][j] = weight if weight != 0 else math.inf

for i in range(n):
    for j in range(i + 1, n):
        if W[i][j] != math.inf or W[j][i] != math.inf:
            W[i][j] = W[j][i] = min(
                W[i][j] if W[i][j] != math.inf else float("inf"),
                W[j][i] if W[j][i] != math.inf else float("inf"),
            )

labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C"]


def matrix_print(matrix, vertex, param, title):
    print(f"\n    {title}:\n")
    print("   ", " ".join(param[:vertex]))
    print("   " + "_" * (vertex * 2 + 1))
    for row in range(vertex):
        print(
            f"{param[row]} |",
            " ".join(str(matrix[row][column]) for column in range(vertex)),
        )


def print_weight_matrix():
    print("\n    Weight Matrix W:\n")
    header = "    " + " ".join(f"{label:>4}" for label in labels[:n])
    print(header)
    print("    " + "-" * (len(header) - 4))
    for row in range(n):
        print(
            f"{labels[row]:>2} |",
            " ".join(
                (
                    f"{W[row][column]:4d}"
                    if isinstance(W[row][column], int)
                    else ("   0" if row == column else " inf")
                )
                for column in range(n)
            ),
        )
