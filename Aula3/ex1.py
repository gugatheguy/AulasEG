from lib2to3.pgen2 import grammar
from traceback import print_tb
from lark import Discard, Lark,Token
from lark.tree import pydot__tree_to_png
from lark import Transformer
from numpy import isin

class transforma_lista(Transformer):
    def __init__(self):
        self.output = {}
        self.soma = 0
        self.len = 0
        self.freqDict = {}
        self.isAdding = False

    def start(self,items):
        self.output["len"] = self.len
        self.output['mostfreq'] = max(self.freqDict.items() , key= lambda x : x[1])[0]
        self.output['soma'] = self.soma
        return self.output

    def elementos(self,items):
        return items

    def elemento(self, word):
        self.len += 1
        pal = word[0]
        self.freqDict.setdefault(pal,0)
        self.freqDict[pal] += 1
        return pal

    def WORD(self,word):
        pal = str(word)
        if pal == "agora":
            self.isAdding = True
        elif pal == "fim":
            self.isAdding = False
        return str(word)

    def NUM(self,num):
        n = int(num)
        if self.isAdding:
            self.soma += int(n)
        return n

    def LISTA(self,lista):
        return str(lista)

    def PT(self,pt):
        return Discard


    def VIR(self,vir):
        return Discard

grammar = '''
start : LISTA elementos PT
LISTA : "Lista" | "LISTA"
elementos : elemento (VIR elemento)*
elemento: NUM | WORD
NUM: "0".."9"+
WORD: ("a".."z"|"A".."Z")+
VIR: ","
PT : "."
%import common.WS
%ignore WS
'''

l = Lark(grammar)
frase = "Lista 1,agora, 1, 2,ola,ola, fim, agora, 3 ,agora, ola, 4, fim, 7, 8, ola."
tree = l.parse(frase)
data = transforma_lista().transform(tree)
print(data)