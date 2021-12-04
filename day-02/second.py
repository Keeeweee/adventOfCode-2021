instructions = [line.rstrip('\n').split(' ') for line in open('data/data.txt')]

print(instructions)


position = [0, 0, 0]

for instruction in instructions:
    if instruction[0] == 'forward':
        position[0] += int(instruction[1])
        position[1] += position[2] * int(instruction[1])
    elif instruction[0] == 'down':
        position[2] += int(instruction[1])
    elif instruction[0] == 'up':
        position[2] -= int(instruction[1])

print(position[0] * position[1])