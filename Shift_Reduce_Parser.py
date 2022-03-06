#Program to implement Shift Reduce Parser

# <---------------------INPUT GRAMMERS-------------------->

# gram = {
# 	"S":["S+S","S*S","i"]
# }
# gram = {
#     "E":["E+T","T"],
#     "T":["T*F","F"],
#     "F":["(E)","i"]
# }
gram = {
	"S":["(L)","a"],
	"L":["L,S","S"]
}
#<-----------------------INPUT ENDS----------------------->

starting_terminal = list(gram.keys())[0] #Starting symbol
inp = input("Enter input string: ") #input Symbol
stack = "$" #initial stack content
print(f'{"Stack": <15}'+"|"+f'{"Input Buffer": <15}'+"|"+f'Parsing Action')
print(f'{"-":-<50}')
print(f'{stack: <15}'+"|"+f'{inp: <15}'+"|"+f'------') #Printing Initial State of Parser
while True:
	action = True
	i = 0
	while i<len(gram[starting_terminal]):
		if gram[starting_terminal][i] in stack:
			stack = stack.replace(gram[starting_terminal][i],starting_terminal)
			print(f'{stack: <15}'+"|"+f'{inp: <15}'+"|"+f'Reduce S->{gram[starting_terminal][i]}')
			i=-1
			action = False
		i+=1
	if len(inp)>1:
		stack+=inp[0]
		inp=inp[1:]
		print(f'{stack: <15}'+"|"+f'{inp: <15}'+"|"+f'Shift')
		action = False

	if inp == "$" and stack == ("$"+starting_terminal):
		print(f'{stack: <15}'+"|"+f'{inp: <15}'+"|"+f'Accepted')
		break

	if action:
		print(f'{stack: <15}'+"|"+f'{inp: <15}'+"|"+f'Rejected')
		break