import math
import time
import itertools

def get_angle(p1, p2):
    return math.atan2(p1[1] - p2[1], p1[0] - p2[0])

def check_visible(p1, p2):
    for blocker in asteroids:
        if blocker == p1 or blocker == p2: continue
        if is_dead[blocker]: continue

        if get_angle(p1, blocker) == get_angle(blocker, p2) == get_angle(p1, p2):
            return False

    return True

def are_alive():
    no_alive = len([1 for roid in asteroids if not is_dead[roid]])
    return False if no_alive == 1 else True

def angle_sort(point):
    return get_angle(station, point)

ast_map = open('input.txt').readlines()
asteroids = []

for i in range(len(ast_map)):
    for j in range(len(ast_map[i])):
        if ast_map[i][j] == '#':
            asteroids.append((j, i))

visible = {asteroid: [] for asteroid in asteroids}
is_dead = {asteroid: False for asteroid in asteroids}

def p1():
    for src, tar in itertools.combinations(asteroids, 2):
        if check_visible(src, tar):
            visible[src].append(tar)
            visible[tar].append(src)

    max_val = 0
    for key, value in visible.items():
        if len(value) > max_val:
            max_val = len(value)
            max_key = key

    print(max_key, max_val)
    return asteroids.index(max_key)


station = asteroids[p1()]
def p2():
    no_kill = 1

    while are_alive():
        visible[station] = []

        for tar in asteroids:
            if tar == station: continue
            if check_visible(station, tar) and not is_dead[tar]: visible[station].append(tar)
        
        partition = 0
        visible[station].sort(key=angle_sort)
        top = math.pi / 2
        for tar in visible[station]:
            if get_angle(station, tar) >= top:
                partition = visible[station].index(tar)
                break

        i = partition
        while True:
            if no_kill == 200:
                print(visible[station][i])
                return
            is_dead[visible[station][i]] = True

            no_kill += 1

            i = (i + 1) % len(visible[station])
            if i == partition: break

p2()