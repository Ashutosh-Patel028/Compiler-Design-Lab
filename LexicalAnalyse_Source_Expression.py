#Lexical Analyser
import re                                
tokens = []                               
user=input("Enter the expression").split()

for word in user:
    if re.match("[a-z]", word) or re.match("[A-Z]", word):
        tokens.append(['IDENTIFIER', word])
    elif word in '*-/+%':
        tokens.append(['ARITHMETIC OPERATOR', word])
    elif word in '=':
        tokens.append(['ASSIGNMENT OPERATOR', word])
    elif word in '(){}[]':
        tokens.append(['BRACKETS', word])
    elif word in ',;:.':
        tokens.append(['PUNCTUATION', word])
    elif re.match("[0-9]", word):
            tokens.append(["INTEGER/CONSTANT", word])
for i in tokens:
    print(i)