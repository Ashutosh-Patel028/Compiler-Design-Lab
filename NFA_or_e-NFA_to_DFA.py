#Converts epsilon-NFA to DFA and NFA to DFA both
from graphviz import Digraph
import json

class NFA:
    def __init__(self, no_state, states, no_alphabet, alphabets, start,
                 no_final, finals, no_transition, transitions):
        self.no_state = no_state
        self.states = states
        self.no_alphabet = no_alphabet
        self.alphabets = alphabets
        self.alphabets.append('e')
        self.no_alphabet += 1
        self.start = start
        self.no_final = no_final
        self.finals = finals
        self.no_transition = no_transition
        self.transitions = transitions
        self.graph = Digraph(format='png')

        # Dictionaries to get index of states or alphabets
        self.states_dict = dict()
        for i in range(self.no_state):
            self.states_dict[self.states[i]] = i
        self.alphabets_dict = dict()
        for i in range(self.no_alphabet):
            self.alphabets_dict[self.alphabets[i]] = i

        # transition table is of the form
        # [From State + Alphabet pair] -> [Set of To States]
        self.transition_table = dict()
        for i in range(self.no_state):
            for j in range(self.no_alphabet):
                self.transition_table[str(i)+str(j)] = []
        for i in range(self.no_transition):
            self.transition_table[str(self.states_dict[self.transitions[i][0]])
                                  + str(self.alphabets_dict[
                                      self.transitions[i][1]])].append(
                self.states_dict[self.transitions[i][2]])

    # Method to get input from User
    @classmethod
    def fromUser(cls):
        no_state = int(input("Number of States : "))
        states = list(input("States : ").split())
        no_alphabet = int(input("Number of Alphabets : "))
        alphabets = list(input("Alphabets : ").split())
        start = input("Start State : ")
        no_final = int(input("Number of Final States : "))
        finals = list(input("Final States : ").split())
        no_transition = int(input("Number of Transitions : "))
        transitions = list()
        print("Enter Transitions (from alphabet to) (e for epsilon): ")
        for i in range(no_transition):
            transitions.append(input("-> ").split())
        return cls(no_state, states, no_alphabet, alphabets, start,
                   no_final, finals, no_transition, transitions)

    # Method to represent quintuple
    def __repr__(self):
        return "Q : " + str(self.states)+"\nΣ : "
        + str(self.alphabets)+"\nq0 : "
        + str(self.start)+"\nF : "+str(self.finals) + \
            "\nδ : \n" + str(self.transition_table)

    def getEpsilonClosure(self, state):

        closure = dict()
        closure[self.states_dict[state]] = 0
        closure_stack = [self.states_dict[state]]

        while (len(closure_stack) > 0):
            cur = closure_stack.pop(0)
            for x in self.transition_table[
                    str(cur)+str(self.alphabets_dict['e'])]:
                if x not in closure.keys():
                    closure[x] = 0
                    closure_stack.append(x)
            closure[cur] = 1
        return closure.keys()

    def getStateName(self, state_list):
        name = ''
        for x in state_list:
            name += self.states[x]
        return name

    def isFinalDFA(self, state_list):
        for x in state_list:
            for y in self.finals:
                if (x == self.states_dict[y]):
                    return True
        return False

print("E-NFA to DFA:")
#<-----------------------------INPUTS------------------------------>
# INPUTS
# Number of States : no_state
# Array of States : states
# Number of Alphabets : no_alphabet
# Array of Alphabets : alphabets
# Start State : start
# Number of Final States : no_final
# Array of Final States : finals
# Number of Transitions : no_transition
# Array of Transitions : transitions

#reading json file and passing object values in NFA object
# f=open("input1.json","r")
# nfa_dict=json.load(f)
# nfa=NFA(
#     nfa_dict['noOfStates'],
#     nfa_dict['arrayStates'],
#     nfa_dict['noOfAlphabets'],
#     nfa_dict['arrayAlphabets'],
#     nfa_dict['startState'],
#     nfa_dict['noOfFinalStates'],
#     nfa_dict['arrayFinalStates'],
#     nfa_dict['noOfTransitions'],
#     nfa_dict['arrayOfTransitions']
# )

