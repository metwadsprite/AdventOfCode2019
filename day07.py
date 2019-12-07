from IntcodeSim import IntcodeSim
import itertools

def_mem = [int(arg) for arg in open('input.txt').read().split(',')]

end_signal = 0

# phases = [0, 1, 2, 3, 4]
phases = [5, 6, 7, 8, 9]

for phase_perm in itertools.permutations(phases):    
    amps = [IntcodeSim(def_mem, phase_perm[i]) for i in range (5)]
    buffer = [0]
    i = 0

    while True:
        amps[i].clear_output()
        amps[i].provide_input(buffer)
        amps[i].run()
        buffer = amps[i].output

        i = (i + 1) % 5
        
        if amps[4].reach_exit:
            end_signal = max(end_signal, max(buffer))
            break

print(end_signal)