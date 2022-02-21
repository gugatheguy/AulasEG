from lib2to3.pgen2 import grammar
from lark import Lark,Token
from lark.tree import pydot__tree_to_png
from lark import Transformer

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
#print(tree)
#print(tree.pretty())
for element in tree.children:
    print(element)

tokens = tree.scan_values(lambda x:isinstance(x,Token))

for token in tokens:
    print(token)

pydot__tree_to_png(tree,"aula2.png")