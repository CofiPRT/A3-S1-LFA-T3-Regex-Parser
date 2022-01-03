from sys import argv
from antlr4 import FileStream, CommonTokenStream
from antlr_files.RegexLexer import RegexLexer
from antlr_files.RegexParser import RegexParser
from NFABuilder import NFABuilder

use_graphviz = True
construct_min_dfa = True


# verify the command line arguments
def validate_input():
    argc = len(argv)
    expected_argc = 4

    message = "Invalid argument count: " + str(argc) + ". "
    message += "Must be: " + str(expected_argc)

    assert argc == expected_argc, message


if __name__ == '__main__':
    validate_input()

    # acquire IO files
    output_file_nfa = open(argv[2], "w")
    output_file_dfa = open(argv[3], "w")

    # initialize parsing components
    input_stream = FileStream(argv[1])
    lexer = RegexLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = RegexParser(stream)

    tree = parser.expr()

    # construct an NFA from the given Regex
    NFA = NFABuilder().build(tree)
    if use_graphviz:
        NFA.render_graphviz()

    output_file_nfa.write(str(NFA))

    # construct a DFA from the generated NFA
    DFA = NFA.to_dfa()
    if use_graphviz:
        DFA.render_graphviz()

    if construct_min_dfa:
        # construct a min-DFA from the generated DFA
        DFA = DFA.to_min_dfa_myphill_nerode()
        if use_graphviz:
            DFA.render_graphviz()

    output_file_dfa.write(str(DFA))

    output_file_nfa.close()
    output_file_dfa.close()
