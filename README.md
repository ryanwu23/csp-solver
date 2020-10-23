# Ryan Wu Fall, 2020
## PA4 CS76 - CSP README
## Running the code
In order to test the Map coloring problem, one can run test_mapcoloring.py.
More test cases can also be created as long as you pass in variables, domains, and constraints
(look at report.md at Map Coloring Implementation for clear instructions about parameters).

To test the board circuit problem, one can run test_circuit.py.
More test cases can also be created if you pass in the list of pieces and the board size
(look at report.md at Circuit Board Implementation for clear instructions about parameters).

To change the heuristics used, go into csp_problem.py and read the comments inside the functions select_var and var_domains.
To disable AC-3 follow the directions on csp_problem.py on line 30.