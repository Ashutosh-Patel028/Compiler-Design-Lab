
def print_iter(Matched,Stack,Input,Action,verbose=True):
    if verbose==True:
        print(".".join(Matched).ljust(30)," | ",".".join(Stack).ljust(25)," | ",".".join(Input).ljust(30)," | ",Action)
#The predictive parsing algorithm
def predictive_parsing(sentence,parsingtable,terminals,start_state="S",verbose=True):      #Set verbose to false to not see the stages of the algorithm
    status = None
    match = []
    stack = [start_state,"$"]
    Inp = sentence.split(".")
    if verbose==True:
        print_iter(["Matched"],["Stack"],["Input"],"Action")
    print_iter(match,stack,Inp,"Initial",verbose)
    action=[]
    while(len(sentence)>0 and status!=False):
        top_of_input = Inp[0]
        pos = top_of_input
        if stack[0] =="$" and pos == "$" :
            print_iter(match,stack,Inp,"Accepted",verbose)
            return "String Accepted"
        if stack[0] == pos:
            print_iter(match,stack,Inp,"Pop {0}".format(stack[0]),verbose)
            match.append(stack[0])
            del(stack[0])
            del(Inp[0])
            continue
        if stack[0]=="epsilon":
            print_iter(match,stack,Inp,"Poping Epsilon",verbose)
            del(stack[0])
            continue
        try:
            production=parsingtable[stack[0]][pos]
            print_iter(match,stack,Inp,stack[0]+" -> "+production,verbose)
        except:
            return "error for "+str(stack[0])+" on "+str(pos),"Not Accepted"

        new = production.split(".")   
        stack=new+stack[1:]
    return "Not Accepted"

if __name__=="__main__":
    #String Acceptence in Predictive Parser
    # #input for the grammar : E->TE1;E1->+TE1|epsilon;T->FT1 ...
    # parsingtable = {
    # "E" : {"id" : "T.E1", "(" : "T.E1"},
    # "E1" : {"+":"+.T.E1", ")":"epsilon", "$" : "epsilon"},
    # "T" : {"id" : "F.T1", "(" : "F.T1" },
    # "T1" : {"+" : "epsilon", "*" : "*.F.T1", ")" : "epsilon", "$" : "epsilon"},
    # "F":{"id":"id","(":"(.E.)"}
    # }
    # terminals = ["id","(",")","+","*"]
    # print(predictive_parsing(sentence="id.+.(.id.+.id.).$",parsingtable=parsingtable,terminals=terminals,start_state="E",verbose=True))
    
    parsingtable = {
    "S" : {"(" : "(.L.)", "a" : "a"},
    "L" : {"(":"S.L1", "a":"S.L1"},
    "L1" : {")" : "epsilon", "," : ",.S.L1" }
    }
    terminals=["(",")",",","a"]
    string="(.a.,.a.).$"
    start_state="S"
    print(predictive_parsing(sentence=string,parsingtable=parsingtable,terminals=terminals,start_state=start_state))
    
    
    #Another Example done in class:-
    # print(predictive_parsing(sentence="c.c.c.c.d.d.$",parsingtable={"S" : {"c":"C.C","d":"C.C"},"C":{"c":"c.C","d":"d"}},terminals=["c,d"],start_state="S"))
