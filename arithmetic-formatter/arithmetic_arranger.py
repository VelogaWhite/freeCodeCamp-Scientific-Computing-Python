def printscreen(list):
    i = 0

    while i < len(list):
        if i+2 > len(list):
            print(f"{list[i]:>5}")
        else:
            print(f"{list[i]:>5}", end = '    ')
        i += 1

def arithmetic_arranger(problems, show_answers=False):
    fnlist = [] #first line
    selist = [] #second line
    answerlist = []

    for prob in problems:
        #split each problem into 3 sections
        x =prob.split()
        #and split one into each line
        fnlist.append(x[0])
        selist.append(x[1]+ " " +x[2])
        answer = int(x[0]) + int(x[1] + x[2])
        answerlist.append(answer)

    print(fnlist)
    print(selist)
    print(answerlist,"\n")
    printscreen(fnlist)
    printscreen(selist)
    print("----")
    if show_answers == True:
        printscreen(answerlist)

                

        


    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True)}')
