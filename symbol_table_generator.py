# Stimulation of Symbol Table
operators = {'=': 'Assignment Operator','+': 'Addition Operator', '-' : 'Substraction Operator', '/' :'Division Operator',
'*': 'Multiplication Operator', '++' :'increment Operator', '--' : 'Decrement Operator', '%' : 'Modulo Operator',
'<':'Relational operator','>':'Relational operator','|':'Logical operator','&':'Logical operator','!':'Logical operator'}
dataType = {'int': 'Integer','float' :'Floating Point', 'char': 'Character','long': 'long int'}
numbers = str(list(range(-100,100)))
keyWords = ['if','else','for', 'while','do','return','break','continue','print']
nonIdentifiers = ['_','`','~','@','#','$','(',')','"',':',';','{','}','[',']','?']

def symbolTable(token):
    if((token not in operators.keys()) and (token not in dataType.keys()) and (token not in keyWords) and (token not in numbers) and (token not in nonIdentifiers)):
            print(token + "\t\t" + str(id(token)))


exp = input("Enter the expression : ")
print("NOTE : Enter each token with space")
tokens = exp.split(' ')
print("\nSymbol \t\t Address")
tokens = set(tokens)
for i in tokens:
    symbolTable(i)

#EXAMPLE-1
#Input: c = a + b * 60
#Output:
'''
Symbol           Address
a               1663189761456
c               1663189334256
b               1663189420976
'''