# nfa = NFA(
#     4,  # number of states
#     ['A', 'B', 'C', 'D'],  # array of states
#     3,  # number of alphabets
#     ['a', 'b', 'c'],  # array of alphabets
#     'A',  # start state
#     1,  # number of final states
#     ['D'],  # array of final states
#     7,  # number of transitions
#         [['A', 'a', 'A'], ['A', 'e', 'B'], ['B', 'b', 'B'],
#          ['A', 'e', 'C'], ['C', 'c', 'C'], ['B', 'b', 'D'],
#          ['C', 'c', 'D']]
#     # array of transitions with its element of type :
#         # [from state, alphabet, to state]
# )
nfa=NFA(     #NFA input
    3,
    ['q0','q1','q2'],
    2,
    ['a','b'],
    'q0',
    1,
    ['q2'],
    4,
    [['q0','a','q0'],['q0','b','q0'],['q0','b','q1'],['q1','b','q2']]
)

# nfa=NFA(    #epsion NFA input
#     3,
#     ['q0','q1','q2'],
#     2,
#     ['0','1'],
#     'q0',
#     1,
#     ['q2'],
#     6,
#     [['q0','0','q0'],['q0','e','q1'],['q1','1','q1'],['q1','e','q2'],['q2','0','q2'],['q2','1','q2']]
# )

# nfa = NFA.fromUser() # To get input from user
# print(repr(nfa)) # To print the quintuple in console
# <------------------------------------INPUT OVER-------------------------------------->

# Making NFA Graph
nfa.graph = Digraph(format='png')
nfa.graph.attr(rankdir='LR') 
for x in nfa.states:
    if (x not in nfa.finals):
        nfa.graph.attr('node', shape='circle')
        nfa.graph.node(x)
    else:
        nfa.graph.attr('node', shape='doublecircle',color='blue')
        nfa.graph.node(x)
nfa.graph.attr('node', shape='none')
nfa.graph.node('')
nfa.graph.edge('', nfa.start,arrowsize='2',color='red')
for x in nfa.transitions:
    nfa.graph.edge(x[0], x[2], label=('ε', x[1])[x[1] != 'e'])
nfa.graph.attr(label=r'\n\nNFA')
nfa.graph.attr(fontsize='20')
nfa.graph.render('nfa_Input', view=True,directory=r"C:\Users\ashut\Desktop\Compiler Design Lab\Images")



# Making DFA Graph
dfa = Digraph(format='png')
dfa.attr(rankdir='LR')

epsilon_closure = dict()
for x in nfa.states:
    epsilon_closure[x] = list(nfa.getEpsilonClosure(x))

dfa_stack = list()
dfa_stack.append(epsilon_closure[nfa.start])

if (nfa.isFinalDFA(dfa_stack[0])):
    dfa.attr('node', shape='doublecircle',color='blue')
else:
    dfa.attr('node', shape='circle')
dfa.node(nfa.getStateName(dfa_stack[0]))

dfa.attr('node', shape='none')
dfa.node('')
dfa.edge('', nfa.getStateName(dfa_stack[0]),arrowsize='2',color='red')

dfa_states = list()
dfa_states.append(epsilon_closure[nfa.start])

while (len(dfa_stack) > 0):
    cur_state = dfa_stack.pop(0)

    for al in range((nfa.no_alphabet) - 1):
        from_closure = set()
        for x in cur_state:
            from_closure.update(
                set(nfa.transition_table[str(x)+str(al)]))

        if (len(from_closure) > 0):
            to_state = set()
            for x in list(from_closure):
                to_state.update(set(epsilon_closure[nfa.states[x]]))

            if list(to_state) not in dfa_states:
                dfa_stack.append(list(to_state))
                dfa_states.append(list(to_state))

                if (nfa.isFinalDFA(list(to_state))):
                    dfa.attr('node', shape='doublecircle',color='blue')
                else:
                    dfa.attr('node', shape='circle')
                dfa.node(nfa.getStateName(list(to_state)))

            dfa.edge(nfa.getStateName(cur_state),
                     nfa.getStateName(list(to_state)),
                     label=nfa.alphabets[al])

        else:

            # Check if any dead state was present before this
            # if not then make a new dead state ϕ
            if (-1) not in dfa_states:
                dfa.attr('node', shape='circle')
                dfa.node('ϕ')
                for alpha in range(nfa.no_alphabet - 1):
                    dfa.edge('ϕ', 'ϕ', nfa.alphabets[alpha])

                dfa_states.append(-1)

            dfa.edge(nfa.getStateName(cur_state,),'ϕ', label=nfa.alphabets[al])
dfa.attr(label=r'\n\nDFA')
dfa.attr(fontsize='20')
#Render DFA Graph
dfa.render('dfa_Output',view=True,directory=r"C:\Users\ashut\Desktop\Compiler Design Lab\Images")
    




