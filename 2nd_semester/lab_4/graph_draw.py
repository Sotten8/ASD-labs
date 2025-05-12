from tkinter import Tk, Canvas, Button, Frame
from draw_utils import *
from positions import generate_positions
from shared_data import n
import shared_data, math
from condensational_matrix import find_strongly_connected_components

threshold = 1
positions = generate_positions()


def draw_condensation_graph(canvas, directed=True):
    canvas.delete("all")
    components = find_strongly_connected_components(shared_data.directed_matrix)
    component_positions = []
    radius = 30
    spacing = 100

    for i, component in enumerate(components):
        angle = 2 * 3.1415 * i / len(components)
        x = 300 + 200 * math.cos(angle)
        y = 300 + 200 * math.sin(angle)
        component_positions.append((x, y))

    for i, (x, y) in enumerate(component_positions):
        canvas.create_oval(
            x - radius,
            y - radius,
            x + radius,
            y + radius,
            fill="lightyellow",
            outline="black",
            width=2,
        )
        component_label = ", ".join(
            shared_data.numeric_labels[v] for v in components[i]
        )
        canvas.create_text(x, y, text=component_label, font=("Times New Roman", 10))

    for i in range(len(components)):
        for j in range(len(components)):
            if i == j:
                continue
            has_edge = any(
                shared_data.directed_matrix[u][v] == threshold
                for u in components[i]
                for v in components[j]
            )
            if has_edge:
                x1, y1 = component_positions[i]
                x2, y2 = component_positions[j]
                draw_arrow(canvas, x1, y1, x2, y2, radius=radius)


def create_graph_window():
    graph_window = Tk()
    graph_window.title("Graph Visualization")

    canvas = Canvas(graph_window, width=600, height=600)
    canvas.pack()

    button_frame = Frame(graph_window)
    button_frame.pack()

    def draw_all(directed=True):
        canvas.delete("all")
        draw_graph(canvas, positions)
        for i in range(n):
            for j in range(n):
                if shared_data.directed_matrix[i][j] == threshold:
                    if (
                        not directed
                        and shared_data.directed_matrix[j][i] == threshold
                        and j < i
                    ):
                        continue
                    x1, y1 = positions[i]
                    x2, y2 = positions[j]
                    if i == j:
                        draw_self_loop(canvas, x1, y1, directed=directed)
                    elif is_crossing_vertex(
                        x1, y1, x2, y2, positions, skip_indices={i, j}
                    ):
                        draw_arc(canvas, x1, y1, x2, y2, directed=directed)
                    elif directed:
                        if shared_data.directed_matrix[j][i] == threshold:
                            draw_arc(canvas, x1, y1, x2, y2, directed=directed)
                        else:
                            draw_arrow(canvas, x1, y1, x2, y2)
                    else:
                        draw_line(canvas, x1, y1, x2, y2)

    def toggle_graph():
        if button_mode.cget("text") == "Switch to Undirected":
            button_mode.config(text="Switch to Directed")
            draw_all(directed=False)
        else:
            button_mode.config(text="Switch to Undirected")
            draw_all(directed=True)

    def show_condensation():
        draw_condensation_graph(canvas)

    button_mode = Button(
        button_frame, text="Switch to Undirected", command=toggle_graph
    )
    button_mode.pack(side="left", padx=5)

    button_condensation = Button(
        button_frame, text="Switch to Condensational", command=show_condensation
    )
    button_condensation.pack(side="left", padx=5)

    draw_all(directed=True)
    graph_window.mainloop()
