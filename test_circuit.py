# Ryan Wu
# CS 76, PA4
# October 2020
from CircuitProblem import CircuitProblem
from csp_problem import backtracking_search


test = CircuitProblem([(3, 2),(5, 2), (2, 3), (7,1)],
                          (10, 3))
result = backtracking_search(test)
print(result)

test = CircuitProblem([(1, 1),(1, 2), (2, 1), (2,2)],
                          (3, 3))
result = backtracking_search(test)
print(result)

test = CircuitProblem([(1, 1),(1, 2), (2, 1), (2,2), (1, 3)],
                          (3, 3))
result = backtracking_search(test)
print(result)

test = CircuitProblem([(2, 3),(1, 3), (3, 1), (3, 2)],
                          (3, 6))
result = backtracking_search(test)
print(result)