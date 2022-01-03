from sys import stderr
from typing import FrozenSet, Dict, Tuple
from DFA import DFA
try:
    import graphviz
except ImportError:
    graphviz = None

epsilon = 'eps'
State = int
Symbol = chr


class NFA:
    def __init__(self, state_count: int,
                 alphabet: FrozenSet[Symbol],
                 final_states: FrozenSet[State],
                 delta: Dict[Tuple[State, Symbol], FrozenSet[State]],
                 name: str = 'My NFA'):
        self.state_count = state_count
        self.states = set(range(state_count))
        self.alphabet = alphabet
        self.initialState = 0

        extra_states = final_states.difference(self.states)
        if extra_states:
            message = "Could not init DFA: "
            message += "The final states is not a subset of the states set. "
            message += "(Extra states: " + str(sorted(extra_states)) + ")"
            raise Exception(message)

        self.final_states = final_states

        for curr_state in self.states:
            for curr_char in self.alphabet:
                dest_states = delta.get((curr_state, curr_char))

                if dest_states:
                    extra_states = dest_states.difference(self.states)

                    if extra_states:
                        message = "Could not init DFA: "
                        message += "The delta function is not valid. "
                        message += "(Transition from state " + str(curr_state)
                        message += " on character " + str(curr_char)
                        message += " leads to non-existent states " + str(extra_states) + ")"
                        raise Exception(message)

        self.delta = delta
        self.epsilon_closures = self.compute_epsilon_closures()
        self.name = name

    def __str__(self):
        result = str(self.state_count) + '\n'

        result += " ".join(str(x) for x in sorted(self.final_states)) + '\n'

        for (curr_state, char), dest_states in sorted(self.delta.items()):
            result += " ".join(str(x) for x in [curr_state, char] + sorted(list(dest_states)))
            result += '\n'

        return result

    def compute_epsilon_closures(self):
        epsilon_closures = {k: set() for k in self.states}
        current_path = list()

        def dfs(curr_state: State):
            # we have reached this state, any previous state can reach it
            curr_epsilon_closure = epsilon_closures[curr_state]

            already_visited = len(curr_epsilon_closure) != 0

            # add self to epsilon closure
            curr_epsilon_closure.add(curr_state)

            for pathState in current_path:
                epsilon_closures[pathState].update(curr_epsilon_closure)

            # already visited, update without continuing the DFS
            if already_visited:
                return

            # move through epsilon-transitions
            next_states = self.delta.get((curr_state, epsilon))

            if next_states is None:
                return

            # continue the DFS
            for nextState in next_states:
                current_path.append(curr_state)
                dfs(nextState)
                current_path.pop()

        for state in self.states:
            dfs(state)

        return epsilon_closures

    def to_dfa(self, name: str = 'My converted DFA'):
        multi_state_to_simple_state = dict()  # O(1) indexing
        simple_state_index = 0
        generated_delta = dict()

        queue = []  # multi-states to be processed

        initial_multi_state = frozenset(self.epsilon_closures[self.initialState])

        multi_state_to_simple_state[initial_multi_state] = simple_state_index
        simple_state_index += 1

        queue.append(initial_multi_state)

        index = 0

        # process multi-states
        while queue:
            curr_multi_state = queue.pop(0)

            # for every possible non-epsilon transition
            for char in self.alphabet - {epsilon}:
                new_multi_state = set()

                # build the destination multi-state
                for currState in curr_multi_state:
                    next_states = self.delta.get((currState, char))

                    if next_states is None:
                        continue

                    # epsilon-close all results
                    for nextState in next_states:
                        new_multi_state.update(self.epsilon_closures[nextState])

                frozen_multi_state = frozenset(new_multi_state)

                generated_delta[(curr_multi_state, char)] = frozen_multi_state

                # process this multi-state in the future
                if frozen_multi_state not in multi_state_to_simple_state:
                    queue.append(frozen_multi_state)
                    multi_state_to_simple_state[frozen_multi_state] = simple_state_index
                    simple_state_index += 1

        # also update the transitions and final states
        dfa_delta = dict()
        dfa_final_states = set()

        for (curr_multi_state, char), destMultiState in generated_delta.items():
            source_state = multi_state_to_simple_state[curr_multi_state]
            destination_state = multi_state_to_simple_state[destMultiState]

            dfa_delta[(source_state, char)] = destination_state

            if not curr_multi_state.isdisjoint(self.final_states):
                dfa_final_states.add(source_state)

            if not destMultiState.isdisjoint(self.final_states):
                dfa_final_states.add(destination_state)

        # construct the DFA
        return DFA(
            state_count=len(multi_state_to_simple_state),
            alphabet=frozenset(self.alphabet - {epsilon}),
            final_states=frozenset(dfa_final_states),
            delta=dfa_delta,
            name=name
        )

    def render_graphviz(self):
        if not graphviz:
            print('Could not render NFA: package \'graphviz\' could not be imported', file=stderr)

        graph_attr = {
            'rankdir': 'LR'
        }

        node_attr = {
            'fontsize': '11',
            'fontcolor': 'black'
        }

        edge_attr = {
            'shape': 'tee'
        }

        dot = graphviz.Digraph(
            comment='DFA',
            strict=False,
            graph_attr=graph_attr,
            node_attr=node_attr,
            edge_attr=edge_attr
        )

        for state in self.states:
            dot.node(str(state), shape='doublecircle' if state in self.final_states else 'circle')

        for (state, char), dest_states in self.delta.items():
            for dest_state in dest_states:
                dot.edge(str(state), str(dest_state), label=str('\u03B5' if char is epsilon else char))

        dot.render('graphviz/' + self.name + '.gv', view=True, format='pdf')
