def generate_positions():
    positions = []
    spacing = 120
    offset = 100

    for i in range(3):
        positions.append((offset + i * spacing, offset))
    for i in range(3):
        positions.append((offset + 3 * spacing, offset + i * spacing))
    for i in range(3, 0, -1):
        positions.append((offset + i * spacing, offset + 3 * spacing))
    for i in range(3, 0, -1):
        positions.append((offset, offset + i * spacing))

    return positions
