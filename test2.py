
arr={'E': ['T', "E'"], 'T': ['F', "T'"], 'F': ['(', 'E', ')', 'i'], "E'": ['+', 'T', "E'", 'e'], "T'": ['*', 'F', "T'", 'e']}
terminals=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','(',')',',','+','*']
# for k in arr:
#     print(k,end="->")
#     for val in arr[k]:
#         print(val,end=" ")
#     print()



def printProcedure(gram):
    flag=False
    for k in arr:
        print("<--------------------------------->")
        print(f"procedure: {k}()")
        print("Begin:")
        for ch in arr[k]:
            if(ch in terminals and ch !='e'):
                if(flag):
                    print("End ")
                flag=True
                print(f"if an input symbol '{ch}' then,")
                print("Begin: ")
            elif(ch not in terminals):
                print(f"{ch}()")
            elif(ch == arr[k][-1]):
                print("End")
                print('Else')
                if(ch=='e'):
                    print("Null character")
                else:
                    print(f"if an input symbol '{ch}' then")
                    print("Begin\nEnd")
        print("End")
        print("<--------------------------------->")

printProcedure(arr)