with open('tema_4_2.6_d.in', 'r') as f:
    lines=f.readlines()


def cfg_create(lines):
    variables = set() #set pentru variabile
    terminals = set() #set pentru terminale
    new_terminals=set() 
    starting_variable = [] #variabila de start
    cfg={} #dictionarul care contine cfg ul
    productions = [] #lista pentru tranzitii


    for line in lines:
        productions.append(line.strip()) #se adauga productiile

    for line in lines:  
        aux=""
        variable_flag = False  #flag pentru a determina daca am gasit o variabila
        for letter in line:
            if letter == "<":  # variabilele sunt intre < >
                variable_flag = True
            elif letter == ">":
                variable_flag= False
                variables.add(aux)
                if not starting_variable:
                    starting_variable.append(aux)  #se adauga variabila de start
                aux=""
            elif variable_flag == True:
                aux += letter


    for line in lines:
        aux = " "
        terminal_flag = False  # flag pentru a determina daca am gasit un terminal
        for letter in line:
            if letter == '"':  # simbolurile care sunt intre " " sunt terminale
                terminal_flag = not terminal_flag
            elif terminal_flag:
                aux += letter
            elif aux:
                terminals.add(aux.strip('"'))
                aux = ""


    for terminal in terminals: # se verifica sa nu existe spatii 
        if terminal != ' ':
            new_terminals.add(terminal)
# epsilon e "E"
# se creeaza cfg ul care are ca si chei : 'variables', 'terminals', 'start', 'productions' si ca si valori multimile / listele corespunzatoare
    cfg["variables"] = variables
    cfg["terminals"] = new_terminals
    cfg["start"] = starting_variable
    cfg["productions"] = productions

    return cfg


result = cfg_create(lines)
print("cfg : ",result)