from tokenize import Double
from unittest import main
from simplex import Simplex



if __name__ == "__main__":
        
    simplex = Simplex()
    
    def isNotNumber(n: str)  -> bool:
            if(n==''):
                return False
            
            elif (n.isnumeric()):
                return False
            
            elif (n[0]=='-' and n[1:len(n)].isnumeric()):
                return False
            
            elif ( '/' in n):                
            
                if (n[0] == '-' and n[1:n.index('/')].isnumeric() and n[n.index('/')+1:len(n)].isnumeric()):                
                    return False 
            
                elif (n[0:n.index('/')].isnumeric() and n[n.index('/')+1:len(n)].isnumeric()):
                    return False
                
                else:
                    return True
                
            elif ('.' in n):
                
                if (n[0] == '-' and n[1:n.index('.')].isnumeric() and n[n.index('.')+1:len(n)].isnumeric()):                
                    return False 
            
                elif (n[0:n.index('.')].isnumeric() and n[n.index('.')+1:len(n)].isnumeric()):
                    return False
                
                else:
                    return True            
            
            else:
                return True
       
    print('Max - M \t Min - m')    
    m = input()
    
    while (m != 'M' and m != 'm'):
        print('escolha uma das duas opções M/m')
        m = input()
    
    if (m == 'M'):        
        m = 1
        
    else:
        m = -1
        
    z = []
    variable = []
    count = 1

    print('escreva os coeficientes da funçao a otimizar (carregue no enter para acabar o ciclo):')

    while True:  
        n = input(f'x{count}:')        
        
        while (isNotNumber(n)):
           
            print('introduza um valor numerico')
            n = input(f'x{count}:') 
               
        if (n==''):            
            z = [float(i)*m for i in z ]
            print('  ',variable)      
            print('z=',z)
            count -=1
            print()               
            print('Numero de variaveis:',count)
            print()         
            break  
               
        else:
            if('/' in n):
                n = int(n[0:n.index('/')])/int(n[n.index('/')+1:len(n)])
                
            z.append(n)
            variable.append('x'+ str(count))           
            count += 1
             
        
            
    rest = []
    sinals = []
    c_ind = []
    count2 =1
    operation = ['=', '<=', '=<', '=>', '>=']
    n_rest =int(input('Numero de restrições:'))
    
    while (len(rest)<n_rest):        
        print(f'R{count2}:')
        
        r = []
        
        for i in range(count):            
            var = input(f'x{i+1}:')
            
            while (isNotNumber(var)):                
                print('introduza um valor numerico')
                var = input(f'x{count2}:') 
                
            if('/' in var):
                var = int(var[0:var.index('/')])/int(var[var.index('/')+1:len(var)])    
            
            elif (var == ''):
               var = 0
            r.append(var)
           
        r = [float(i) for i in r ]
        
        print('Escolha um sinal entre: = <= =>')    
        s = input('sinal:')
       
        while (s not in operation):
            print('Escolha um sinal entre: = <= =>')
            s = input('sinal:')        
        
        sinals.append(s)    
        
        b = input(f'b{count2}:') 
        
        while (isNotNumber(b)):
            print('introduza um valor numerico')
            b = input(f'b{count2}:')
        
        c_ind.append(float(b)) 
        print()    
       
        rest.append(r)  
        count2 +=1  
        r = []    
       
    for i in range(0,len(rest),1):
        print(f'R{i+1}:',rest[i],sinals[i],c_ind[i])      
    
    print()
   
    
    for i in range(0,len(c_ind),1):
        
        if (c_ind[i] < 0):
            c_ind[i] *= -1
            rest[i] = [-1* value for value in rest[i]]
            
            if (sinals[i] in ['=>','>=']):
                sinals[i] = '<='
            
            elif(sinals[i] in ['<=','=<']):
                sinals[i] = '=>'
                
            else:
                pass
            
        else:
            pass    
        
    for i in range(len(rest)):
        print(f'R{i+1}:',rest[i],sinals[i],c_ind[i])           
   
