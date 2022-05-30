import numpy as np #libreria para proceso matematicos
import matplotlib.pyplot as plt #libreria para la grafica
from sympy import Symbol #libreria para calcular la derivada
import sympy

#creacion de variables
xi= 0 #variables para inicializar los calculos
x = Symbol('x') #Crea la Variable X
tolerancia = 0.00001
error = 1


f = input("Digite una funcion (con variable x): ")
df = sympy.diff(f) #Deriva a la funcion F

print("La derivada de la funcion es : ",df)

f= sympy.lambdify(x, f) 
df= sympy.lambdify(x, df)

i = 0 #contador para iteracion
while error > tolerancia:
  i+=1
  raiz = xi - (f(xi)/df(xi))
  error = np.abs((raiz-xi)/raiz)
  print('x ',i, '= ', xi) #Imprime las iteraciones para ver cuantas se tuvo que hacer
  xi = raiz

print("La raiz es: ",raiz)
print("El valor de f(x) es: ", f(raiz))

#lineas de codigo para la grafica
xs = np.linspace(raiz-1, raiz+1, 50) #evaluar puntos de raiz-1 y raiz+1, 50 es la cantidad de puntos que deseo tener
plt.plot(xs, f(xs), label = 'f(x)')
plt.title("Metodo Newton - Raphson") #titulo
plt.axhline(y=0, color = 'g') #hacer aparecer la linea en eje Y=0
plt.plot(raiz, f(raiz),'bo',label = f'f(x)=0, x={raiz:.6f}', color= 'k') #comando para ver el punto en la grafica
plt.legend(loc = 'upper left') #legenda
plt.show() #mostrar grafica
