from antlr_files.RegexVisitor import RegexVisitor
from antlr_files.RegexParser import RegexParser
from NFA import NFA, epsilon, State


# link rules based on Thompson's algorithm
class NFABuilder(RegexVisitor):
    def __init__(self):
        self.delta = dict()
        self.alphabet = {epsilon}
        self.initial_state = 0
        self.final_states = set()
        self.curr_state_index = self.initial_state + 1

    def add_transition(self, source: State, symbol: chr, destination: State):
        destination_set = self.delta.get((source, symbol))

        if not destination_set:
            destination_set = set()
            self.delta[(source, symbol)] = destination_set

        destination_set.add(destination)

    def create_enclosing_states(self):
        start_state = self.curr_state_index
        end_state = start_state + 1

        # increment for future uses
        self.curr_state_index = end_state + 1

        return start_state, end_state

    def visitSymbol(self, ctx: RegexParser.SymbolContext):
        symbol = str(ctx.SYMBOL())

        # save this symbol in the NFA's alphabet
        self.alphabet.add(symbol)

        # create two new states
        start_state, end_state = self.create_enclosing_states()

        # generate the transition
        self.add_transition(start_state, symbol, end_state)

        return start_state, end_state

    def visitParentheses(self, ctx: RegexParser.ParenthesesContext):
        # disregard visiting the parentheses
        return self.visit(ctx.expr())

    def visitKleene(self, ctx: RegexParser.KleeneContext):
        inner_nfa = ctx.precedence4()

        # force post-order
        start_state, end_state = self.visit(inner_nfa)

        # create two new states
        new_start_state, new_end_state = self.create_enclosing_states()

        # enclose in the new states
        self.add_transition(new_start_state, epsilon, start_state)
        self.add_transition(end_state, epsilon, new_end_state)

        # add epsilon transition for repeating
        self.add_transition(end_state, epsilon, start_state)

        # add epsilon transition for skipping
        self.add_transition(new_start_state, epsilon, new_end_state)

        return new_start_state, new_end_state

    def visitConcat(self, ctx: RegexParser.ConcatContext):
        left_nfa = ctx.precedence3()
        right_nfa = ctx.precedence2()

        # force post-order
        left_start_state, left_end_state = self.visit(left_nfa)
        right_start_state, right_end_state = self.visit(right_nfa)

        # link
        self.add_transition(left_end_state, epsilon, right_start_state)

        return left_start_state, right_end_state

    def visitUnion(self, ctx: RegexParser.UnionContext):
        left_nfa = ctx.precedence2()
        right_nfa = ctx.precedence1()

        # force post-order
        left_start_state, left_end_state = self.visit(left_nfa)
        right_start_state, right_end_state = self.visit(right_nfa)

        # create two new states
        new_start_state, new_end_state = self.create_enclosing_states()

        # link start state
        self.add_transition(new_start_state, epsilon, left_start_state)
        self.add_transition(new_start_state, epsilon, right_start_state)

        # link end state
        self.add_transition(left_end_state, epsilon, new_end_state)
        self.add_transition(right_end_state, epsilon, new_end_state)

        return new_start_state, new_end_state

    def build(self, tree):
        # force post-order
        start_state, end_state = self.visit(tree)

        # enclose the generated NFA in an initial state and a final state
        self.initial_state = 0
        self.final_states.add(self.curr_state_index)

        # link the enclosed NFA
        self.add_transition(self.initial_state, epsilon, start_state)
        self.add_transition(end_state, epsilon, self.curr_state_index)

        # construct the NFA
        return NFA(
            state_count=self.curr_state_index + 1,
            alphabet=frozenset(self.alphabet),
            final_states=frozenset(self.final_states),
            delta=self.delta
        )
