# -*- coding: utf-8 -*-
"""MetodoBiseccion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17TDMqZm0pL9wWZ7ahdAubXFeneKeq_c4

### Comparación de método de bisección y método de exploración exhaustiva
"""

from sympy.abc import x,y
import numpy as np
import time
from sympy import *

class NaiveMethods:

  def incrementalSearch(self, a, b, func):
    X = np.linspace(a, b, 1001)
    Y = np.zeros_like(X)
    
    for i in range(len(X)):
      if func.subs(x, X[i]) == 0:
        print("La raíz real es: ", X[i])

class NumericalMethods:

  def bisectionMethod(self,a,b,tol,maxIter,func):
    if (func.subs(x,a)*func.subs(x,b) < 0):
      print("Existe un cambio de signo")
    else:
      print("No existen raices reales en el intervalo")
      return 0

    error = np.inf
    iteracion=1
    while (error>=tol or iteracion==maxIter):
      c=(a+b)/2
      if (func.subs(x,a)*func.subs(x,c) < 0):
        #Hay una raiz en [a,c]
        a=a
        b=c
      elif (func.subs(x,a)*func.subs(x,c) > 0):
        #Hay una raiz en [c,b]
        a=c
        b=b
      elif (func.subs(x,a)*func.subs(x,c) == 0):
        print("La raíz real se encuentra en: ",c)
        break
      error=abs(b-a)
      iteracion+=1


def main():
  maxIter=90
  tol=0.0000000000000001
  func1 = 2*x+3
  func2 = x**3-1
  func3 = x**3-x
  ##Primera ecuación
  #Método ingenuo
  print("Primera ecuación: 2x+3")
  print("Método ingenuo")
  objN = NaiveMethods()
  start=time.time()
  objN.incrementalSearch(-5, 5, func1)
  end=time.time()
  tiempo=end-start
  print("Tiempo de ejecución: ",tiempo)
  
  #Método de bisección
  print("Método de bisección")
  objNM = NumericalMethods()
  start=time.time()
  objNM.bisectionMethod(-5,5,tol,maxIter,func1)
  end=time.time()
  tiempo=end-start
  print("Tiempo de ejecución: ",tiempo)
  print("")

  ##Segunda ecuación
  #Método ingenuo
  print("Segunda ecuación: x^3-1")
  print("Método ingenuo")
  objN = NaiveMethods()
  start=time.time()
  objN.incrementalSearch(-5, 5, func2)
  end=time.time()
  tiempo=end-start
  print("Tiempo de ejecución: ",tiempo)
  
  #Método de bisección
  print("Método de bisección")
  objNM = NumericalMethods()
  start=time.time()
  objNM.bisectionMethod(-5,5,tol,maxIter,func2)
  end=time.time()
  tiempo=end-start
  print("Tiempo de ejecución: ",tiempo)
  print("")

  ##Tercera ecuación
  #Método ingenuo
  print("Tercera ecuación: x^3-x")
  print("Método ingenuo")
  objN = NaiveMethods()
  start=time.time()
  objN.incrementalSearch(-5, 5, func3)
  end=time.time()
  tiempo=end-start
  print("Tiempo de ejecución: ",tiempo)
  
  #Método de bisección
  print("Método de bisección")
  objNM = NumericalMethods()
  start=time.time()
  objNM.bisectionMethod(-5,5,tol,maxIter,func3)
  end=time.time()
  tiempo=end-start
  print("Tiempo de ejecución: ",tiempo)

if __name__ == "__main__":
  main()