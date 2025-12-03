BATTERIES_PACK_COUNT = 12


def find_max_battery(bank: str, from_idx: int, to_idx: int):
    max_joltage = 0
    idx = 0
    for i in range(from_idx, to_idx):
            if int(bank[i]) > max_joltage:
                idx = i
                max_joltage = int(bank[i])
    
    return idx, max_joltage


with open('day_3/input.txt', 'r') as file:
    total_joltage = 0
    for bank in file:
        bank = bank.strip()
        
        battery_idx = -1
        bank_joltages = []
        for num in range(1, BATTERIES_PACK_COUNT + 1):
            battery_idx, battery_joltage = find_max_battery(bank, battery_idx + 1, len(bank) - (BATTERIES_PACK_COUNT - num))
            bank_joltages.append(str(battery_joltage))
        
        bank_joltage = int(''.join(bank_joltages))
        total_joltage += bank_joltage

print(f'Total joltage: {total_joltage}')
