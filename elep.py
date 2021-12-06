import os, sys

class ElephantProgram:
    def __init__(self, lines):
        self.n = int(lines[0])
        self.weights = [int(x) for x in lines[1].split()]
        self.original = [int(x) for x in lines[2].split()]
        self.moved = [int(x) for x in lines[3].split()]

    def get_simple_cycles(self):
        visited = [False for i in range(self.n)]
        global_minimum = min(self.weights)
        w = 0
        for i in range(self.n-1):
            if not visited[i]:
                c = 0
                cycle_sum = 0
                cycle_minimum = 6501
                x = i
                while True:
                    visited[x] = True
                    x = self.moved[x]
                    cycle_minimum = min(self.weights[x-1], cycle_minimum)
                    cycle_sum = cycle_sum + self.weights[x-1]
                    c = c + 1
                    if visited[self.original.index(x)] == True:
                        break
                    else:
                        x = self.original.index(x)
                if cycle_sum + (c-2) * cycle_minimum < cycle_sum + cycle_minimum + (c+1) * global_minimum:
                    w = w + cycle_sum + (c-2) * cycle_minimum
                else:
                    w = w + cycle_sum + cycle_minimum + (c+1) * global_minimum
                print(sum(visited))
        return w

program = ElephantProgram(sys.stdin.readlines())
print(program.get_simple_cycles())