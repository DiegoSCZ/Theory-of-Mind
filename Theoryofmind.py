import tomsup as ts
import random
import numpy as np

#iniciar el juego de emparejar monedas#
penny = ts.PayoffMatrix(name='penny_competitive')  #se agrega matriz#
print(penny)

jung = ts.RB(bias=0.7) #creación del agente que competirá que escogerá 1 el 70% de las veces#
