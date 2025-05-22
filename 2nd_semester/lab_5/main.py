from graph_draw import create_graph_window
from matrix_print import matrix_print, directed_matrix, undirected_matrix, labels, n

matrix_print(directed_matrix, n, labels, "Directed graph")
print("\n    ----------------------\n")
matrix_print(undirected_matrix, n, labels, "Undirected graph")

create_graph_window()
