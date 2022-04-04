from google.colab import files
uploaded = files.upload()
def checker(token):
    if(token in operators.keys()):
        print(token + " is " + operators[token])
        return
    elif(token in dataType.keys()):
        print(token + " is " + dataType[token])
        return
    elif(token in keyWords):
        print(token + " is keyword")
        return
    elif(token in numbers):
        print(token + " is constant")
        return
    elif(token in nonIdentifiers):
        print(token + " is preprocessor")
        return
    else:
        print(token + " is identifier" )



operators = { '=': 'Assignment Operator','+': 'Additon Operator', '-' : 'Substraction Operator', '/' : 'Division Operator', 
            '*': 'Multiplication Operator', '++' : 'increment Operator', '--' : 'Decrement Operator', '%' : 'Modulo Operator', 
            '<':'Special operator','>':'Special operator','|':'Logical operator','&':'Logical operator','!':'Logical operator','.':'Special operator',',':'Special operator', }
dataType = {'int': 'Integer','float' : 'Floating Point', 'char': 'Character','long': 'long int'}
numbers = str(list(range(-100,100)))
keyWords = ['if','else','for', 'while','do','return','break','continue','print','main','include','stdio','h']
nonIdentifiers = ['_','`','~','@','#','$','(',')','"',':',';','{','}','[',']','?']

f = open("input.txt")
print("Tokens are : \n")
x=f.read()
xin=x.split('\n')
for x in xin:
    tokens = x.split(' ')
    for i in tokens:
        checker(i)