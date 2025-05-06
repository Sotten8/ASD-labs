from tkinter import Tk, Canvas
from graph_draw import create_graph
from matrix_print import matrix_print, directed_matrix, undirected_matrix, labels, n

matrix_print(directed_matrix, n, labels, "Directed graph")
print("\n    ----------------------\n")
matrix_print(undirected_matrix, n, labels, "Undirected graph")

root = Tk()
root.title("Directed/Undirected Graph")

canvas = Canvas(root, width=600, height=600, bg="white")
canvas.pack()

create_graph(root, canvas)

root.mainloop()
