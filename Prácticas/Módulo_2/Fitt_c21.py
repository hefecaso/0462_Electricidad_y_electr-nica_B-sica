#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Editor de Spyder

@author: Héctor Fernando Carrera Soto

Reporte_4_F2 Jun 2020
"""
import pandas as pd
from scipy.interpolate import interp1d #Contiene todos los métodos numericos
import numpy as np #Ayuda a generar modelos de ecuaciónes
from matplotlib import pyplot as plt #esta librería ayuda a plotear gráficas
import statsmodels.api as smf

xls = pd.ExcelFile('Libro1.xlsx')
df = xls.parse('Sheet1')
#print(df)
#print('')
#print('Datos de voltaje con primera corrida: ')
x = df.loc[:, 'Corriente']
#print(x)
#print('')
y = df.loc[:, 'Voltaje']
#print(y)


'''
print('')
print('')
print('Comparando las tablas para verificar: ')
print('')
print('Si puede ver la sigiente tabla y los datos coinciden, el programa corre bien')
'''
print('')
var = ['Corriente','Voltaje']
df = df[var]
#El (-)indica que buscara datos de [0, infinito)
print(df[-30:])

'''
print('')
print('Imprimiendo datos de Voltaje')
print(x)
print('')
print('')
print('Imprimiendo datos de Corriente')
print(y)
print('')
'''



plt.plot(x, y,'ro', label='Voltaje vs Corriente')
plt.plot(x, y,'black')
plt.title('Gráfica Voltaje (V) vs Corriente (A)')
plt.ylabel('Voltaje')
plt.xlabel('Corriente')
#
#
coeficiente=np.polyfit(x,y,3) #Variables X y Y en ecuación de grado 1
#Otro ejemplo numpy.polyfit(np.log(x), y, 1)
polinomio=np.poly1d(coeficiente) #Hacemos un polinomio para ver los coeficientes como polinomio normal...
#... tomará los coeficientes que obtendremos del polinomio lineal
print(" ")#Imprimimos un espacio en blanco
print("El polinomio del ajuste lineal es: ", polinomio) #Imprimimos el polinomio, en este caso es "0.04743 x + 64.04"
print(" ")#Imprimimos un espacio en blanco
f=interp1d(x,y,3) #Interpolamos para obtener un valor por medio de un ajuste lineal
ys=polinomio(x)#Valores al hacer un ajuste lineal en la gráfica, en este caso, una pendiente constante
plt.plot(x,ys,'blue', label = 'Modelo la ecuación: 2.489e+13 x - 3.784e+08 x - 9.998e+05 x + 12') #g^ imprime en color verde en plt.plot(x,ys,'g^') o para imprimer un guín azúl, solo colocamos (x,y)
plt.legend(loc="upper left") #loc imprime las etiquetas de las gráficas, upper left las coloca a la izquierda
plt.grid() #Imprime una cuadrícula en la gráfica


# endog = variable dependiente, exog = variable independiente
reg = smf.OLS(formula ='Voltaje(V) * Corriente(A)', endog=y, exog=x, data=df)
df = df.dropna()
res = reg.fit()
print(res.summary())
print('')



print('==============================================================================')
test = smf.stats.linear_rainbow(res)
print('Diagnóstico y test: ',test)

r2 = res.rsquared
print('r^2 = ',r2 )
print('==============================================================================')
print('')


