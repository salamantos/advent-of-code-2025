total_joltage = 0

with open('day_3/test_input.txt', 'r') as file:
    for bank in file:
        bank = bank.strip()
        
        first_battery_idx = 0
        first_battery_joltage = 0
        for i in range(len(bank) - 1):
            if int(bank[i]) > first_battery_joltage:
                first_battery_idx = i
                first_battery_joltage = int(bank[i])
        
        second_battery_joltage = 0
        for i in range(first_battery_idx + 1, len(bank)):
            if int(bank[i]) > second_battery_joltage:
                second_battery_joltage = int(bank[i])
        
        bank_joltage = int(str(first_battery_joltage) + str(second_battery_joltage))
        total_joltage += bank_joltage

print(f'Total joltage: {total_joltage}')
