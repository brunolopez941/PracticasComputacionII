# -*- coding: utf-8 -*-
"""MétodosNuméricos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vTFQK7yFrhBvkbrwlDX2IOtxVUT6kNaX

# Métodos numéricos
"""

from sympy.abc import x,y
import numpy as np
import time
from sympy import *
import math


class NaiveMethods:

  def incrementalSearch(self, a, b, func):
    print("Búsqueda exhaustiva")
    X = np.linspace(a, b, 10001)
    Y = np.zeros_like(X)
    existe=False

    for i in range(len(X)):
      if func.subs(x, X[i]) == 0:
        print("La raíz real es: ", X[i])
        existe=True
    if (existe==False):
      print("No se encontró raíz real en el intervalo dado")

class NumericalMethods:

  def bisectionMethod(self,a,b,tol,maxIter,func):
    print("Método de la bisección")
    if (func.subs(x,a)*func.subs(x,b) < 0):
      print("Existe un cambio de signo")
    else:
      print("No existen raices reales en el intervalo")
      return 0

    iteracion=1
    c=(a+b)/2
    error = abs(f.subs(x,c))

    while (error>=tol or iteracion==maxIter):
      c=(a+b)/2.
      producto = func.subs(x,a)*func.subs(x,c)

      if (producto < 0):
        #Hay una raiz en [a,c]
        #a=a
        b=c
      elif (producto > 0):
        #Hay una raiz en [c,b]
        a=c
        #b=b
      elif (producto == 0):
        print("Solución:",c)
        break
      #print("Iteración:",iteracion,"Aproximación:",c)
      error=abs(b-a)
      #print("Error:",error)
      iteracion+=1
    #print("La raíz real se encuentra en:",c)

  def newton(self,x2,f,tol,maxIter):
    print("Método de Newton")
    fp = diff(f,x)
    iteracion=1
    eAbsolute=np.inf

    while (eAbsolute>=tol or iteracion==maxIter):
      x1=x2
      if (fp.subs(x,x1)==0):
        print("Error matemático")
        break
      x2=x1-(f.subs(x,x1)/fp.subs(x,x1))
      #print("Iteración:",iteracion,"Aproximación:",x2)
      eAbsolute=abs(x2-x1)
      #print("Error absoluto:",eAbsolute)
      #print("")
      iteracion+=1

    if (iteracion>maxIter):
      print("No converge a ninguna solución")
    else:
      print("Solución:",x2)

  def secante(self,x1,x2,f,tol,maxIter):
    print("Método de la secante")
    iteracion=1
    eAbsolute=np.inf

    while (eAbsolute>=tol or iteracion==maxIter):
      x0=x1
      x1=x2
      x2=x1-((f.subs(x,x1)*(x1-x0))/(f.subs(x,x1)-f.subs(x,x0)))
      #print("Iteración:",iteracion,"Aproximación:",x2)
      eAbsolute=abs(x2-x1)
      #print("Error absoluto:",eAbsolute)
      #print("")
      iteracion+=1

    if (iteracion>maxIter):
      print("No converge a ninguna solución")
    else:
      print("Solución:",x2)

  def brentDekker(self,a,b,tol,maxIter,f):
    print("Método Brent-Dekker")
    if (f.subs(x,a)*f.subs(x,b)>=0):
      print("No existe raíz en el rango proporcionado")
      return 0
    if (abs(f.subs(x,a))<abs(f.subs(x,b))):
      a,b=b,a

    c=a
    mflag=True
    iteracion=1
    error=np.inf

    while (error>=tol or iteracion==maxIter):
      #print(iteracion)
      if (f.subs(x,a)!=f.subs(x,c) and f.subs(x,b)!=f.subs(x,c)):  
        sa=a*f.subs(x,b)*f.subs(x,c)*(1/(f.subs(x,a)-f.subs(x,b)))*(1/(f.subs(x,a)-f.subs(x,c)))
        sb=b*f.subs(x,a)*f.subs(x,c)*(1/(f.subs(x,b)-f.subs(x,a)))*(1/(f.subs(x,b)-f.subs(x,c)))
        sc=c*f.subs(x,a)*f.subs(x,b)*(1/(f.subs(x,c)-f.subs(x,a)))*(1/(f.subs(x,c)-f.subs(x,b)))
        s=sa+sb+sc
      else:
        s=b-f.subs(x,b)*(b-a)*(1/(f.subs(x,b)-f.subs(x,a)))

      aux=(3*a+b)/4
      delta=0.00001
      if (s>aux and s<b) or (mflag==True and abs(s-b)>=(abs(b-c)/2)) or (mflag==False and abs(s-b)>=(abs(c-d)/2)) or (mflag==True and abs(b-c)<abs(delta)) or (mflag==False and abs(c-d)<abs(delta)):
        s=(a+b)/2
        mflag=True
      else:
        mflag=False

      d=c
      c=b
      if (f.subs(x,a)*f.subs(x,s)<0):
        b=s
      else:
        a=s

      if (abs(f.subs(x,a))<abs(f.subs(x,b))):
        a,b=b,a
      iteracion+=1
      error=abs(b-a)
    print("Solución :",b)


def main():
  #f = 2*x+3
  #f = x**3-1
  #f = x**3-x
  #f = x**3-2*x-5
  f=(x+3)*(x-1)**2
  print("Función:",f)
  print("")
  tol = 0.000000000000001
  maxIter=900
  #x0 es mayor que x1
  #x1 es mayor que x2
  initial1=float(5)
  initial2=float(6)

  start=time.time()
  objN=NaiveMethods()
  objN.incrementalSearch(-5,5,f)
  end=time.time()
  tiempo=end-start
  print("Tiempo de ejecución:",tiempo)
  print("")

  start=time.time()
  objNMBiseccion=NumericalMethods()
  objNMBiseccion.bisectionMethod(-5,5,tol,maxIter,f)
  end=time.time()
  tiempo=end-start
  print("Tiempo de ejecución:",tiempo)
  print("")

  start=time.time()
  objNMNewton=NumericalMethods()
  objNMNewton.newton(initial1,f,tol,maxIter) 
  end=time.time()
  tiempo=end-start
  print("Tiempo de ejecución:",tiempo)
  print("")

  start=time.time()
  objNMSecante=NumericalMethods()
  objNMSecante.secante(initial1,initial2,f,tol,maxIter)
  end=time.time()
  tiempo=end-start
  print("Tiempo de ejecución:",tiempo)
  print("")

  start=time.time()
  objNMBrent=NumericalMethods()
  objNMBrent.brentDekker(-5.,5.,tol,maxIter,f)
  end=time.time()
  tiempo=end-start
  print("Tiempo de ejecución:",tiempo)


if __name__ == "__main__":
  main()