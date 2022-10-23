import tomsup as ts
import random
import numpy as np

# iniciar el juego de emparejar monedas#
penny = ts.PayoffMatrix(name='penny_competitive')  # se agrega matriz#
print(penny)

jung = ts.RB(bias=0.7)  # creación del agente (RB: random bias) que competirá que escogerá 1 el 70% de las veces#

# examine agent
print(f"jung is a class of type: {type(jung)}")
if isinstance(jung, ts.Agent):
    print(f"but jung is also an instance of the parent class ts.Agent")

#hacer que jung elija una opción

choice = jung.compete()

print(f'jung chose {choice} and his probabiliy fo choosing 1 was {jung.get_bias()}.')



