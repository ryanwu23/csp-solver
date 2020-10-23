# Ryan Wu
# CS 76, PA4
# October 2020
class CircuitProblem:

    # constructor
    def __init__(self, variables, boardSize):
        self.variables = variables
        self.boardSize=boardSize

        #create the dictionary of domains
        self.domains = {}
        for var in self.variables:
            self.domains[var] = self.get_domain(var)

        #create the dictonary of constraints
        self.constraints = {}
        for i in variables:
            for j in variables:
                if i!=j:
                    self.constraints[(i, j)] = self.get_possible(i, j) #possible starting points for those two variables

        #for the solution output
        self.AC = False
        self.var_heuristic = None
        self.domain_heuristic = None
        self.nodes = 0
        self.solution = None


    # printing out the solution
    def __str__(self):
        result = "Circuit Board Problem:\n"
        if self.AC:
            result += "AC-3: used\n"
        else:
            result += "AC-3: not used\n"
        result += "Variable heuristic: " + self.var_heuristic + "\n"
        result += "Domain heuristic: " + self.domain_heuristic + "\n"
        result += "Number of Calls: " + str(self.nodes) + "\n"
        if self.solution==False:
            result += "No Solution Found\n"
        else:
            result += "Solution: "+str(self.solution)+"\n"
            result += "Board:\n"
            result += self.strBoard()
        return result

    # helper function to get the resulting board in the form of a string
    def strBoard(self):
        w, h = self.boardSize[0], self.boardSize[1]
        board = [[0 for x in range(w)] for y in range(h)]
        counter=0

        # for each piece in the solution set the board values to an incrementing number
        for size in self.solution:
            point=self.solution[size]
            counter+=1
            for x in range (point[0], point[0]+size[0]):
                for y in range(point[1], point[1] + size[1]):
                    board[y][x]=counter

        # convert that number to a, b, c, d ... etc and add to a string
        str = ""
        for y in range(self.boardSize[1]-1, -1, -1):
            for x in range(0, self.boardSize[0]):
                if board[y][x]==0:
                    str+="."
                else:
                    str+=chr(96+board[y][x])
            str+="\n"
        return str

    # helper function to get all the possible values for two pieces
    def get_possible(self, a, b):
        result=list()

        w, h = self.boardSize[0], self.boardSize[1]
        for point1 in self.domains[a]:
            # set the board and for each location, fill out the area of piece
            board = [[0 for x in range(w)] for y in range(h)]
            for x in range(point1[0], point1[0] + a[0]):
                for y in range(point1[1], point1[1] + a[1]):
                    board[y][x] = 1

            # if any of the area in piece 2 over lapps, don't add it. if no overlap, add the two points.
            for point2 in self.domains[b]:
                add=True
                for i in range(point2[0], point2[0] + b[0]):
                    for j in range(point2[1], point2[1] + b[1]):
                        if board[j][i]!=0:
                            add=False
                if add:
                    result.append((point1, point2))
        return result

    # getting the start domain of a piece
    def get_domain(self, size):
        result = []
        # every point where the piece stays in bound
        for x in range (0, self.boardSize[0] - size[0]+1):
            for y in range(0, self.boardSize[1] - size[1]+1):
                result.append((x, y))
        return result
