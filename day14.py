from math import ceil
import copy

lines = open('input.txt').readlines()

react = {}

for line in lines:
    line = line.split('=>')

    result = list(reversed(line[1].strip().split(' ')))
    result[1] = int(result[1])
    result = tuple(result)

    reqs = line[0].strip().split(', ')
    reqs = [list(reversed(req.split(' '))) for req in reqs]
    reqs = [[req[0], int(req[1])] for req in reqs]

    react[result] = reqs


def get_requirements(elem, amt=1):
    for key, val in react.items():
        if key[0] == elem:
            return {req[0]: ceil(amt / key[1]) * req[1] for req in val}


def get_create(elem, amt=1):
    for key, val in react.items():
        if key[0] == elem:
            return ceil(amt / key[1]) * key[1]


def produce(elem, amt=1):
    if elem == 'ORE':
        inventory[elem] += amt
        produced[elem] += amt
        return

    reqs = get_requirements(elem, amt)

    for key, val in reqs.items():
        if inventory[key] < val: produce(key, val - inventory[key])
        inventory[key] -= val
    
    inventory[elem] += get_create(elem, amt)
    produced[elem] += get_create(elem, amt)


inventory = {key[0]: 0 for key, _ in react.items()}
inventory['ORE'] = 0
produced = {key[0]: 0 for key, _ in react.items()}
produced['ORE'] = 0

produce('FUEL', 1)
print(produced['ORE'])


inventory = {key[0]: 0 for key, _ in react.items()}
inventory['ORE'] = 0
produced = {key[0]: 0 for key, _ in react.items()}
produced['ORE'] = 0

produce('FUEL', 6326857)
print(produced['ORE'])
print(produced['ORE'] < 1000000000000)