def has_consecutive(number):
    prev_digit = number % 10
    number //= 10

    no_consec = 0

    consecs = set()

    while number > 0:
        cur_digit = number % 10
        number //= 10

        if cur_digit == prev_digit:
            no_consec += 1
        else:
            consecs.add(no_consec)
            no_consec = 0

        prev_digit = cur_digit

    consecs.add(no_consec)
    if 1 in consecs:
        return True
    else:
        return False


def has_increasing(number):
    has_inc = True

    prev_digit = number % 10
    number //= 10

    while number > 0:
        cur_digit = number % 10
        number //= 10

        if cur_digit > prev_digit:
            has_inc = False

        prev_digit = cur_digit

    return has_inc

with open('input.txt') as input_file:
    line = input_file.readline()
    line = line.split('-')
    lbound = int(line[0])
    rbound = int(line[1])

counter = 0
for number in range(lbound, rbound + 1):
    if has_consecutive(number) and has_increasing(number):
        counter += 1

print(counter)
