def func():
    for x in range(1,17):
        
        # fazer repeticoes a cada expoente
        def testa(w):
            return (x+w)%float(expoente*2) == 0
        
        # para d
        expoente = 1
        if testa(0):
            d = 1
        else:
            d = 0
            
        # para c
        expoente = 2
        if testa(0) or testa(1):
            c = 1
        elif testa(2) or testa(3):
            c = 0
            
        # para b
        expoente = 4
        if testa(0) or testa(1) or testa(2) or testa(3):
            b = 1
        elif testa(4) or testa(5) or testa(6) or testa(7):
            b = 0
                
        # para a
        expoente = 8    
        if testa(0) or testa(1) or testa(2) or testa(3) or testa(4) or testa(5) or testa(6) or testa(7):
            a = 1
        elif testa(8) or testa(9) or testa(10) or testa(11) or testa(12) or testa(13) or testa(14) or testa(15):
            a = 0
            
            
        ######################################    
        # ~~~~~~~ AQUI O SEU CIRCUITO ~~~~~~~~
        
        
        S = a or b or c or d
        
        
        
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        ######################################
        
        
        
        
        # so pra fazer tabela
        res = [a,b,c,d]
        
        # imprime a tabela bonitona
        print str(res) + str(S)