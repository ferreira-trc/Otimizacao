from simplex import Simplex

simplex = Simplex()

simplex.objectiveFuncion([1, 2, 4, 0])
simplex.addRest ([0, 4, 6, 7])
simplex.addRest ([0, 6, 8, 5])

simplex.solve()