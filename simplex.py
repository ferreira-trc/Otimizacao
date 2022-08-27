from itertools import count
from tkinter import Variable
from unittest import registerResult, result
from collections import defaultdict
from xml.dom.minidom import Element


class  Simplex :
    
    def __init__(self):
        self.table = []
        self.variabels = []
    
    def objectiveFunction (self, fo: list):
        self.table.append(fo)
    
    def addRest (self, sa: list):
        self.table.append(sa)
        
    def addVariabels (self, variabel: str):
        self.variabels.append(variabel)
        
    def basicVariavels (self) -> list:
        
        basic_variabels = []
                
        for col in range(len(self.variabels)):
            
            if (self.table[0][col] == 0):
                value = []
                
                for line in range(len(self.table)):
                    
                    if (line != 0):                    
                        value.append(self.table[line][col])
                    
                    else:
                        pass
                        
                                       
                if (sum(value) == 1 and (1 or 0 in value)):
                    basic_variabels.append(col)
                                  
        return basic_variabels   
    
    def getEntryVar (self) -> int:
        fo = []
        
        for col in range(len(self.table[0])-1):
            fo.append(self.table[0][col])
            
        c_p = max(fo)        
        idx = self.table[0].index(c_p)
        
        return idx
    
    def getExitVar (self, entry_var: int) -> int:
        result = {}
        vidx = [] 
               
        for line in range(len(self.table)):
            
            if (line > 0):
                
                if (self.table[line][entry_var] > 0):
                    division = self.table[line][-1] / self.table[line][entry_var]
                    result[line] = division
                    
                else:
                    pass
        
        idx = min(result, key=result.get)       

        for line in result.keys():
            
            if (result[line] == min(result.values())):
                vidx.append(int(line))
            
                            
        if (len(vidx)==1):                        
            return idx
        
        else:                      
            basicv = self.basicVariavels()
            k = 0
              
            while (len(vidx)!=1):
                vidx = []
                    
                for line in result.keys():
                    
                    if (line > 0): 
                                      
                        if (self.table[line][entry_var] > 0):                            
                            division = self.table[line][basicv[k]] / self.table[line][entry_var]
                            result[line] = division
                                                
                        else:
                            pass
                
                k += 1       
                idx = min(result, key=result.get) 
            
                for line in result.keys():
                    
                    if (result[line] == min(result.values())):
                        vidx.append(int(line))
                    
                    else:
                        del result[line]    
                    
                    
            idx = vidx[0]
            
            return idx
   
    def calNewPivotLine (self, entry_var: int, exit_var: int) -> list:
        line = self.table[exit_var]
        
        pivot = line[entry_var]
        
        new_pivot_line = [value / pivot for value in line]
        
        return new_pivot_line
   
    def calNewLine(self, line: list, entry_var: int, pivotLine: list) -> list:
        pivot = float(line[entry_var] * -1.0)
        
        resultLine = [value * pivot for value in pivotLine]
        
        newLine = []
        
        for col in range(len(resultLine)):
            sumValue = line[col] + resultLine[col]
            newLine.append(sumValue)
        
        return newLine
    
    def bigM(self,z: list, m: int) -> float:
            maxZ = max(z)
            
            if ( abs(maxZ) == 1):
                maxZ =2
                
            big_M = float(-m*maxZ**10)
            
            return big_M
    
    def bigmMet(self,bigM: float, z: list, artVarLine: list) -> list:
        resultLine = [value * bigM for value in artVarLine]
        
        newZ = []
        
        for i in range(len(resultLine)):
            sumValue = z[i] - resultLine[i]
            newZ.append(sumValue)
        
        return newZ
    
    def dantzigCriterion (self) -> bool:
         positive = list(filter(lambda x: x > 0, self.table[0]))
         
         return False if len(positive) > 0 else True
     
    def showTable (self):        
        max_ = []                
        
        for col in range(len(self.table[0])):
            maxbycol = 0
            
            for line in range(len(self.table)):
                maxbycol = max(maxbycol,len(f"{self.table[line][col]:.2f}"))
                
            max_.append(maxbycol)
        
        for col in range(len(self.variabels)):
            print(' '*(int(max_[col]/8 +1)*8-len(f"{self.variabels[col]}")) + f"{self.variabels[col]}", end = "")    
               
        print('  |'+' '*(int(max_[-1]/8 +1)*8-3) +'RHS\n')
        
        for col in range(len(self.table[0])):
            print('-'*(int(max_[col]/8 +1)*8), end = '') 
              
        print('---') 
               
        for line in range(len(self.table)):
            
            if (line == 1):
                
                for col in range(len(self.table[0])):
                    print('-'*(int(max_[col]/8 +1)*8), end = '')   
                print('---') 
                                                  
            for col in range(len(self.table[0])):                
                
                if ( col == len(self.table[0])-1):
                    print('  |', end='')
                                   
                print(' '*(int(max_[col]/8 +1)*8-len(f"{self.table[line][col]:.2f}")) + f"{self.table[line][col]:.2f}",end = '')
            print("\n") 
   
    def calculate(self):
        entryVar = self.getEntryVar()       
        firstExitLine = self.getExitVar(entryVar)       
        pivotLine = self.calNewPivotLine(entryVar,firstExitLine)               
        self.table[firstExitLine] = pivotLine       
        tableCopy = self.table.copy()       
        idx = 0 
        
        while idx < len (self.table):
            
            if (idx != firstExitLine):
                line = tableCopy[idx]
                newLine = self.calNewLine(line, entryVar, pivotLine)
                self.table[idx] = newLine
                
            idx += 1
    
    def solve(self):
        print('Quadro 0\n')
        self.showTable()        
        z = None
        x = []
        vb = []
        v = self.basicVariavels()
        
        for col in range(len(v)):
            vb.append(self.variabels[v[col]])
            
        print('Base basica:', vb)       
        print(f'variavel a sair: {vb[self.getExitVar(self.getEntryVar())-1]}',f'variavel a entrar: {self.variabels[self.getEntryVar()]}', sep= ' --> ')
        vb.pop(self.getExitVar(self.getEntryVar())-1)       
        vb.insert(self.getExitVar(self.getEntryVar())-1,self.variabels[self.getEntryVar()])               
        self.calculate()        
        print('__________________________________________________________________________________________________________\n')
        print('Quadro 1\n')                
        self.showTable()
        
        count = 2
        
        while not self.dantzigCriterion():            
            print('Base basica:', vb)
            print(f'variavel a sair: {vb[self.getExitVar(self.getEntryVar())-1]}',f'variavel a entrar: {self.variabels[self.getEntryVar()]}', sep= ' --> ')
            vb.pop(self.getExitVar(self.getEntryVar())-1)       
            vb.insert(self.getExitVar(self.getEntryVar())-1,self.variabels[self.getEntryVar()])            
            self.calculate()
            print('__________________________________________________________________________________________________________\n')
            print(f'Quadro {count}\n')            
            print()
            self.showTable()   
            count += 1
        
        print('Base basica:', vb)   
        z = self.table[0][-1]
        
        for col in range(len(self.variabels)):
            
             if ( self.variabels[col] in vb):
                 x.append(self.table[vb.index(self.variabels[col])+1][-1])
                
             else:
                 x.append(float(0))
        
        print('z(x) =',z)        
        print('x =',x)
                 
                
        
          
        
        
        
             
        
        
        
        
        
   
        
      
        