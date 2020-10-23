# Ryan Wu
# CS 76, PA4
# October 2020

from math import inf
import random

# VARIABLE HEURISTICS
# returns the next variable that hasn't been assigned
def next_var(csp, assignment):
    for vars in csp.variables:
        if not vars in assignment:
            return vars

#returns the variable with the fewest legal values
def mrv_heuristic(csp, assignment):
    min = inf
    final = None
    for var in csp.variables:
        if not var in assignment:
            #smaller domain means less legal values
            if len(csp.domains[var]) < min:
                min = len(csp.domains[var])
                final = var
    return final

#returns the variable with the most constraints on remaining variables
def degree_heuristic(csp, assignment):
    holder = None
    compare = -1
    #loop through looking for that with most constraints
    for vars in csp.variables:
        if not vars in assignment:
            counter = 0
            for border in csp.constraints:
                if border[0] == vars and not border[1] in assignment:
                    counter += 1
            #compare the number of constraints
            if counter > compare:
                compare = counter
                holder = vars
    return holder


# DOMAIN HEURISTIC
# returns the domains in the order of csp.domains
def inorder(csp, var, assignment):
    return csp.domains[var]

# returns them randomized
def randomize(csp, var, assignment):
    result = csp.domains[var].copy()
    random.shuffle(result)
    return result

# returns in order the values that rules out the fewest values in the remaining variables first
def lcv_heuristic(csp, var, assignment):
    #dictionary to hold the amount it rules out
    domain = {}
    for i in csp.domains[var]:
        domain[i] = 0
    # get the amount of values each variable rules out
    for keys in csp.constraints:
        if var == keys[0]:
            if not var in assignment:
                for i in domain:
                    if not domain[i] in csp.domains[var]:
                        domain[i] += 1
    # order the list from lowest to highest
    result = []
    while domain:
        curr = inf
        insert = None
        for i in domain:
            if curr > domain[i]:
                curr = domain[i]
                insert = i
        domain.pop(insert)
        result.append(insert)
    return result

