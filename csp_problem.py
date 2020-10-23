import heuristics

# starts the recursive backtracking and returns the csp with the solution
def backtracking_search(csp):
    # add the solution path to the csp
    csp.solution = recursive_backtracking({}, csp)
    return csp #return the csp because you can print it out later

# Recursive backtracking function to get solution path
def recursive_backtracking(assignment, csp):
    # node is being visited
    csp.nodes += 1
    # if the assignments has the same length as variables, each variable has been assigned so return the solution
    if len(assignment) == len(csp.variables):
        return assignment
    var = select_var(csp, assignment) #select a value

    # going through each of the possible domains
    for value in var_domains(csp, var, assignment):
        # only adds if its consistent (can be added without breaking constraints)
        if consistent(csp, var, value, assignment):
            domains = csp.domains.copy() #so we don't lose the past domain when backtracking
            # assign the value to the variable and update the domains
            assign(csp, var, value, assignment)

            #this is the arc-consistency algorithm. To get rid of it comment out line 31 and 38-41 and indent left lines 32-37.
            if AC_3(csp):
                result=recursive_backtracking(assignment, csp) #recursive call
                if result: # if found return back up
                    return result
                # reset the domain and get rid of the assignment
                csp.domains = domains
                assignment.pop(var)
            else:
                #if AC-3 fails, reset the domain and get rid of the assignment
                csp.domains=domains
                assignment.pop(var)
    return False

# arc consistency which gets rid of recursive calls
def AC_3(csp):
    csp.AC = True
    arcs = list(csp.constraints.keys())
    # checks each arc
    while arcs:
        pair = arcs.pop(0)
        # make revisions
        if revise(csp, pair[0], pair[1]):
            #check if it fails now
            if len(csp.domains[pair[0]])==0:
                return False
            # adds neighbor arcs
            for con in csp.constraints:
                if con[0] == pair[0] and con[1] != pair[1]:
                    arcs.append((con[1], pair[0]))
    return True

#revising the domain
def revise(csp, x, y):
    revised = False

    for i in csp.domains[x]:
        found=False
        # checks if there is a domain in y that fulfills the constraints in domain x
        for j in csp.domains[y]:
            if i!=j and x!=y and (i, j) in csp.constraints[(x, y)]:
                found=True
        # if not fulfilled, removed the domain and return true to indicate it was revised
        if not found:
            csp.domains[x].remove(i)
            revised = True
    return revised

# assign the value to var and alter the domain
def assign(csp, var, value, assignment):
    # assigning
    assignment[var]=value
    # changing the domain for that assignment
    csp.domains [var] = [value]
    # for each of the connecting constraints, remove that value from the domain
    for con in csp.constraints:
        if con[0] == var:
            domain = list()
            for pairs in csp.constraints[con]:
                if value==pairs[0] and pairs[1] in csp.domains[con[1]]:
                    domain.append(pairs[1])
            csp.domains[con[1]]=domain

# returns a selected variable
def select_var(csp, assignment):
    # can use 3 different lines:
    # func = heuristics.next_var            gives back the next unassigned variable
    # func = heuristics.mrv_heuristic       chooses the variable with the fewest legal values
    # func = heuristics.degree_heuristic    chooses the variable with the most constraints on remaining variables
    func = heuristics.degree_heuristic
    csp.var_heuristic = func.__name__
    return func(csp, assignment)

# returns a list of domains for that variable
def var_domains(csp, var, assignment):
    # can use 3 different lines:
    # func = heuristics.inorder         returns the domains in the order of csp.domains
    # func = heuristics.randomize       returns the list of domains in a randomized order
    # func = heuristics.lcv_heuristic   returns in order the values that rules out the fewest values in the remaining variables first
    func = heuristics.lcv_heuristic
    csp.domain_heuristic = func.__name__
    return func(csp, var, assignment)

# makes sure the the var with the value is consistent with teh current assignment
def consistent(csp, var, value, assignment):
    # goes through the constraints
    for keys in csp.constraints:
        if keys[0] == var and keys[0]==keys[1]:
            return False
        if keys[0] == var and keys[1] in assignment:
            # return false if it fails for one of them
            if not (value, assignment[keys[1]]) in csp.constraints[keys]:
                return False
    return True
