from sys import stderr
from typing import FrozenSet, Dict, Tuple
from itertools import product
try:
    import graphviz
except ImportError:
    graphviz = None

State = int
Symbol = chr


class DFA:
    def __init__(self, state_count: int,
                 alphabet: FrozenSet[Symbol],
                 final_states: FrozenSet[State],
                 delta: Dict[Tuple[State, Symbol], State],
                 name: str = 'My DFA'):
        self.state_count = state_count
        self.states = frozenset(range(state_count))
        self.alphabet = alphabet
        self.initial_state = 0

        extra_states = final_states.difference(self.states)
        if extra_states:
            message = "Could not init DFA: "
            message += "The final states is not a subset of the states set. "
            message += "(Extra states: " + str(sorted(extra_states)) + ")"
            raise Exception(message)

        self.final_states = final_states

        for curr_state in self.states:
            for curr_char in self.alphabet:
                dest_state = delta.get((curr_state, curr_char))

                if dest_state is None:
                    message = "Could not init DFA: "
                    message += "The delta function is not total. "
                    message += "(Missing transition from state " + str(curr_state)
                    message += " on character " + str(curr_char) + ")"
                    raise Exception(message)
                elif dest_state not in self.states:
                    message = "Could not init DFA: "
                    message += "The delta function is not valid. "
                    message += "(Transition from state " + str(curr_state)
                    message += " on character " + str(curr_char)
                    message += " leads to non-existent state " + str(dest_state) + ")"
                    raise Exception(message)

        self.delta = delta
        self.name = name

    def __str__(self):
        result = str(self.state_count) + '\n'

        result += " ".join(str(x) for x in sorted(self.final_states)) + '\n'

        for (curr_state, char), dest_state in sorted(self.delta.items()):
            result += " ".join(str(x) for x in [curr_state, char, dest_state])
            result += '\n'

        return result

    def to_min_dfa_myphill_nerode(self, name: str = 'My converted min-DFA'):
        # eliminate inaccessible states
        filtered_states = set()

        def visit_states_dfs(state_: State):
            if state_ in filtered_states:
                return

            filtered_states.add(state_)

            # visit reachable states
            for char_ in self.alphabet:
                visit_states_dfs(self.delta[(state_, char_)])

        visit_states_dfs(self.initial_state)

        # initialize the Myphill-Nerode table
        table: Dict[State, Dict[State, bool]] = {x: {} for x in filtered_states}

        for (state1, state2) in product(filtered_states, repeat=2):
            is_final1 = state1 in self.final_states
            is_final2 = state2 in self.final_states

            # mark if one state is final and the other is not
            mark = is_final1 != is_final2

            table[state1][state2] = mark
            table[state2][state1] = mark

        while True:
            changed = False

            for (state1, state2) in product(filtered_states, repeat=2):
                if table[state1][state2]:  # skip already marked pairs
                    continue

                for curr_char in self.alphabet:
                    dest1 = self.delta[(state1, curr_char)]
                    dest2 = self.delta[(state2, curr_char)]

                    # mark
                    if table[dest1][dest2]:
                        table[state1][state2] = True
                        table[state2][state1] = True
                        changed = True
                        break

            if not changed:
                break

        def find_connected_component(state_: State):
            if state_ not in domain:
                return

            domain.remove(state_)
            connected_component.add(state_)

            for pair_state, marked in table[state_].items():
                if not marked:  # an edge exists if these two states form an unmarked pair
                    find_connected_component(pair_state)

        # merge unmarked pairs
        connected_components = list()
        domain = set(filtered_states)
        for state in filtered_states:
            if state not in domain:
                continue

            connected_component = set()
            find_connected_component(state)

            connected_components.append(connected_component)

        # construct the min-DFA
        new_final_states = set()
        state_to_merged_state = dict()

        # merge each connected_component into a new state
        new_state = 1
        for connected_component in connected_components:
            if self.initial_state in connected_component:
                merged_state = self.initial_state
            else:
                merged_state = new_state
                new_state += 1

            for state in connected_component:
                state_to_merged_state[state] = merged_state

            if connected_component.issubset(self.final_states):
                new_final_states.add(merged_state)

        # construct the new delta
        new_delta = dict()
        for (state, char), dest_state in self.delta.items():
            if state not in filtered_states:
                continue

            new_state = state_to_merged_state[state]
            new_dest_state = state_to_merged_state[dest_state]
            new_delta[(new_state, char)] = new_dest_state

        return DFA(state_count=len(connected_components),
                   alphabet=self.alphabet,
                   final_states=frozenset(new_final_states),
                   delta=new_delta,
                   name=name)

    def to_min_dfa_equivalence(self, name: str = 'My converted min-DFA'):
        # eliminate inaccessible states
        filtered_states = set()

        def visit_states_dfs(state_: State):
            if state_ in filtered_states:
                return

            filtered_states.add(state_)

            # visit reachable states
            for curr_char in self.alphabet:
                visit_states_dfs(self.delta[(state_, curr_char)])

        visit_states_dfs(self.initial_state)

        # there are two initial partitions: the final states and the non-final states
        final_states_partition = set(self.final_states)
        non_final_states_partition = filtered_states.difference(final_states_partition)

        partition_index_to_states = {0: non_final_states_partition, 1: final_states_partition}

        # for complexity purposes
        state_to_partition_index = {state: (1 if state in self.final_states else 0) for state in filtered_states}

        def distinguishable(state1_: State, state2_: State):
            for curr_char in self.alphabet:
                destination1 = self.delta.get((state1_, curr_char))
                destination2 = self.delta.get((state2_, curr_char))

                # for this character, the transitions lead to states in different partitions
                if state_to_partition_index[destination1] != state_to_partition_index[destination2]:
                    return True

            return False

        def find_connected_component(state_: State):
            if state_ not in domain:
                return

            domain.remove(state_)
            connected_component.add(state_)
            new_state_to_partition_index[state_] = new_partition_index

            for next_state in set(domain):
                if not distinguishable(state_, next_state):  # an edge exists if these states are not distinguishable
                    find_connected_component(next_state)

        while True:
            new_partition_index_to_states = dict()
            new_state_to_partition_index = dict()

            for states in partition_index_to_states.values():
                domain = set(states)
                for state in states:
                    if state not in domain:
                        continue

                    new_partition_index = len(new_partition_index_to_states)

                    connected_component = set()
                    find_connected_component(state)

                    new_partition_index_to_states[new_partition_index] = connected_component

            # no changes have been made, stop
            if new_partition_index_to_states == partition_index_to_states:
                break

            partition_index_to_states = new_partition_index_to_states
            state_to_partition_index = new_state_to_partition_index

        # construct the min-DFA
        new_final_states = set()
        partition_index_to_merged_state = dict()

        # merge each partition into a new state
        new_state = 1
        for (partition_index, states) in partition_index_to_states.items():
            if self.initial_state in states:
                partition_index_to_merged_state[partition_index] = self.initial_state
            else:
                partition_index_to_merged_state[partition_index] = new_state
                new_state += 1

            if states.issubset(self.final_states):
                new_final_states.add(partition_index_to_merged_state[partition_index])

        # construct the new delta
        new_delta = dict()
        for (state, char), dest_state in self.delta.items():
            if state not in filtered_states:
                continue

            new_state = partition_index_to_merged_state[state_to_partition_index[state]]
            new_dest_state = partition_index_to_merged_state[state_to_partition_index[dest_state]]
            new_delta[(new_state, char)] = new_dest_state

        return DFA(
            state_count=len(partition_index_to_merged_state),
            alphabet=self.alphabet,
            final_states=frozenset(new_final_states),
            delta=new_delta,
            name=name
        )

    def render_graphviz(self):
        if not graphviz:
            print('Could not render DFA: package \'graphviz\' could not be imported', file=stderr)

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

        for (state, char), dest_state in self.delta.items():
            dot.edge(str(state), str(dest_state), label=str(char))

        dot.render('graphviz/' + self.name + '.gv', view=True, format='pdf')
