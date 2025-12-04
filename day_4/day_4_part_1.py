def add_to_ajacent_rolls(matrix: list[list[int]], row_idx: int, col_idx: int):
    for i in range(max(row_idx - 1, 0), min(row_idx + 2, len(matrix))):
        for j in range(max(col_idx - 1, 0), min(col_idx + 2, len(matrix[0]))):
            matrix[i][j] += 1
    matrix[row_idx][col_idx] -= 1


diagram = []

with open('day_4/input.txt', 'r') as file:
    for line in file:
        diagram.append(list(line.strip()))

rows = len(diagram)
columns = len(diagram[0])

ajacent_counts = [[0 for _ in range(columns)] for _ in range(rows)]
for i in range(rows):
    for j in range(columns):
        if diagram[i][j] == '@':
            add_to_ajacent_rolls(ajacent_counts, i, j)

accessible_rolls = 0
for i in range(rows):
    for j in range(columns):
        if diagram[i][j] == '@' and ajacent_counts[i][j] < 4:
            accessible_rolls += 1

print(f'Number of accessible rolls: {accessible_rolls}')
