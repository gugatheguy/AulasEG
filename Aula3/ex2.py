from lib2to3.pgen2 import grammar
from traceback import print_tb
from lark import Discard, Lark,Token
from lark.tree import pydot__tree_to_png
from lark import Transformer
from numpy import isin

class transforma_lista(Transformer):
    def __init__(self):
        self.output = {}
        self.num = 0
        self.soma = 0
        self.len = 0
        self.medias = {}
        self.notas = {}
        self.nome = ""
        self.sqlqs = []
        self.turma = ""

    def start(self,items):
        self.output['numAlunos'] = self.num
        self.output['medias'] = self.medias
        self.output['notas'] = self.notas
        self.output['queries'] = []
        self.turma = items[0]
        for e in self.sqlqs:
            self.output['queries'].append(f"INSERT INTO Resultado(nomeAluno,nota,dataInsercao,turma\nVALUES ({e['nome']},{e['nota']},GETDATE(),{self.turma}))")
        return self.output

    def TURMA(self,t):
        return Discard

    def NOME(self,t):
        self.nome = str(t)
        return str(t)

    def PT(self,t):
        return Discard
    
    def PE(self,t):
        return Discard

    def PD(self,t):
        return Discard
    
    def VIR(self,t):
        return Discard
    
    def PTVIR(self,t):
        return Discard

    def aluno(self,t):
        self.num += 1
        self.medias[self.nome] = round(self.soma/self.len,2)
        self.soma = 0
        self.len = 0
        return t[0],t[1]

    def lista(self, t):
        return t

    def NUM(self, t):
        n = int(t)
        self.soma += n
        self.notas.setdefault(n,set())
        self.notas[n].add(self.nome)
        self.len += 1
        self.sqlqs.append({'nome':self.nome, 'nota': n})
        return n

grammar = '''
start : TURMA NOME alunos
TURMA : "TURMA"
alunos : aluno (PTVIR aluno)* PT
aluno: NOME PE lista PD 
lista: NUM (VIR NUM)*
NUM: "0".."9"+
NOME: ("a".."z"|"A".."Z")+
VIR: ","
PTVIR: ";"
PT : "."
PE : "("
PD : ")"
%import common.WS
%ignore WS
'''

l = Lark(grammar)
frase = '''TURMA A
ana (12, 13, 15, 12, 13, 15, 14);
joao (9,7,3,6,9);
xico (12,16).'''
tree = l.parse(frase)
data = transforma_lista().transform(tree)
print(data)