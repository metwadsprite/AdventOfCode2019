from util.intcode import IntcodeMachine

mem = [int(number) for number in open('input.txt').readline().split(',')]

def in_beam(pos):
    beam = IntcodeMachine(mem, [int(pos.real), int(pos.imag)])
    beam.run()
    if beam.output[0]: return True
    else: return False


def p1():
    counter = 0
    for i in range(50):
        for j in range(50):
            if  in_beam(complex(i, j)): counter += 1
    return counter


def p2():
    pos = complex(100, 200)
    while True:
        if not in_beam(pos):
            pos += 1
        else:
            if in_beam(complex(pos.real + 99, pos.imag - 99)):
                return complex(pos.real, pos.imag - 99)
            pos += 1j


sol = p2()
print(int(sol.real * 10000 + sol.imag))