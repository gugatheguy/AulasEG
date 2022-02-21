# ------------------------------------------------------------
# teste4 : Intervalos
# ------------------------------------------------------------
import sys
import ply.yacc as yacc
from teste4_lex import tokens

def p_sequencia(p):
    "sequencia : sentido intervalos"
    if p[2] == -1:
       print("falhou!")
    else:
       print("máximo: ",p[2])

def p_sentidoA(p):
    "sentido : '+'"
    p.parser.flag = True
    p.parser.last = 0

def p_sentidoD(p):
    "sentido : '-'"
    p.parser.flag = False
    p.parser.last = 100000000

def p_intervalos_intervalo(p):
    "intervalos : intervalo"
    p[0] = p[1]

def p_intervalos_intervalos(p):
    "intervalos : intervalos intervalo"
    #p[0] = p[2] if (p[1]!=-1) else -1
    p[0] = max(p[1],p[2]) if (p[1]!=-1 and p[2]!=-1) else -1

def p_intervalo(p):
    "intervalo : '[' NUM ',' NUM ']'"
    p[0] = -1
    if (p.parser.flag and (p[2] > p.parser.last)) and  (p[4] >= p[2]):
       p[0] = p[4] - p[2]
    if ((not p.parser.flag) and (p[2] < p.parser.last)) and  (p[4] <= p[2]) :
       p[0] = p[2] - p[4]
    p.parser.last = p[4]

def p_error(p):
    print('Syntax error: ', p)
    parser.success = False

#inicio do Parser e Calculadora
parser = yacc.yacc()

for line in sys.stdin:
    parser.success = True
    parser.flag = True
    parser.last = 0
    parser.parse(line)
