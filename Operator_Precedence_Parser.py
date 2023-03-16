import numpy as np
from prettytable import PrettyTable


def printTable(terminals): 
    terminals.append('$')   #terminals is a list of Terminals
    print("Terminals = ",terminals)
    l=list("abcdefghijklmnopqrstuvwxyz")
    o=list('(/*%+-)')
    p=list('(/*%+-)') 
    precedence=np.empty([len(terminals)+1,len(terminals)+1],dtype=object,order="C")  #here precedence Precedence-2d-array
    precedence[0][0]="TERMINALS"
    for j in range(1,len(terminals)+1):
        precedence[0][j]=terminals[j-1]
        precedence[j][0]=terminals[j-1] 
    for i in range(1,len(terminals)+1):
            for j in range(1,len(terminals)+1):
                if(precedence[i][0]==precedence[0][j]):
                    precedence[i][j]=""
                elif((precedence[i][0] in l)and(precedence[0][j] in l)):
                    precedence[i][j]=""
                elif((precedence[i][0] in l)):
                    precedence[i][j]=">"
                elif((precedence[i][0] in o) and (precedence[0][j] in o)):
                    if(o.index(precedence[i][0])<=o.index(precedence[0][j])):
                        precedence[i][j]=">"
                    else:
                        precedence[i][j]="<"
                elif((precedence[i][0] in o)and precedence[0][j]in l):
                    precedence[i][j]="<"
                elif(precedence[i][0]=="$" and precedence[0][j]!="$"):
                    precedence[i][j]="<"
                elif(precedence[0][j]=="$" and precedence[i][0]!="$" ):
                    precedence[i][j]=">"
                else:
                    break
    myTable = PrettyTable(col  for col in precedence[0])
    for row in range(1,len(precedence)):
        myTable.add_row(precedence[row])
    print(myTable)
    return precedence

def checkString(precedence):
    i=list(input("Enter the string want to be checked(non-terminals should be in cursive(small) letter...\n"))
    i.append("$")
    s=[None]*len(i)
    q=0
    s.insert(q,"$")
    x=[row[0] for row in precedence]
    x[0]=''
    y=list(precedence[0])
    y[0]=''
    h=0
    p=list('(/*%+-)')
    while(s[0]!=s[1]):
        if((i[len(i)-2] in p)):
            break
        elif((s[q] in x)and(i[h]in y )):
            if(precedence[x.index(s[q])][y.index(i[h])]=="<"):
                q+=1
                s.insert(q,i[h])
                h+=1
            elif(precedence[x.index(s[q])][y.index(i[h])]==">"):
                s.pop(q)
                q-=1
            elif((precedence[x.index(s[q])][y.index(i[h])]=='')and ((s[q]=="$") and (i[h]=="$"))):
                s[1]=s[0]
        else:
            break
    if(s[0]!=s[1]):
        return False
    else:
        return True    

def grammarcheck(i):
    print("Enter Prodiction->",str(i+1)," (For null production please enter any special symbol or whitespace...)\n")
    b=list(input().split("->"))
    f=list("abcdefghijklmnopqrstuvwxyz")
    if(b[0]==" " or b[0]=="" or b[0] in f or len(b)==1):
        return False
    else:
        b.pop(0)
        b=list(b[0])
        s=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        o=list("(abcdefghijklmnopqrstuvwxyz^/*+-|)")
        sp=['!','@','#','$','?','~','`',',',';',':','"','=','_','&',"'",""," "]
        for i in range(0,len(b),2):
            if(b[i]==" "):
                g=False
            elif(b[i] in sp):
                g=False
                break
            elif(b[len(b)-1] in o and ((b[0]=="(" and b[len(b)-1]==")" )or (b.count("(")==b.count(")")))):
                g=True
            elif(b[i] in f):
                g=True
            elif(b[len(b)-1] in o):
                g=False
            elif((i==len(b)-1) and (b[i] in s)):
                g=True
            elif((i==len(b)-1) and (b[i] not in s) and (b[i] in o)and b[i-1] in o):
                g=True
            elif((b[i] in s) and(b[i+1]in o)):
                g=True
            elif((b[i] in s) and (b[i+1] in s)):
                g=False
                break
            else:
                g=False
                break
        if(g==True):
            return True
        else:
            return False


c=int(input("Enter the number of Productions..\n"))
for i in range(c):
    if(grammarcheck(i)):
        t=True
    else:
        t=False
        break
if(t):
    print("\n**Grammar is accepted**\n")
    terminals=list(input("Enter all the terminals present in grammer (in small case)\n"))
    precedence=printTable(terminals)
    if(checkString(precedence)):
        print("\n**String is accepted**\n")
    else:
        print("\n**String is not accepted**\n")
else:
    print("\n**Grammar is not accepted**\n")




'''
I/O example for grammer E->E+E|E*E|id and id+id*id

Enter the number of Productions..
3
Enter Prodiction-> 1  (For null production please enter any special symbol or whitespace...)

E->E+E
Enter Prodiction-> 2  (For null production please enter any special symbol or whitespace...)

E->E*E
Enter Prodiction-> 3  (For null production please enter any special symbol or whitespace...)

E->i

**Grammar is accepted**

Enter all the terminals present in grammer (in small case)
+*i
Terminals =  ['+', '*', 'i', '$']
+-----------+---+---+---+---+
| TERMINALS | + | * | i | $ |
+-----------+---+---+---+---+
|     +     |   | < | < | > |
|     *     | > |   | < | > |
|     i     | > | > |   | > |
|     $     | < | < | < |   |
+-----------+---+---+---+---+
Enter the string want to be checked(non-terminals should be in cursive(small) letter...
i+i*i

**String is accepted**
'''