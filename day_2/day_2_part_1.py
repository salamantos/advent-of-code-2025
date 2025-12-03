with open('day_2/input.txt', 'r') as file:
    content = file.read().strip()

invalid_codes = []
intervals = content.split(',')
for interval in intervals:
    start, end = interval.split('-')
    if len(start) % 2 == 0:
        base = int(start[:len(start)//2])
    else:
        base = int('1' + '0' * (len(start) // 2))
    
    while True:
        code = int(str(base) * 2)
        if code > int(end):
            break
        if code >= int(start):
            invalid_codes.append(code)
        base += 1

print(f'Invalid IDs: {invalid_codes}')
print(f'Invalid IDs sum: {sum(invalid_codes)}')
