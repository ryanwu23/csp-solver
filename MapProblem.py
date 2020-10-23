class MapProblem:

    # Constructor
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        #create the dictionary of constraints
        self.constraints = {}
        insert = list()
        for i in domains:
            for j in domains:
                if i != j:
                    insert.append((i, j))
        for tuple in constraints:
            self.constraints[tuple[::-1]] = insert.copy()
            self.constraints[tuple] = insert.copy()

        #create the dictionary of domains
        self.domains = {}
        for var in self.variables:
            self.domains[var] = domains.copy()

        # for the solution output
        self.AC = False
        self.var_heuristic=None
        self.domain_heuristic=None
        self.nodes=0
        self.solution = None

    # Printing out the solution
    def __str__(self):
        result = "Map Coloring Problem:\n"
        if self.AC:
            result += "AC-3: used\n"
        else:
            result += "AC-3: not used\n"
        result += "Variable heuristic: "+ self.var_heuristic +"\n"
        result += "Domain heuristic: " + self.domain_heuristic + "\n"
        result += "Number of Calls: " + str(self.nodes) + "\n"
        if self.solution == False:
            result += "No Solution Found\n"
        else:
            result += "Solution: " + str(self.solution) + "\n"
        return result
