import itertools
import math

lines = [cds.strip('<').strip('>\n').split(', ') for cds in open('input.txt').readlines()]
loc = [[int(cd.split('=')[1]) for cd in line] for line in lines]
vel = [[0, 0, 0] for _ in loc]
pot_eng = [0 for _ in loc]
kin_eng = [0 for _ in loc]
tot_eng = [0 for _ in loc]

no = len(loc)

def lcm(a, b):
    return a // math.gcd(a, b) * b


def apply_gravity():
    for src, tar in itertools.permutations(range(no), 2):
        for cd in range(3):
            if loc[src][cd] < loc[tar][cd]:
                vel[src][cd] += 1
                vel[tar][cd] -= 1
            elif loc[src][cd] > loc[tar][cd]:
                vel[src][cd] -= 1
                vel[src][cd] += 1
    
    for i in range(no):
        kin_eng[i] = 0
        for cd in range(3):
            kin_eng[i] += abs(vel[i][cd])


def apply_vel():
    for i in range(no):
        for cd in range(3):
            loc[i][cd] += vel[i][cd]
    
    for i in range(no):
        pot_eng[i] = 0
        for cd in range(3):
            pot_eng[i] += abs(loc[i][cd])
        
        tot_eng[i] = kin_eng[i] * pot_eng[i]


def step():
    apply_gravity()
    apply_vel()


seen = [set() for _ in range(no)]
found_step = [None for _ in range(no)]

cur_step = 0
while not found_step[0] or not found_step[1] or not found_step[2]:
    step()

    for cd in range(3):
        if not found_step[cd]:
            comb = str([[loc[i][cd], vel[i][cd]] for i in range(no)])
            if comb in seen[cd]: found_step[cd] = cur_step
            seen[cd].add(comb)
    
    cur_step += 1

print(lcm(found_step[0], lcm(found_step[1], found_step[2])))