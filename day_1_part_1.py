position = 50
zero_positions = 0

with open('input.txt', 'r') as file:
    for line in file:
        command = line.strip()
        direction = 1 if command[0] == 'R' else -1
        number_of_steps = int(command[1:])
        
        position = (position + direction * number_of_steps) % 100
        if position == 0:
            zero_positions += 1

print(f'Zero positions encountered: {zero_positions}')
