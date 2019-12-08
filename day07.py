from util.intcode import IntcodeMachine
import itertools

def_mem = [int(arg) for arg in open('input.txt').read().split(',')]

# phases = [0, 1, 2, 3, 4]
phases = [5, 6, 7, 8, 9]

end_signal = 0
for phase_perm in itertools.permutations(phases):    
    amps = [IntcodeMachine(def_mem, phase_perm[i]) for i in range (5)]
    buffer = [0]
    i = 0

    while True:
        amps[i].clear_output()
        amps[i].add_input(buffer)
        amps[i].run()
        buffer = amps[i].output

        if amps[-1].reached_exit:
            end_signal = max(end_signal, buffer[-1])
            break

        i = (i + 1) % 5

print(end_signal)