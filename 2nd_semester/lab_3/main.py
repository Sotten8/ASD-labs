from tkinter import Tk, Canvas
from graph_draw import create_graph
from matrix_print import dir_matrix_print, undir_matrix_print, labels, n

dir_matrix_print(n, labels)
print("\n    ----------------------\n")
undir_matrix_print(n, labels)

root = Tk()
root.title("Directed/Undirected Graph")

canvas = Canvas(root, width=600, height=600, bg="white")
canvas.pack()

create_graph(root, canvas)

root.mainloop()
