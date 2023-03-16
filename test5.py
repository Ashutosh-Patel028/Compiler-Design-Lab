#shift reduce parser
import re
gram = {"E": ["E+T", "T"], "T": ["T*F", "F"], "F": ["(E)", "i"]}
start = 'E'
term = []
nonterm = []
for i, j in gram.items():
    print(i, end=' -> ')
    print(*j, sep=' | ')
    for k in j:
        for m in k:
            if((re.match("[A-Z]", m))):
                term.append(m)
            else:
                nonterm.append(m)


def stkchecker(stk):
    k = 1
    for _ in range(len(stk)):
        for i, j in gram.items():
            if(''.join(stk[k:]) in j):
                return i, stk[k:]
            k += 1
            return 0

w = 'i+i$' #input string to be checked
print('\nstack\t\t\tinput\t\t\taction')
stk = ['$']
i = 1
print(stk, '\t\t\t', w, '\t\t\tshift')
stk.append(w[0])
while 1:
    if(w[i:] == '$' and ''.join(stk) == ('$'+start)):
        print(stk, '\t\t\t', w[i:], '\t\t\taccepted ')
        break
    if(stkchecker(stk)):
        temp1, temp2 = stkchecker(stk)
        print(stk, '\t\t\t', w[i:],
                '\t\t\treduce ', temp1, ' -> ', temp2)
        for _ in range(len(temp2)):
            stk.pop()
            stk.append(temp1)
    else:
        print(stk, '\t\t\t', w[i:], '\t\t\tshift')
        stk.append(w[i])
        i += 1
