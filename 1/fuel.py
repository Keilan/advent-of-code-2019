import sys

def compute_fuel(mass):
    return mass // 3 - 2

def compute_additional_fuel(mass):
    """
    Solves part 2 by computing the fuel required for the fuel.
    """
    total_additional = 0
    additional_fuel = compute_fuel(mass)
    while additional_fuel > 0:
        total_additional += additional_fuel
        additional_fuel = compute_fuel(additional_fuel)
    return total_additional

fuel_sum = 0
for line in sys.stdin:
    mass = int(line)
    module_fuel = compute_fuel(mass)
    fuel_sum += module_fuel

    additional_fuel = compute_additional_fuel(module_fuel)
    fuel_sum += additional_fuel

print(f'The fuel sum is {fuel_sum}')
