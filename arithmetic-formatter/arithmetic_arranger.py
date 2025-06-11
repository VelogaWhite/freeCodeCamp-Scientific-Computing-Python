def printscreen(list):
    i = 0

    while i < len(list):
        if i+2 > len(list):
            print(f"{list[i]:>6}")
        else:
            print(f"{list[i]:>6}", end = '    ')
        i += 1

def arithmetic_arranger(problems, show_answers=False):
    fnlist = [] #first line
    selist = [] #second line
    lineslist = [] #third line
    answerlist = [] 
    count = 0
    for prob in problems:
        #split each problem into 3 sections
        x =prob.split()
        #and split one into each line
        fnlist.append(x[0])
        selist.append(x[1]+ " " +x[2])
        lineslist.append("-" *(len(selist[count]))) #and - to the lineslist according to len of selist
        answer = int(x[0]) + int(x[1] + x[2])
        answerlist.append(answer)
        count += 1

    print(fnlist)
    print(selist)
    ###print(len(selist[0]))
    print(answerlist,"\n")
    printscreen(fnlist)
    printscreen(selist)
    printscreen(lineslist)
    if show_answers == True:
        printscreen(answerlist)
                


    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2000", "45 + 43", "123 + 49"],True)}')