# criterio de nao negatividade

    print('\n')
    print('criterio de nao negatividade das variaveis')
    
    answer = ''
    a = []
                      
    for i in range(len(variable)):
        print(variable[i],':\n 1 - positiva\n 2- ilimitada\n 3- maior que uma constante positiva\n')       
        answer = int(input('Resposta:'))
        
        while (answer not in [1,2,3]):
            print('Só pode escolher entre 1, 2 e 3!')
            answer = int(input('Resposta:'))         
        
        a.append(answer)
    
    if (a[0] == 2):
            variable[0] = 'x'+ str(1)+'+'
            variable.insert(1,'x'+ str(1)+'-')
            z.insert(1,-1*z[0]) 
                
            for j in range (0,len(rest),1):
                rest[j].insert(1,-1*rest[j][0])
    
    elif (a[0] == 3): 
        const = input('escreva a constante:')
            
        while (isNotNumber(const)):                
            print('introduza um valor numerico')
            const = input('escreva a constante:') 
                
        if('/' in const):
            const = int(const[0:const.index('/')])/int(const[const.index('/')+1:len(const)])
                
        variable[0] = 'x'+'~'+ str(0)            
            
        for j in range (len(c_ind)):
            c_ind[j] -= rest[0][j]*float(const)   
    
        
    for i in range(1,len(a),1): 
        
        if (a[i] == 2):
            if(a[i-1] == a[i]):
                k = i + 1
                variable[k] = 'x'+ str(k)+'+'
                variable.insert(k+1,'x'+ str(k)+'-')
                z.insert(k+1,-1*z[k]) 
                
                for j in range (0,len(rest),1):
                    rest[j].insert(k+1,-1*rest[j][k])
            
            else:
                variable[i] = 'x'+ str(i+1)+'+'
                variable.insert(i+1,'x'+ str(i+1)+'-')
                z.insert(i+1,-1*z[i]) 
                
                for j in range (len(rest)):
                    rest[j].insert(i+1,-1*rest[j][i])
                
        if (a[i] == 3):
            const = input('escreva a constante:')
            
            while (isNotNumber(const)):                
                print('introduza um valor numerico')
                const = input('escreva a constante:') 
                
            if('/' in const):
                const = int(const[0:const.index('/')])/int(const[const.index('/')+1:len(const)])
                
            variable[i] = 'x'+ str(i+1) +'~'           
            
            for j in range (len(c_ind)):
                c_ind[j] -= rest[i][j]*float(const)
                
        
        
                
#######################################################################################################################
#                                                     Forma Standart                                                  #
#######################################################################################################################

# introdução das variaveis de folga


    count3 = 1

    for i in range(0,len(sinals),1):        
        
        if(sinals[i] in ['<=', '=<']):
            variable.append('f'+ str(count3))
            z.append(float(0))
            rest[i].append(float(1))
            
            for j in range(0,len(sinals),1):
                                
                while (len(rest[j]) < len(z)):
                    rest[j].append(float(0))
                            
            count3 += 1    
        
                
        elif(sinals[i] in ['=>', '>=']):
            variable.append('f'+ str(count3))
            z.append(float(0))
            rest[i].append(float(-1))
                       
            for j in range(0,len(sinals),1):
                                
                while (len(rest[j]) < len(z)):
                    rest[j].append(float(0))
            
            count3 += 1
        
        else:
            pass
            
       
                   
                   
# introdução das variaveis artificiais 

    big_M =simplex.bigM(z,m)  
 
    count3 = 1         
     
    for i in range(0,len(sinals),1): 
        
        if(sinals[i] in ['=>', '>=']):
            variable.append('a'+ str(count3))
            z.append(big_M)            
            rest[i].append(float(1))
            
            for j in range(0,len(sinals),1):
                                
                while (len(rest[j]) < len(z)):
                    rest[j].append(float(0))
            
            count3 += 1
                   
        elif(sinals[i] == '=' ):
            variable.append('a'+ str(count3))
            z.append(float(big_M))            
            rest[i].append(float(1))
            
            for j in range(0,len(sinals),1):
                                
                while (len(rest[j]) < len(z)):
                    rest[j].append(float(0))
                    
            count3 += 1
            
        else:
            pass   
    
    variable.append('b')
    z.append(float(0))
    
    for i in range(len(c_ind)):
        rest[i].append(c_ind[i])
                     
    print('\n\n')    
    print(variable)
    print(' ',z)    
    for i in range(len(rest)):
        print(f'R{i+1}:',rest[i])  
                             
    print()
    print()   
    
    # metodo big M     

    idx_aVar =[]

    for i in range(len(variable)):
        if ('a' in variable[i]):
            idx_aVar.append(i)

    for i in range(len(rest)):
    
        for j in range(len(idx_aVar)):
        
            if(rest[i][idx_aVar[j]]==1):
                z = simplex.bigmMet(big_M,z,rest[i])
            
    
    
    print('-----------------------------------------------------------------------------------------------\n')    
    print('  ',variable)
    print('z= ',z)    
    
    for i in range(0,len(rest),1):
        print(f'R{i+1}:',rest[i])  
        
    print()
    print()
    print('-----------------------------------------------------------------------------------------------\n\n')    
    print()
    print()
    
    simplex.objectiveFunction(z)
    
    for i in range(len(rest)):
        simplex.addRest(rest[i])
        
    for i in range(len(variable)-1):
        simplex.addVariabels(variable[i])
        
    simplex.solve()


    
        
        
        
        
        
   
