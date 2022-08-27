from json.tool import main
from simplex import Simplex

if __name__ == "__main__":
    
    variables = ['x1','x2','x3','x4','f1','f2','f3']
    
    z1 = [0.75,-20,0.5,-6,0,0,0,0]
    
    rest1 = [0.25,-8,-1,9,1,0,0,0]
    rest2 = [0.5,-12,-0.5,3,0,1,0,0]
    rest3 = [0,0,1,0,0,0,1,1]
    
    z2 = [0,0,0,0.75,-20,0.5,-6,0]
    
    rest1_1 = [1,0,0,0.25,-8,-1,9,0]
    rest2_2 = [0,1,0,0.5,-12,-0.5,3,0]
    rest3_3 = [0,0,1,0,0,1,0,1]
    
    simplex = Simplex()
    
    for i in range(len(variables)):
        simplex.addVariabels(variables[i])
    
    simplex.objectiveFunction(z1)
    
    simplex.addRest(rest1)
    simplex.addRest(rest2)
    simplex.addRest(rest3)
    
    
    
    simplex.solve()