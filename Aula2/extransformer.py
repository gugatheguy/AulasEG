from lark import Lark,Token
from lark import Transformer

class transforma_lista(Transformer):
  def start(self,items):
    output = {}
    output["sum"] = sum(items[1])
    output["len"] = len(items[1])
    return output
  def elementos(self,items):
    r=list(filter(lambda x: x!=',',items))
    return r
  def PE(self,pe):
    return str(pe)
  def PD(self,pd):
    return str(pd)
  def NUM(self,num):
    return int(num)
  def VIR(self,vir):
    return str(vir)

grammar = '''
start : PE elementos PD
elementos : NUM (VIR NUM)*
PE : "["
PD : "]"
NUM : "0".."9"+
VIR : ","
%import common.WS
'''

# tbm podemos fazer %import common

l = Lark(grammar)
frase = "[1,2,3]"
tree = l.parse(frase)

data = transforma_lista().transform(tree)
print(data)

