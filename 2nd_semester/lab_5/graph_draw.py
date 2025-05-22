from draw_utils import *
from positions import generate_positions
from matrix_print import directed_matrix, n
from tkinter import Button, Tk, Canvas, Frame, messagebox, Label
from graph_traversal import GraphTraversal

threshold = 1
positions = generate_positions()


def create_graph_window():
    graph_window = Tk()
    graph_window.title("Graph Visualization")

    canvas = Canvas(graph_window, width=600, height=600)
    canvas.pack()

    info_frame = Frame(graph_window)
    info_frame.pack(pady=5)

    status_label = Label(
        info_frame, text="Status: Ready for traversal", font=("Arial", 12)
    )
    status_label.pack()

    traversal_info = Label(info_frame, text="", font=("Arial", 10))
    traversal_info.pack()

    button_frame = Frame(graph_window)
    button_frame.pack()

    traversal = GraphTraversal(directed_matrix)

    def draw_all(directed=True):
        canvas.delete("all")

        for i in range(n):
            for j in range(n):
                if directed_matrix[i][j] == threshold:
                    if not directed and directed_matrix[j][i] == threshold and j < i:
                        continue

                    x1, y1 = positions[i]
                    x2, y2 = positions[j]

                    edge_color = "gray"
                    width = 1
                    if (i, j) in traversal.traversal_tree:
                        edge_color = "red"
                        width = 3

                    if i == j:
                        draw_self_loop(
                            canvas,
                            x1,
                            y1,
                            directed=directed,
                            color=edge_color,
                            width=width,
                        )
                    elif is_crossing_vertex(
                        x1, y1, x2, y2, positions, skip_indices={i, j}
                    ):
                        draw_arc(
                            canvas,
                            x1,
                            y1,
                            x2,
                            y2,
                            directed=directed,
                            color=edge_color,
                            width=width,
                        )
                    elif directed:
                        if directed_matrix[j][i] == threshold:
                            draw_arc(
                                canvas,
                                x1,
                                y1,
                                x2,
                                y2,
                                directed=directed,
                                color=edge_color,
                                width=width,
                            )
                        else:
                            draw_arrow(
                                canvas, x1, y1, x2, y2, color=edge_color, width=width
                            )
                    else:
                        draw_line(canvas, x1, y1, x2, y2, color=edge_color, width=width)

        radius = 25
        for i, (x, y) in enumerate(positions):
            color = traversal.get_vertex_color(i)
            canvas.create_oval(
                x - radius,
                y - radius,
                x + radius,
                y + radius,
                fill=color,
                outline="black",
                width=2,
            )
            canvas.create_text(
                x,
                y,
                text=str(i + 1),
                font=("Times New Roman", 12, "bold"),
                fill="black",
            )

        status_text = "Status: "
        if not traversal.started:
            status_text += "Ready for traversal"
            traversal_info.config(text="")
        elif traversal.completed:
            status_text += "Traversal completed"
            order_text = "Traversal order: " + " → ".join(
                [str(v + 1) for v in traversal.traversal_order]
            )
            traversal_info.config(text=order_text)
            status_label.config(text=status_text)

            messagebox.showinfo(
                "Traversal Complete",
                "Graph traversal completed!\nTraversal tree adjacency matrix and vertex renumbering are displayed in the console.",
            )
        else:
            if traversal.traversal_type == "BFS":
                status_text += (
                    f"BFS traversal - current vertex: {traversal.current_vertex + 1}"
                )
            else:
                status_text += (
                    f"DFS traversal - current vertex: {traversal.current_vertex + 1}"
                )

            if traversal.traversal_order:
                order_text = "Traversal order: " + " → ".join(
                    [str(v + 1) for v in traversal.traversal_order]
                )
                traversal_info.config(text=order_text)

        status_label.config(text=status_text)

    def toggle_graph():
        if button_mode.cget("text") == "Switch to Undirected":
            button_mode.config(text="Switch to Directed")
            draw_all(directed=False)
        else:
            button_mode.config(text="Switch to Undirected")
            draw_all(directed=True)

    def start_bfs():
        if traversal.init_bfs() == -1:
            messagebox.showwarning(
                "No Start Vertex", "No vertex with outgoing edges found!"
            )
        draw_all()

    def start_dfs():
        if traversal.init_dfs() == -1:
            messagebox.showwarning(
                "No Start Vertex", "No vertex with outgoing edges found!"
            )
        draw_all()

    def next_step():
        if not traversal.started:
            messagebox.showwarning("Not Started", "Please start BFS or DFS first!")
            return
        traversal.next_step()
        draw_all()

    def reset_traversal():
        traversal.reset()
        traversal_info.config(text="")
        draw_all()

    button_mode = Button(
        button_frame, text="Switch to Undirected", command=toggle_graph
    )
    button_mode.pack(side="left", padx=5)

    Button(button_frame, text="BFS", command=start_bfs).pack(side="left", padx=5)
    Button(button_frame, text="DFS", command=start_dfs).pack(side="left", padx=5)
    Button(button_frame, text="Next Step", command=next_step).pack(side="left", padx=5)
    Button(button_frame, text="Reset", command=reset_traversal).pack(
        side="left", padx=5
    )

    def show_matrix_and_renumbering():
        if not traversal.completed and traversal.started:
            traversal.print_traversal_tree_matrix()
            traversal.print_renumbering()
        elif not traversal.started:
            messagebox.showinfo("Info", "First start traversal (BFS or DFS).")
        else:
            traversal.print_traversal_tree_matrix()
            traversal.print_renumbering()

    Button(
        button_frame,
        text="Show Matrix & Renumbering",
        command=show_matrix_and_renumbering,
    ).pack(side="left", padx=5)

    draw_all(directed=True)
    graph_window.mainloop()
