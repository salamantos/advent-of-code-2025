def find_for_repetitions(start: int, end: int, repetitions: int) -> list[int]:
    invalid_codes_for_repetitions = []
    
    if len(start) % repetitions == 0:
        base = int(start[:len(start)//repetitions])
    else:
        base = int('1' + '0' * (len(start) // repetitions))
    
    while True:
        code = int(str(base) * repetitions)
        if code > int(end):
            break
        if code >= int(start):
            invalid_codes_for_repetitions.append(code)
        base += 1
        
    return invalid_codes_for_repetitions


with open('day_2/input.txt', 'r') as file:
    content = file.read().strip()

invalid_codes = []
intervals = content.split(',')
for interval in intervals:
    start, end = interval.split('-')
    
    found_set = set()
    for repetitions in range(2, len(end) + 1):
        found_set.update(find_for_repetitions(start, end, repetitions))
    
    invalid_codes.extend(found_set)

print(f'Invalid IDs: {invalid_codes}')
print(f'Invalid IDs sum: {sum(invalid_codes)}')
