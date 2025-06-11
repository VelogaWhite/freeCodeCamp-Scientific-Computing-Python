def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    fnlist = [] #first line
    selist = [] #second line
    lineslist = [] #third line
    answerlist = [] 
    for prob in problems:

        if '*'  in prob or '/' in prob:
            return "Error: Operator must be '+' or '-'."
        else:
            #split each problem into 3 sections
            x =prob.split()
            if len(x[0]) > 4 or len(x[2]) > 4:
                return 'Error: Numbers cannot be more than four digits.'
            #and split one into each line

            max_len = max(len(x[0]), len(x[2]))
            column_width = max_len + 2 # +2 for operator and space

            fnlist.append(f"{x[0]:>{column_width}}")
            
            selist.append(f"{x[1]}{' ' * (column_width - len(x[2]) - 1)}{x[2]}")
            lineslist.append("-" *(column_width)) #and - to the lineslist according to len of selist
            try:
                answer = int(x[0]) + int(x[1] + x[2])
            except (TypeError, ValueError):
                return 'Error: Numbers must only contain digits.'
            answerlist.append(str(f"{answer:>{column_width}}"))
       
   
    arranged_output = []
    arranged_output.append("    ".join(fnlist))
    arranged_output.append("    ".join(selist))
    arranged_output.append("    ".join(lineslist))

    if show_answers:
        arranged_output.append("    ".join(answerlist))



    return "\n".join(arranged_output)


print("------------------------------- ")
print(f'\n{arithmetic_arranger(["3255 + 6985", "3801 - 2", "45 + 43", "123 + 49"], True)}')
