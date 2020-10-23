# Ryan Wu
# CS 76, PA4
# October 2020
from MapProblem import MapProblem
from csp_problem import backtracking_search

test = MapProblem(["WA", "NT", "SA", "Q", "NSW", "V", "T"],
                      ["Red", "Blue", "Green"],
                      [("WA", "NT"),("WA", "SA"), ("NT","SA"),("NT","Q"),("SA","Q"),("Q","NSW"),("SA","NSW"),("SA","V"),("NSW","V")])
result = backtracking_search(test)
print(result)

# should return no solution because I put WA != WA as a constraint
test = MapProblem(["WA", "NT", "SA", "Q", "NSW", "V", "T"],
                      ["Red", "Blue", "Green"],
                      [("WA", "NT"),("WA", "SA"), ("NT","SA"),("NT","Q"),("SA","Q"),("Q","NSW"),("SA","NSW"),("SA","V"),("NSW","V"), ("WA", "WA")])
result = backtracking_search(test)
print(result)

test = MapProblem(['WA', 'NSW', 'T', 'SA', 'V', 'Q', 'NT'],
                      ["Red", "Blue", "Green"],
                      [("WA", "NT"),("WA", "SA"), ("NT","SA"),("NT","Q"),("SA","Q"),("Q","NSW"),("SA","NSW"),("SA","V"),("NSW","V")])
result = backtracking_search(test)
print(result)

test = MapProblem(['WA', 'V', 'Q', 'SA', 'NT', 'NSW', 'T'],
                      ["Red", "Blue", "Green"],
                      [("WA", "NT"),("WA", "SA"), ("NT","SA"),("NT","Q"),("SA","Q"),("Q","NSW"),("SA","NSW"),("SA","V"),("NSW","V")])
result = backtracking_search(test)
print(result)