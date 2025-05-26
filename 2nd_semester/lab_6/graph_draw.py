from draw_utils import *
from positions import generate_positions
from matrix_print import n, W, print_weight_matrix
from kruskal import Graph
from tkinter import Button, Tk, Canvas, Frame, Label, StringVar
import math

threshold = 1
positions = generate_positions()


def create_graph_window():
    graph_window = Tk()
    graph_window.title("Graph Visualization")

    main_frame = Frame(graph_window)
    main_frame.pack(fill="both", expand=True, padx=10, pady=10)

    info_panel = Frame(main_frame, bg="#f0f0f0")
    info_panel.pack(side="top", fill="x", pady=(0, 10))

    status_var = StringVar()
    status_var.set("Press 'Start' to begin")
    status_label = Label(
        info_panel,
        textvariable=status_var,
        font=("Arial", 10, "bold"),
        bg="#f0f0f0",
        padx=10,
        pady=5,
    )
    status_label.pack(fill="x")

    weight_var = StringVar()
    weight_var.set("Current weight: 0 | Total MST weight: 0")
    weight_label = Label(
        info_panel,
        textvariable=weight_var,
        font=("Arial", 10),
        bg="#f0f0f0",
        padx=10,
        pady=5,
    )
    weight_label.pack(fill="x")

    canvas = Canvas(main_frame, width=550, height=550, bg="white")
    canvas.pack(side="top", fill="both", expand=True)

    button_panel = Frame(main_frame)
    button_panel.pack(side="bottom", fill="x", pady=(10, 0))

    g = Graph(n)
    for i in range(n):
        for j in range(i + 1, n):
            if W[i][j] > 0:
                g.add_edge(i, j, W[i][j])

    mst_edges = g.kruskal_mst()
    total_weight = sum(w for u, v, w in mst_edges)

    traversal_path = []
    visited = [False] * n
    current_step = 0
    highlighted_edges = []
    current_vertex = None
    next_vertex = None
    mst_complete = False
    traversal_started = False

    VERTEX_RADIUS = 18
    WEIGHT_OFFSET = 35

    def calculate_weight_position(x1, y1, x2, y2, weight):
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2

        dx = x2 - x1
        dy = y2 - y1
        length = math.hypot(dx, dy)

        if length == 0:
            return mid_x, mid_y

        perp_x = -dy / length
        perp_y = dx / length

        offset = 20
        final_x = mid_x + perp_x * offset
        final_y = mid_y + perp_y * offset

        return final_x, final_y

    def draw_edge_weight(x1, y1, x2, y2, weight, is_active=False):
        weight_x, weight_y = calculate_weight_position(x1, y1, x2, y2, weight)

        bg_color = "#ff4444" if is_active else "white"
        fg_color = "white" if is_active else "black"
        outline = "black" if is_active else "#888888"

        canvas.create_rectangle(
            weight_x - 15,
            weight_y - 10,
            weight_x + 15,
            weight_y + 10,
            fill=bg_color,
            outline=outline,
            width=1,
        )
        canvas.create_text(
            weight_x,
            weight_y,
            text=str(weight),
            font=("Arial", 8, "bold"),
            fill=fg_color,
            tags="weight",
        )

    def build_traversal_path():
        nonlocal traversal_path, visited
        traversal_path = []
        visited = [False] * n
        stack = [0]
        visited[0] = True
        traversal_path.append(0)

        adj = [[] for _ in range(n)]
        for u, v, w in mst_edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        while stack:
            u = stack.pop()
            for v, w in sorted(adj[u], key=lambda x: x[1]):
                if not visited[v]:
                    visited[v] = True
                    traversal_path.append((u, v, w))
                    traversal_path.append(v)
                    stack.append(v)

    def draw_graph():
        nonlocal mst_complete
        canvas.delete("all")

        drawn_edges = set()
        inactive_weights = []
        active_weights = []

        for i in range(n):
            for j in range(i + 1, n):
                if W[i][j] > 0 and W[i][j] != math.inf:
                    x1, y1 = positions[i]
                    x2, y2 = positions[j]
                    weight = W[i][j]

                    edge_color = "#cccccc"
                    width = 1
                    is_active = (i, j) in highlighted_edges or (
                        j,
                        i,
                    ) in highlighted_edges

                    if is_active:
                        edge_color = "#ff4444"
                        width = 3

                    if i == j:
                        draw_self_loop(
                            canvas,
                            x1,
                            y1,
                            directed=False,
                            color=edge_color,
                            width=width,
                        )
                    elif is_crossing_vertex(x1, y1, x2, y2, positions, {i, j}):
                        draw_arc(
                            canvas,
                            x1,
                            y1,
                            x2,
                            y2,
                            directed=False,
                            color=edge_color,
                            width=width,
                        )
                    else:
                        draw_line(canvas, x1, y1, x2, y2, color=edge_color, width=width)

                    drawn_edges.add((min(i, j), max(i, j)))

        for i, j in drawn_edges:
            weight = max(W[i][j], W[j][i])
            if weight > 0:
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                is_active = (i, j) in highlighted_edges or (j, i) in highlighted_edges
                if is_active:
                    active_weights.append((x1, y1, x2, y2, weight, True))
                else:
                    inactive_weights.append((x1, y1, x2, y2, weight, False))

        for x1, y1, x2, y2, weight, is_active in inactive_weights:
            draw_edge_weight(x1, y1, x2, y2, weight, is_active)

        for x1, y1, x2, y2, weight, is_active in active_weights:
            draw_edge_weight(x1, y1, x2, y2, weight, is_active)

        for i, (x, y) in enumerate(positions):
            color = "#aaccff"
            if i == current_vertex:
                color = "#ffff44"
            elif i == next_vertex:
                color = "#ffaa44"

            canvas.create_oval(
                x - VERTEX_RADIUS,
                y - VERTEX_RADIUS,
                x + VERTEX_RADIUS,
                y + VERTEX_RADIUS,
                outline="black",
                width=2,
                fill=color,
            )
            canvas.create_text(
                x, y, text=str(i + 1), font=("Arial", 10, "bold"), fill="black"
            )

        if not traversal_started:
            status_var.set("Press 'Start' to begin")
        elif current_step == 0 and traversal_started:
            status_var.set("Starting from vertex 1")
        elif current_step < len(traversal_path):
            if isinstance(traversal_path[current_step - 1], tuple):
                u, v, w = traversal_path[current_step - 1]
                status_var.set(
                    f"Step {current_step}: Adding edge {u+1}-{v+1} (weight {w})"
                )
            else:
                v = traversal_path[current_step - 1]
                status_var.set(f"Step {current_step}: Visiting vertex {v+1}")
        else:
            status_var.set(f"Minimum spanning tree found! Total weight: {total_weight}")
            mst_complete = True

        current_w = sum(
            w
            for step in traversal_path[:current_step]
            if isinstance(step, tuple)
            for u, v, w in [step]
        )
        weight_var.set(
            f"Current weight: {current_w} | Total MST weight: {total_weight}"
        )

    def start_traversal():
        nonlocal traversal_started
        if not traversal_started:
            traversal_started = True
            build_traversal_path()
            next_step()

    def next_step():
        nonlocal current_step, current_vertex, next_vertex, mst_complete
        if not traversal_started:
            start_traversal()
            return

        if current_step < len(traversal_path):
            if isinstance(traversal_path[current_step], tuple):
                u, v, w = traversal_path[current_step]
                highlighted_edges.append((u, v))
                current_vertex = u
                next_vertex = v
            else:
                v = traversal_path[current_step]
                current_vertex = v
                next_vertex = None
            current_step += 1
        elif not mst_complete:
            mst_complete = True
        draw_graph()

    def reset():
        nonlocal current_step, highlighted_edges, current_vertex
        nonlocal next_vertex, mst_complete, traversal_started
        current_step = 0
        highlighted_edges = []
        current_vertex = None
        next_vertex = None
        mst_complete = False
        traversal_started = False
        draw_graph()

    Button(
        button_panel,
        text="Start",
        command=start_traversal,
        bg="#4CAF50",
        fg="white",
        font=("Arial", 10, "bold"),
    ).pack(side="left", padx=5, ipadx=10)
    Button(
        button_panel,
        text="Next Step",
        command=next_step,
        bg="#2196F3",
        fg="white",
        font=("Arial", 10, "bold"),
    ).pack(side="left", padx=5, ipadx=10)
    Button(
        button_panel,
        text="Reset",
        command=reset,
        bg="#f44336",
        fg="white",
        font=("Arial", 10, "bold"),
    ).pack(side="left", padx=5, ipadx=10)

    print("\n" + "=" * 50)
    print_weight_matrix()

    draw_graph()
    graph_window.mainloop()
