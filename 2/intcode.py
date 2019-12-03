import sys


intcode_operations = {
    1: {'values': 4, 'function': lambda x, y: x + y},
    2: {'values': 4, 'function': lambda x, y: x * y},
}
def execute(memory, instruction_pointer):
    """
    Executes the given instruction and returns the new instruction pointer.
    """

    operation = intcode_operations[memory[instruction_pointer]]

    # Get the correct number of parameters
    instruction = memory[instruction_pointer:instruction_pointer + operation['values']]

    # Perform the operationn
    memory[instruction[3]] = operation['function'](
        memory[instruction[1]],
        memory[instruction[2]]
    )

    # Return new pointer location
    return instruction_pointer + operation['values']

def run(memory):
    instruction_pointer = 0
    while memory[instruction_pointer] != 99:
        instruction_pointer = execute(memory, instruction_pointer)


# Read in the memory
initial_state = sys.stdin.readline()
initial_memory = [int(c) for c in initial_state.split(',')]

# Modification to resolve 1202 Error
memory = initial_memory.copy()
memory[1] = 12
memory[2] = 2

# Run it
run(memory)

# Print Final Result
print(f'Initial Result - {memory[0]}')

# Brute Force Part 2
for noun in range(100):
    for verb in range(100):
        memory = initial_memory.copy()
        memory[1] = noun
        memory[2] = verb
        run(memory)
        result = memory[0]

        if memory[0] == 19690720:
            output = 100 * noun + verb
            print(f'Result found for noun {noun} and verb {verb}, final result is {output}')
