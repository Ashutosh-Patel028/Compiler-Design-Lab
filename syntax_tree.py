# represent syntax tree for given expression

OPERATORS = set(['+', '-', '*', '/', '(', ')', '^']) 
PRIORITY = {1:'-', 2:'+',3:'*', 4:'/'} 
k=0
tac={} 
p=4
st={} 

def preaft(exp,op): 
  ind=exp.index(op) 
  pre=aft=0
  for i in range(ind): 
    if(exp[i] in OPERATORS): 
     pre=i 
  for i in range(ind+1,len(exp)): 
    if(exp[i] in OPERATORS): 
      aft=i 
      break
  return pre,aft

def findop(exp): 
  for o in range(len(exp)): 
    if(exp[o] in OPERATORS): 
     return exp[o],exp[:o],exp[o+1:] 


def threeAddressCode(expression,p,k): 
  while p>=1: 
    if(PRIORITY[p] in expression): 
      pre,aft=preaft(expression,PRIORITY[p]) 
      if(pre==0 and aft!=0): 
        tac['t'+str(k)]=expression[:aft] 
        expression='t'+str(k)+expression[aft:] 
        op,l,r= findop(tac['t'+str(k)]) 
        st['t'+str(k)]={op:{'l':l,'r':r}} 
        k+=1
      elif(aft==0 and pre!=0): 
        tac['t'+str(k)]=expression[pre+1:] 
        expression=expression[:pre+1]+('t'+str(k)) 
        op,l,r=findop(tac['t'+str(k)]) 
        st['t'+str(k)]={op:{'l':l,'r':r}} 
        k+=1
      elif(pre==0 and aft==0): 
        tac['t'+str(k)]=expression[:] 
        op,l,r=findop(tac['t'+str(k)]) 
        st['t'+str(k)]={op:{'l':l,'r':r}} 
        expression=('t'+str(k)) 
        break
      else: 
        tac['t'+str(k)]=expression[pre+1:aft] 
        expression=expression[:pre+1]+('t'+str(k))+expression[aft:] 
        op,l,r=findop(tac['t'+str(k)]) 
        st['t'+str(k)]={op:{'l':l,'r':r}} 
        k+=1
  else:
    p-=1
  return k 

def threeAddressCodeB(expression,k): 
  if('('in expression ): 
    i=expression.index('(') 
    tac['t'+str(k)]=expression[i+1:expression.index(')')] 
    op,l,r=findop(tac['t'+str(k)]) 
    st['t'+str(k)]={op:{'l':l,'r':r}} 
    k+=1
    expression,k=threeAddressCodeB(expression[:expression.index('(')]+'t'+str(k-1)+expression[expression.index(')')+1:],k) 
    return expression,k 
  else: 
    return expression,k

expression = input('Enter expression: ') 
spl=expression.split('=') 
expression,k=threeAddressCodeB(spl[1],k)
k=threeAddressCode(expression,p,k) 
st['t'+str(k+1)]={'=':{'l':spl[0],'r':'t'+str(k)}} 
for i,j in st.items(): 
  print(i,j)