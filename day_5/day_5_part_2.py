ranges = []

with open('day_5/input.txt', 'r') as file:
    for line in file:
        stripped_line = line.strip()
        
        if stripped_line == '':
            break
        
        start, end = stripped_line.split('-')
        ranges.append([int(start), int(end)])

ranges.sort()
for i in range(len(ranges)):
    if ranges[i][0] > ranges[i][1]:
        continue
    
    for j in range(i+1, len(ranges)):
        if ranges[j][0] > ranges[j][1]:
            continue
        
        if ranges[i][1] >= ranges[j][0]:
            ranges[j][0] = ranges[i][1] + 1

total_fresh = 0
for r in ranges:
    if r[0] > r[1]:
        continue
    
    total_fresh += r[1] - r[0] + 1

print(f'Total fresh ingrediests: {total_fresh}')
