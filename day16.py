signal = open('input.txt').readline().strip()

offset = int(signal[:7])
signal = [int(digit) for digit in signal] * 10000
signal = signal[offset:]

for phase in range(100):
    partial_sum = 0
    for i in range(len(signal) - 1, -1, -1):
        partial_sum += signal[i]
        signal[i] = abs(partial_sum) % 10

print(*signal[:8], sep='')