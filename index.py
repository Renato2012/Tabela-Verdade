#!/usr/bin/python
#coding=UTF-8

# Leandro Kanis
# version 1
# Renato Araújo
# version 2

"""
Generate table 2^5 [a,b,c,d,e].
"""

for x in range(1, 33):

    # fazer repeticoes a cada expoente
    def testa(w):
        return (x+w)%float(expoente*2) == 0

    # para e
    expoente = 1
    if testa(0):
        e = 1
    else:
        e = 0

    # para d
    expoente = 2
    if testa(0) or testa(1):
        d = 1
    elif testa(2) or testa(3):
        d = 0

    # para c
    expoente = 4
    if testa(0) or testa(1) or testa(2) or testa(3):
        c = 1
    elif testa(4) or testa(5) or testa(6) or testa(7):
        c = 0

    # para b
    expoente = 8
    if testa(0) or testa(1) or testa(2) or testa(3) or testa(4) or testa(5) or testa(6) or testa(7):
        b = 1
    elif testa(8) or testa(9) or testa(10) or testa(11) or testa(12) or testa(13) or testa(14) or testa(15):
        b = 0

    # para a
    expoente = 16
    if testa(0) or testa(1) or testa(2) or testa(3) or testa(4) or testa(5) or testa(6) or testa(7) or testa(8) or testa(9) or testa(10) or testa(11) or testa(12) or testa(13) or testa(14) or testa(15):
        a = 1
    elif testa(16) or testa(17) or testa(18) or testa(19) or testa(20) or testa(21) or testa(22) or testa(23) or testa(24) or testa(25) or testa(26) or testa(27) or testa(28) or testa(29) or testa(30) or testa(31):
        a = 0


    ######################################
    S = a and b and c and d and e

    # so pra fazer tabela
    res = [a,b,c,d,e]

    # imprime a tabela bonitona
    print str(res) + " " + str(S)
