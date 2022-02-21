from email.policy import default
from lib2to3.pgen2 import grammar
from lark import Lark,Token
from lark.tree import pydot__tree_to_png
from lark import Transformer
from numpy import isin

class transforma_lista(Transformer):
  def start(self,items):
    output = {}
    output["len"] = len(items[1])
    output['mostfreq'] = max(set(items[1]), key = items[1].count)
    output['soma'] = 0
    isAdding = False
    for e in items[1]:
        match(e):
            case "agora":
                isAdding = True
            case "fim":
                isAdding = False
            case default:
                if isAdding and e.isdigit():
                   output['soma'] += int(e)
    return output
  def elementos(self,items):
    return list(filter(lambda x: x!=',',items))
    
  def LISTA(self,lista):
    return str(lista)
  def PT(self,pt):
    return str(pt)
  def ELEM(self,elem):
    return str(elem)
  def VIR(self,vir):
    return str(vir)

grammar = '''
start : LISTA elementos PT
LISTA : "Lista" | "LISTA"
elementos : ELEM (VIR ELEM)*
ELEM: "0".."9"+|("a".."z"|"A".."Z")+
VIR: ","
PT : "."
%import common.WS
%ignore WS
'''

l = Lark(grammar)
#frase = "LISTA 1 ."
#tree = l.parse(frase)
#print(tree)
#print(tree.pretty())
#for element in tree.children:
#    print(element)
#
#tokens = tree.scan_values(lambda x:isinstance(x,Token))
#
#for token in tokens:
#    print(token)
#
#pydot__tree_to_png(tree,"ex1.png")
#
#frase = "Lista aaa ."
#tree = l.parse(frase)
#print(tree)
#print(tree.pretty())

frase = "Lista 1,agora, 1, 2, fim, agora, 3,ola, 4, fim, 7, 8."
tree = l.parse(frase)
data = transforma_lista().transform(tree)
print(data)
#print(tree)
#print(tree.pretty())

