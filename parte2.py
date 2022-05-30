import numpy as np
import matplotlib.pyplot as plt
from sympy import Symbol


fx = lambda x: (x**3)-2*x-5
dx = lambda x: 3*(x**2)-2
xi= 0
x = Symbol('x')
y = (x**3)-2*x-5
dxx =y.diff(x)
print(dxx)

tolerancia = 0.00001
error = 1

while error > tolerancia:
  raiz = xi - (fx(xi)/dx(xi))
  error = np.abs((raiz-xi)/raiz)
  xi = raiz

print("la raiz es: ",raiz)
print("y el valor de f(x) es: ", fx(raiz))


xs = np.linspace(raiz-1, raiz+1, 50)
plt.plot(xs, fx(xs), label = 'f(x)')
plt.title("Metodo Newton - Raphson")
plt.axhline(y=0, color = 'g')
plt.plot(raiz, fx(raiz),'bo',label = f'f(x)=0, x={raiz:.6f}', color= 'k')
plt.legend(loc = 'upper left')
plt.show()