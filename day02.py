from copy import copy

with open('input.txt') as input_file:
    numbers_og = input_file.readline()
    numbers_og = numbers_og.strip().split(',')

for i in range(0, len(numbers_og)):
    numbers_og[i] = int(numbers_og[i])

for noun in range(0, 100):
    for verb in range(0, 100):
        numbers = copy(numbers_og)

        numbers[1] = noun
        numbers[2] = verb

        it = 0
        steps = 0
        while it < len(numbers):
            steps += 1

            if steps > 100:
                break
            
            if numbers[it] == 1:
                numbers[numbers[it + 3]] = numbers[numbers[it + 1]] + numbers[numbers[it + 2]]
                it += 4
            elif numbers[it] == 2:
                numbers[numbers[it + 3]] = numbers[numbers[it + 1]] * numbers[numbers[it + 2]]
                it += 4
            elif numbers[it] == 99:
                break

        if numbers[0] == 19690720:
            print("{}{}".format(noun, verb))