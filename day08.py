digits = open('input.txt').read().strip()

wide = 25
tall = 6

def get_layer_start(layer_id):
    return (layer_id) * wide * tall

def get_layer_end(layer_id):
    return (layer_id + 1) * wide * tall

def get_layer(layer_id):
    return digits[get_layer_start(layer_id):get_layer_end(layer_id)]

layers = []

i = 0
min_zero_cnt = wide * tall
min_zero_layer = 0
while get_layer_end(i) <= len(digits):
    layer = get_layer(i)
    layers.append(layer)

    zero_count = 0
    for digit in layer:
        if digit == '0':
            zero_count += 1

    if zero_count < min_zero_cnt:
        min_zero_cnt = zero_count
        min_zero_layer = i

    i += 1


found_layer = get_layer(min_zero_layer)

counter = {}
for digit in found_layer:
    if digit not in counter:
        counter[digit] = 0
    counter[digit] += 1

print(counter['1'] * counter['2'])

result_layer = ['2' for _ in range(wide * tall)]
for layer in layers:
    for i in range(wide * tall):
        if result_layer[i] == '2':
            result_layer[i] = layer[i]

result_layer = ['#' if digit == '1' else ' ' for digit in result_layer]

for i in range(tall):
    print(*result_layer[i * wide:(i + 1) * wide], sep='')