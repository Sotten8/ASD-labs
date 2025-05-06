from draw_utils import (
    draw_graph,
    draw_arrow,
    draw_arc,
    draw_line,
    is_crossing_vertex,
    draw_self_loop,
)
from positions import generate_positions
from matrix_print import directed_matrix, n
from tkinter import Button

threshold = 1
positions = generate_positions()


def create_graph(root, canvas):
    def draw_all(directed):
        canvas.delete("all")
        draw_graph(canvas, positions)

        for i in range(n):
            for j in range(n):
                if directed_matrix[i][j] == threshold:
                    x1, y1 = positions[i]
                    x2, y2 = positions[j]

                    if i == j:
                        draw_self_loop(canvas, x1, y1, directed=directed)
                    elif is_crossing_vertex(
                        x1, y1, x2, y2, positions, skip_indices={i, j}
                    ):
                        draw_arc(canvas, x1, y1, x2, y2, directed=directed)
                    else:
                        if directed:
                            draw_arrow(canvas, x1, y1, x2, y2)
                        else:
                            draw_line(canvas, x1, y1, x2, y2)

    draw_all(directed=True)

    def toggle_graph():
        nonlocal button
        if button.cget("text") == "Switch to Undirected":
            button.config(text="Switch to Directed")
            draw_all(directed=False)
        else:
            button.config(text="Switch to Undirected")
            draw_all(directed=True)

    button = Button(root, text="Switch to Undirected", command=toggle_graph)
    button.pack()
