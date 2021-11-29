import os, sys

def test():
    in_list = [x for x in os.listdir() if x.endswith('.in')]
    out_list = [x for x in os.listdir() if x.endswith('.out')]
    true_list = []
    for i in range(len(in_list)):
        lines = open(in_list[i]).readlines()
        program = ElephantProgram(lines)
        if program.run() == int(open(out_list[i]).read()):
            true_list.append(True)
    assert all(true_list) == True


class ElephantProgram:
    def __init__(self, lines):
        self.n = int(lines[0])
        self.weights = [int(x) for x in lines[1].split()]
        self.original = [int(x) for x in lines[2].split()]
        self.moved = [int(x) for x in lines[3].split()]

    def run(self):
        return self.cycle_parameters(self.get_simple_cycles())


    def get_simple_cycles(self):
        visited = [False for i in range(self.n)]
        cycle = {}
        for i in range(self.n):
            cycle[i] = []
            if not visited[i]:
                x = i
                while not visited[x]:
                    visited[x] = True
                    cycle[i].append(self.original[x])
                    x = self.moved.index(self.original[x])
                    print(visited)
        return cycle

    # Wyznaczanie parametrów cykli
    def cycle_parameters(self, lines):
        cycles_dict = self.get_simple_cycles()
        w = 0
        for i in range(len(cycles_dict)):
            cycle_sum = 0
            cycle_minimum, global_minimum = 6500, min(self.weights)
            if len(cycles_dict[i]) > 1:
                for e in cycles_dict[i]:
                    elephant_weight = self.weights[e - 1]
                    cycle_sum = cycle_sum + elephant_weight
                    cycle_minimum = min(cycle_minimum, elephant_weight)

                global_minimum = min(global_minimum, cycle_minimum)
                method_one = cycle_sum + (len(cycles_dict[i]) - 2) * cycle_minimum
                method_two = cycle_sum + cycle_minimum + (len(cycles_dict[i]) + 1) * global_minimum

                w = w + min(method_one, method_two)

        return w

program = ElephantProgram(sys.stdin.readlines())
print(program.run())