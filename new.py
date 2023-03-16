n=int(input())
c={}
op=['+','-','*','/']
print('Quadriples:')
print('loaction\top\targ1\targ2\tresult')
for l,i in code.items():
    for j,k in i.items():
        for m in range(len(k)):
            if(k[m] in op):
                print('(',l,')\t\t',k[m],'\t',k[:m],'\t',k[m+1:],'\t',j)
                print('\n')
def arugl(m):
    for i,j in code.items():
        for k in j.keys():
            if(k==m):
                return'('+str(i)+')'
        return m
print('Triples:')
print('location\top\targ1\targ2')
for l,i in code.items():
    for j,k in i.items():
        for m in range(len(k)):
            if(k[m] in op):
                print('(',l,')\t\t',k[m],'\t',arugl(k[:m]),'\t',arugl(k[m+1:]))
                print('\n')

def arugr(m):
    for i,j in code.items():
        for k in j.keys():
            if(k==m):
                return m

print('indirect triples:')
print('location\top\targ1\targ2')

for l,i in code.items():
    for j,k in i.items():
        for m in range(len(k)):
            if(k[m] in op):
                print('(',l,')\t\t',k[m],'\t',(arugr(k[:m])),'\t',arugr(k[m+1:]))