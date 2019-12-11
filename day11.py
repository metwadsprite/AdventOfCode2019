from util.intcode import IntcodeMachine

mem = [int(number) for number in open('input.txt').readline().split(',')]

brain = IntcodeMachine(mem, [1])
painted_black = set()
painted_white = set()
rotate_right = {'up': 'right', 'right': 'down', 'down': 'left', 'left': 'up'}
rotate_left = {'up': 'left', 'left': 'down', 'down': 'right', 'right': 'up'}
moves = {'up': -1j, 'right': 1, 'down': 1j, 'left': -1}

pos = 0
rot = 'up'

while not brain.reached_exit:
    brain.clear_output()
    brain.run()
    output = brain.output
    
    if output[0] == 0:
        painted_black.add(pos)
        if pos in painted_white: painted_white.remove(pos)
    else:
        painted_white.add(pos)
        if pos in painted_black: painted_black.remove(pos)
    
    if output[1] == 0: rot = rotate_left[rot]
    elif output[1] == 1: rot = rotate_right[rot]

    pos += moves[rot]

    if pos in painted_white: brain.add_input([1])
    else: brain.add_input([0])

print(len(painted_black | painted_white))

for i in range(-1, 7):
    for j in range(0, 41):
        if complex(j, i) in painted_white:
            print('█', end='')
        else:
            print(' ', end='')
    print()