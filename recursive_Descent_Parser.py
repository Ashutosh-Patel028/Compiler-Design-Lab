#Program to implement Recursive Descent Parser

from graphviz import Digraph

#<----------------------------INPUT_GRAMMERS--------------------->

gram = {
    "E":["E+T","T"],
    "T":["T*F","F"],
    "F":["(E)","i"]
}

# gram = {
#     "S":["S+S","S-S","a","b"]
# }

# gram = {
#     "A":["Ac","Sd","e"]
# }

#<-----------------------------INPUT ENDS------------------------>

def removeDirectLR(gramA, A):  #checks for direct Left recursion and removes
	temp = gramA[A]
	tempCr = []
	tempInCr = []
	for i in temp:
		if i[0] == A:
			tempInCr.append(i[1:]+[A+"'"])
		else:
			tempCr.append(i+[A+"'"])
	tempInCr.append(["e"])
	gramA[A] = tempCr
	gramA[A+"'"] = tempInCr
	return gramA

def checkForIndirect(gramA, a, ai): #checks for indirect left recursion
	if ai not in gramA:
		return False
	if a == ai:
		return True
	for i in gramA[ai]:
		if i[0] == ai:
			return False
		if i[0] in gramA:
			return checkForIndirect(gramA, a, i[0])
	return False

def rep(gramA, A):
	temp = gramA[A]
	newTemp = []
	for i in temp:
		if checkForIndirect(gramA, A, i[0]):
			t = []
			for k in gramA[i[0]]:
				t=[]
				t+=k
				t+=i[1:]
				newTemp.append(t)

		else:
			newTemp.append(i)
	gramA[A] = newTemp
	return gramA

def rem(gram):
	c = 1
	conv = {}
	gramA = {}
	revconv = {}
	for j in gram:
		conv[j] = "A"+str(c)
		gramA["A"+str(c)] = []
		c+=1

	for i in gram:
		for j in gram[i]:
			temp = []
			for k in j:
				if k in conv:
					temp.append(conv[k])
				else:
					temp.append(k)
			gramA[conv[i]].append(temp)

	for i in range(c-1,0,-1):
		ai = "A"+str(i)
		for j in range(0,i):
			aj = gramA[ai][0][0]
			if ai!=aj :
				if aj in gramA and checkForIndirect(gramA,ai,aj):
					gramA = rep(gramA, ai)

	for i in range(1,c):
		ai = "A"+str(i)
		for j in gramA[ai]:
			if ai==j[0]:
				gramA = removeDirectLR(gramA, ai)
				break

	op = {}
	for i in gramA:
		a = str(i)
		for j in conv:
			a = a.replace(conv[j],j)
		revconv[i] = a

	for i in gramA:
		l = []
		for j in gramA[i]:
			k = []
			for m in j:
				if m in revconv:
					k.append(m.replace(m,revconv[m]))
				else:
					k.append(m)
			l.append(k)
		op[revconv[i]] = l

	return op

def PrintGrammer(result):   #Printing Resultant Grammer after elimination of Left Recursion
	print("<--------------Grammer after removal of left recursion and left factoring------------>")
	for head,prod in result.items():
		print(head,"->",end=" ")
		i=0
		length=len(prod)
		while i<length:
			val=prod[i]
			for j in val:
				print(j,end="")
			if i+1<length:
				print(" | " ,end="")
			i+=1
		print()

def printProcedure(gram,non_terminals):   #printing recursive procedure
	print("\n*******RECURSIVE PROCEDURE********\n")
	flag=False
	for k in gram:
		print("<--------------------------------->")
		print(f"procedure: {k}()")
		print("Begin:")
		for ch in gram[k]:
			if(ch not in non_terminals and ch !='e'):
				if(flag):
					print("End ")
                
				flag=True
                
				print(f"if an input symbol '{ch}' then,")
                
				print("Begin: ")
            
			elif(ch in non_terminals):
				print(f"{ch}()")
			elif(ch == gram[k][-1]):
				print("End")
				print('Else')
				if(ch=='e'):
					print("Null character")
				else:
					print(f"if an input symbol '{ch}' then")
					print("Begin\nEnd")
		print("End")
		print("<--------------------------------->")

def DrawTransitionDiagram(gram,non_terminals):
    g = Digraph(format="png")
    g.attr(rankdir='LR') 
    ind=0 #counter for unique node name in each subgraph like...q0,q1,q2,q3,........
    cnt=0 #counter for subgraphs to maintain unique names for each subgraph
    flag=False #flag for if last item is terminal
    for key in gram:
        str=gram[key]
        cluster_name=f'cluster_{cnt}'
        with g.subgraph(name=cluster_name) as c:    # a subgraph
            c.attr(rank='same')
            node_lst=[] #a list of node/state names
            #Conditions for last edge to be terminal or non-terminal
            if(str[-1] not in non_terminals):
                node_nos=len(str)
                flag=True
            else:
                node_nos=len(str)+1
            #Iterating and making resonable node names to graph
            for i in range(node_nos):
                node_name=f'q{ind}'
                ind+=1
                node_lst.append(node_name)
                if(i==node_nos-1): #Special Marking Last state as double circle
                    c.attr('node', shape='doublecircle',color='blue')
                    c.node(node_name)
                else:
                    c.attr('node', shape='circle')
                    c.node(node_name)
            # Marking starting state
            c.attr('node', shape='point')
            c.node(f'{cluster_name}')
            c.edge(f'{cluster_name}', node_lst[0],arrowsize='2',color='red')
            # Adding edges to nodes/states
            str_Index=0
            for index,name in enumerate(node_lst):
                if(index!=len(node_lst)-1):
                    c.edge(node_lst[index],node_lst[index+1],str[str_Index])
                    str_Index+=1
            #Adding last terminal as edge from last node to first node
            if(flag):
                c.edge(node_lst[0],node_lst[-1],str[-1])
        cnt+=1
    g.render(filename='Transition_Diagram',view=True,directory=r"C:\Users\ashut\Desktop\Compiler Design Lab\Images")


result = rem(gram)  #Output Grammer,after removal of left recursion
PrintGrammer(result) #printing resultant Grammer to Console

non_terminals=[key for key in result] #non-terminals from Grammer after Removing Left Recursion
#Modifying Grammer and storing in gram1
gram1=dict()
for key,prod in result.items():
    i=0
    length=len(prod)
    lst=[]
    while i<length:
        val=prod[i]
        for j in val:
            lst.append(j)
        i+=1
    gram1[key]=lst

printProcedure(gram1,non_terminals)  #printing recursive Procedure

DrawTransitionDiagram(gram1,non_terminals) #Drawing grammer transitions



#writing recursive procedure
# gram1={"T":["F","A'"]}
# for key,prod in gram1.items():
#     print("Procedure: "+key+"()")
#     print("Begin:\t")
#     for str in prod:
#         if(str in non_terminals):
#             print("\t"+str+"()")
#         elif(str not in non_terminals):
#             print("if an input symbol '{str}' then :\n\t\tBegin:\n")

