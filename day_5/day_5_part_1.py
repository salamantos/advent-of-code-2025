ranges = []
ingredients = []
is_blank_line_occurred = False

with open('day_5/input.txt', 'r') as file:
    for line in file:
        stripped_line = line.strip()
        
        if stripped_line == '':
            is_blank_line_occurred = True
            continue
        
        if not is_blank_line_occurred:
            start, end = stripped_line.split('-')
            ranges.append(range(int(start), int(end) + 1))
        else:
            ingredients.append(int(stripped_line))

total_fresh = 0
for ingredient in ingredients:
    for r in ranges:
        if ingredient in r:
            total_fresh += 1
            break

print(f'Total fresh ingrediests: {total_fresh}')
