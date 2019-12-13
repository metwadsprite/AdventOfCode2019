from util.intcode import IntcodeMachine
import os

mem = [int(number) for number in open('input.txt').readline().split(',')]

score = 0

arcade = IntcodeMachine(mem)
arcade.memory[0] = 2

while True:
    arcade.run()
    output = arcade.output

    walls = set()
    blocks = set()
    paddle = ()
    ball = ()

    for i in range(0, len(output), 3):
        pos = (output[i], output[i + 1])
        if pos[0] == -1 and pos[1] == 0:
            score = output[i + 2]

        if output[i + 2] == 0:
            if pos in walls: walls.remove(pos)
            if pos in blocks: blocks.remove(pos)
        if output[i + 2] == 1: walls.add(pos)
        if output[i + 2] == 2: blocks.add(pos)
        if output[i + 2] == 3: paddle = pos
        if output[i + 2] == 4: ball = pos

    # os.system('cls')
    # for i in range(40):
    #     for j in range(50):
    #         if (i, j) in walls: print('█', end='')
    #         elif (i, j) in blocks: print('#', end='')
    #         elif (i, j) == paddle: print('|', end='')
    #         elif (i, j) == ball: print('O', end='')
    #         else: print(' ', end='')
    #     print()
    # print(score)

    # print(len(blocks))
    if len(blocks) == 0:
        print(score)
        break

    if paddle[0] < ball[0]: arcade.add_input([1])
    elif paddle[0] > ball[0]: arcade.add_input([-1])
    else: arcade.add_input([0])