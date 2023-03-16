#SLR parser ->50%

G = {} #productions in list form, augmented grammar
C = {}
I = {}
J = {}
inputstring = ""
start = ""
terminals = []
nonterminals = []
symbols = []
error = 0
relation = []
r1 = []
n = int(input("Enter no of productions: ")) 
def parse_grammar():
    global G, start, terminals, nonterminals, symbols
    for i in range(n):
        x = input() #read productions from input
        line = " ".join(x.split())
        if(line=='\n'):
            break
        head = line[:line.index("->")].strip()
        prods = [l.strip().split(' ') for l in''.join(line[line.index("->")+2:]).split('|')] #symbols to right of arrow
        if not start:
                start = head+"'"#augmenting the grammar i.e. S'->S
                G[start] = [[head]]
        nonterminals.append(start)
        if head not in G: 
            G[head] = []
        if head not in nonterminals: 
            nonterminals.append(head)
        for prod in prods:
            G[head].append(prod) 
            for char in prod:
                if not char.isupper() and char not in terminals:
                    terminals.append(char)
                elif char.isupper() and char not in nonterminals:
                    nonterminals.append(char)
                    G[char] = [] 
        symbols = terminals+nonterminals

first_look = []

def First(X):
    global first_look
    first = []
    first_look.append(X)
    if X in terminals:
        first.append(X)
    elif X in nonterminals:
        for prods in G[X]:
            if prods[0] in terminals and prods[0] not in first:
                first.append(prods[0])
    else:
        for nonterm in prods:
            if nonterm not in first_look:
                for terms in First(nonterm):
                    if terms not in first:
                        first.append(terms)
                        first_look.remove(X)
            return first


follow_look = []
def Follow(A):
    global follow_look
    follow = []
    follow_look.append(A)
    if A == start:
        follow.append('$')
        for heads in G.keys():
            for prods in G[heads]:
                follow_head = False
                if A in prods:
                    next_symbol_pos = prods.index(A) + 1
                if next_symbol_pos<len(prods):
                    for terms in First(prods[next_symbol_pos]):
                        if terms not in follow:
                            follow.append(terms)
                        else:
                            follow_head = True
                if follow_head and heads not in follow_look:
                    for terms in Follow(heads):
                        if terms not in follow:
                            follow.append(terms)
                        follow_look.remove(A)
                return follow

def closure(I):
    J = I 
    while True:
        item_len = len(J)+sum(len(v) for k, v in J.items())
        for heads in list(J): #for each key in J
            for prods in J[heads]: #for all prods of key in J
                dot_pos = prods.index('.')
                if dot_pos+1<len(prods):
                    prod_after_dot = prods[dot_pos+1]
                if prod_after_dot in nonterminals:
                    for prod in G[prod_after_dot]: 
                        item = ["."]+prod 
                if prod_after_dot not in J.keys():
                    J.update({prod_after_dot:[item]})
                elif item not in J[prod_after_dot]:
                    J[prod_after_dot].append(item) 
                if item_len==len(J)+sum(len(v) for c, v in J.items()):
                    return J

def Goto(I, X):
    goto = {}
    for heads, t in I.items():
        for prods in I[heads]:
            for i in range(len(prods)-1):
                if"."==prods[i] and X == prods[i+1]:
                    temp_prods = prods[:]
                temp_prods[i], temp_prods[i+1] = temp_prods[i+1], temp_prods[i]
                prod_closure = closure({heads: [temp_prods]})
        for keys, v in prod_closure.items():
            if keys not in goto.keys():
                goto[keys] = prod_closure[keys]
            elif prod_closure[keys] not in goto[keys]:
                goto[keys].append(prod_closure[keys])
                return goto

def items():
    global C
    i = 1
    C = {'I0': closure({start: [['.']+G[start][0]]})}
    while True:
        item_len = len(C) + sum(len(v) for k, v in C.items())
        for I in list(C):
            for X in symbols:
                if Goto(C[I], X) and Goto(C[I], X) not in C.values():
                    C['I'+str(i)] = Goto(C[I], X)
                    i += 1
                if item_len==len(C) + sum(len(v) for k, v in C.items()):
                    return

def Action(i):











