from util.intcode import IntcodeMachine
import os
import numpy

def visualize():
    os.system('cls')
    for i in range(25):
        for j in range(40):
            if (j, i) in walls: print('█', end='')
            elif (j, i) in blocks: print('■', end='')
            elif (j, i) == paddle: print('_', end='')
            elif (j, i) == ball: print('o', end='')
            else: print(' ', end='')
        print()
    print(score)


mem = [int(number) for number in open('input.txt').readline().split(',')]

score = 0

arcade = IntcodeMachine(mem)
arcade.memory[0] = 2

walls = set()
blocks = set()
paddle = ()
ball = ()

while not arcade.reached_exit:
    arcade.clear_output()
    arcade.run()
    output = arcade.output

    for i in range(0, len(output), 3):
        pos = (output[i], output[i + 1])
        arg = output[i + 2]
        
        if pos == (-1, 0): score = arg
        elif arg == 0:
            if pos in walls: walls.remove(pos)
            if pos in blocks: blocks.remove(pos)
        elif arg == 1: walls.add(pos)
        elif arg == 2: blocks.add(pos)
        elif arg == 3: paddle = pos
        elif arg == 4: ball = pos

    arcade.add_input([numpy.sign(ball[0] - paddle[0])])

    visualize()

print(score)