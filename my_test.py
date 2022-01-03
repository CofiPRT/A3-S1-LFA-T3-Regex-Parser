from DFA import DFA
from NFA import NFA

input_file = open("my_input", "r")
output_file = open("my_output", "w")

stateCount = int(input_file.readline().strip())
finalStates = set(map(int, input_file.readline().strip().split(" ")))
delta = dict()

alphabet = set()

for line in input_file:
    transition = line.strip().split(" ")

    state = int(transition[0])
    char = transition[1]

    alphabet.add(char)

    delta[(state, char)] = frozenset(map(int, transition[2:]))

nfaInstance = NFA(
    state_count=stateCount,
    final_states=frozenset(finalStates),
    alphabet=frozenset(alphabet),
    delta=delta
)

nfaInstance.render_graphviz()
