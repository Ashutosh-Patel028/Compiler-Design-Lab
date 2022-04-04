import pandas as pd
import copy
import string
# from google.colab import files
# uploaded = files.upload()
try: 
    a=pd.read_csv("input.csv")
    print(a)
    c=a.shape
    print(c)
    print(type(c))
    l=[]
    o=list("+-*/")
    o1=[]
    r=[]
    for i in range(c[0]):
        l=l+[a['left'][i]]
        d=a['right'][i]
        x=d.split()
        l=l+x

    sizel=len(l)
    for z in range(sizel):
        if(l[z] in o):
            o1=o1+[l[z]]
    o1=list(set(o1))
    li=copy.deepcopy(l)
    for x in o1:
        if(x in li):
            li.remove(x)
    li=list(set(li))
    for b in range(len(li)):
        r=r+["R"+str(b)]
    i=1
    ak=0
    z=0
    ACounter=0
    akm=[]
    while(i):
        if(ak==len(l)):
            i=0
        elif(l[ak].isalpha() and l[ak]==a['left'][z]):
            print("MOV "+str(l[ak])+' , '+str(r[li.index(l[ak])]))
            akm=akm+[r[li.index(l[ak])]]
            ak+=1
        elif(((l[ak].isalpha()) and (l[ak] in a['right'][z]))and (l[ak] not in o1)):
            print("MOV "+str(l[ak])+' , '+str(r[li.index(l[ak])]))
            akm=akm+[r[li.index(l[ak])]]
            ak+=1
            ACounter+=1
            if((len(a['right'][z])==1)and (len(akm)==2)):
               print("STOR "+str(akm[len(akm)-1])+' , '+str(akm[0]))
               akm.clear()
               z+=1
               print("\t")
        elif((l[ak] in a['right'][z]) and ((l[ak]in o1)and l[ak]=="+")):
            print("MOV "+str(l[ak+1])+' , '+str(r[li.index(l[ak+1])]))
            akm=akm+[r[li.index(l[ak+1])]]
            print("ADD "+str(akm[len(akm)-2])+' , '+str(akm[len(akm)-1]))
            akm.pop(len(akm)-2)
            print("STOR "+str(akm[len(akm)-1])+' , '+str(akm[0]))
            ak+=2
            ACounter+=2
            if(len(a['right'][z].split(" "))==ACounter):
                   akm.clear()
                   z+=1
                   ACounter=0
                   print("\t")
        elif((l[ak] in a['right'][z]) and ((l[ak]in o1)and l[ak]=="-")):
            print("MOV "+str(l[ak+1])+' , '+str(r[li.index(l[ak+1])]))
            akm=akm+[r[li.index(l[ak+1])]]
            print("SUB "+str(akm[len(akm)-2])+' , '+str(akm[len(akm)-1]))
            akm.pop(len(akm)-2)
            print("STOR "+str(akm[len(akm)-1])+' , '+str(akm[0]))
            ak+=2
            ACounter+=2
            if(len(a['right'][z].split(" "))==ACounter):
                   akm.clear()
                   z+=1
                   ACounter=0
                   print("\t")
        elif((l[ak] in a['right'][z]) and ((l[ak]in o1)and l[ak]=="*")):
            print("MOV "+str(l[ak+1])+' , '+str(r[li.index(l[ak+1])]))
            akm=akm+[r[li.index(l[ak+1])]]
            print("MUL "+str(akm[len(akm)-2])+' , '+str(akm[len(akm)-1]))
            akm.pop(len(akm)-2)
            print("STOR "+str(akm[len(akm)-1])+' , '+str(akm[0]))
            ak+=2
            ACounter+=2
            if(len(a['right'][z].split(" "))==ACounter):
                   akm.clear()
                   z+=1
                   ACounter=0
                   print("\t")
        elif((l[ak] in a['right'][z]) and ((l[ak]in o1)and l[ak]=="/")):
            print("MOV "+str(l[ak+1])+' , '+str(r[li.index(l[ak+1])]))
            akm=akm+[r[li.index(l[ak+1])]]
            print("DIV "+str(akm[len(akm)-2])+' , '+str(akm[len(akm)-1]))
            akm.pop(len(akm)-2)
            print("STOR "+str(akm[len(akm)-1])+' , '+str(akm[0]))
            akm.clear()
            ak+=2
            ACounter+=2
            if(len(a['right'][z].split(" "))==ACounter):
                   akm.clear()
                   z+=1
                   ACounter=0
                   print("\t")
        elif((l[ak].isnumeric())and(l[ak] in a['right'][z])):
            print("MOV "+str(l[ak])+' , '+str(r[li.index(l[ak])]))
            akm=akm+[r[li.index(l[ak])]]
            ak+=1
            ACounter+=1
            if((len(akm)==2)and (a['right'][z]==l[ak-1])):
               print("STOR "+str(akm[len(akm)-1])+' , '+str(akm[0]))
               akm.clear()
               z+=1
               ACounter=0
               print("\t")
        elif((l[ak] not in o1)or (l[ak] not in string.ascii_lowercase)):
            print("\f Error!\n\f Please enter valid syntax for three address code.\n\f Check your csv file...")
            print(f"\f Error description...\nError in line number {z} and place number {ak}.")
            print(f"\f Error element is {a['right'][z]}.")
            break
except (FileNotFoundError):
    print("Please check you input file. It may possible that file doesn't exist.")
    print("Also check the file name that is given in input section at the starting place.")
except(ArithmeticError):
    print("An arithmetic error is caused due to which program is not proceed futher.Please check for the solution.")
except(IndexError):
    print("List index out of range.")
except:
    print("An exceptions occurred.")