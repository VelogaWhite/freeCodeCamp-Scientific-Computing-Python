def printscreen(data_list):
    print_line = "    ".join([f"{item:>6}" for item in data_list])
    print(print_line)
    
def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 4:
        return 'Error: Too many problems.'
    fnlist = [] #first line
    selist = [] #second line
    lineslist = [] #third line
    answerlist = [] 
    count = 0
    for prob in problems:

        if '*'  in prob:
            return "Error: Operator must be '+' or '-'."
        elif '/' in prob:
            return "Error: Operator must be '+' or '-'."
        
        else:
            #split each problem into 3 sections
            x =prob.split()
            if len(x[0]) and len(x[2]) > 4:
                return 'Error: Numbers cannot be more than four digits.'
            #and split one into each line
            fnlist.append(x[0])
            selist.append(x[1]+ " " +x[2])
            lineslist.append("-" *(len(selist[count]))) #and - to the lineslist according to len of selist
            try:
                answer = int(x[0]) + int(x[1] + x[2])
            except TypeError and ValueError:
                return 'Error: Numbers must only contain digits.'
            answerlist.append(answer)
            count += 1
  
    printscreen(fnlist)
    printscreen(selist)
    printscreen(lineslist)
    if show_answers == True:
        printscreen(answerlist)
                


    return problems

print(f'\n{arithmetic_arranger(["3 + 608", "3801 + 2000", "45 + 43", "123 + 49"],True)}')
