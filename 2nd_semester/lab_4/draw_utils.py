import math
import tkinter as tk


def draw_arrow(canvas, x1, y1, x2, y2, radius=25):
    dx, dy = x2 - x1, y2 - y1
    dist = math.hypot(dx, dy)
    if dist == 0:
        return
    dx, dy = dx / dist, dy / dist
    start_x, start_y = x1 + dx * radius, y1 + dy * radius
    end_x, end_y = x2 - dx * radius, y2 - dy * radius
    canvas.create_line(
        start_x, start_y, end_x, end_y, arrow=tk.LAST, width=2, fill="darkblue"
    )


def draw_line(canvas, x1, y1, x2, y2, radius=25):
    dx, dy = x2 - x1, y2 - y1
    dist = math.hypot(dx, dy)
    dx, dy = dx / dist, dy / dist
    start_x, start_y = x1 + dx * radius, y1 + dy * radius
    end_x, end_y = x2 - dx * radius, y2 - dy * radius
    canvas.create_line(start_x, start_y, end_x, end_y, width=2, fill="green")


def draw_arc(canvas, x1, y1, x2, y2, radius=25, directed=True):
    dx, dy = x2 - x1, y2 - y1
    dist = math.hypot(dx, dy)
    if dist == 0:
        return
    dx, dy = dx / dist, dy / dist
    start_x, start_y = x1 + dx * radius, y1 + dy * radius
    end_x, end_y = x2 - dx * radius, y2 - dy * radius
    mx, my = dy, -dx
    norm = math.hypot(mx, my)
    mx, my = mx / norm, my / norm
    control_x = (start_x + end_x) / 2 + mx * 60
    control_y = (start_y + end_y) / 2 + my * 60
    canvas.create_line(
        start_x,
        start_y,
        control_x,
        control_y,
        end_x,
        end_y,
        smooth=True,
        width=2,
        fill="darkblue" if directed else "green",
        arrow=tk.LAST if directed else None,
    )


def draw_self_loop(canvas, x, y, directed=True):
    loop_radius = 20
    canvas_width, canvas_height = int(canvas["width"]), int(canvas["height"])
    center_x, center_y = canvas_width // 2, canvas_height // 2
    margin = 100

    if abs(y - center_y) < margin:
        if x < center_x:
            bbox, arrow_start, arrow_end, angle = (
                (x - 55, y - loop_radius, x - 15, y + loop_radius),
                (x - 23, y - loop_radius + 5),
                (x - 20, y - loop_radius + 7),
                45,
            )
        else:
            bbox, arrow_start, arrow_end, angle = (
                (x + 15, y - loop_radius, x + 55, y + loop_radius),
                (x + 23, y + loop_radius - 35),
                (x + 20, y + loop_radius - 33),
                225,
            )
    elif y < center_y:
        bbox, arrow_start, arrow_end, angle = (
            (x - loop_radius, y - 55, x + loop_radius, y - 15),
            (x - 16, y - loop_radius - 5),
            (x - 13, y - loop_radius),
            -45,
        )
    else:
        bbox, arrow_start, arrow_end, angle = (
            (x - loop_radius, y + 15, x + loop_radius, y + 55),
            (x - loop_radius + 4, y + 25),
            (x - loop_radius + 7, y + 20),
            135,
        )

    canvas.create_arc(
        bbox,
        start=angle,
        extent=270,
        style=tk.ARC,
        width=2,
        outline="darkblue" if directed else "green",
    )

    if directed:
        canvas.create_line(
            *arrow_start, *arrow_end, width=2, fill="darkblue", arrow=tk.LAST
        )


def is_crossing_vertex(x1, y1, x2, y2, positions, skip_indices, radius=25):
    for i, (cx, cy) in enumerate(positions):
        if i in skip_indices:
            continue
        num = abs((y2 - y1) * cx - (x2 - x1) * cy + x2 * y1 - y2 * x1)
        den = math.hypot(y2 - y1, x2 - x1)
        if den == 0:
            continue
        dist = num / den
        if dist < radius:
            dot1 = (cx - x1) * (x2 - x1) + (cy - y1) * (y2 - y1)
            dot2 = (cx - x2) * (x1 - x2) + (cy - y2) * (y1 - y2)
            if dot1 > 0 and dot2 > 0:
                return True
    return False


def draw_graph(canvas, positions, radius=25):
    for i, (x, y) in enumerate(positions):
        canvas.create_oval(
            x - radius,
            y - radius,
            x + radius,
            y + radius,
            fill="lightyellow",
            outline="black",
            width=2,
        )
        canvas.create_text(
            x, y, text=str(i + 1), font=("Times New Roman", 12, "bold"), fill="black"
        )
