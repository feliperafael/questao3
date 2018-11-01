#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 15:28:09 2018

@author: felipe
"""
import numpy as np
import matplotlib.pyplot as plt

sigma = np.sqrt(33.0) 
mi = 94 #km

def f(x, sigma, mi):
    a = (1.0/((2.0*np.pi)*np.power(sigma,2.0)))
    b = (-0.5*( np.power((x - mi)/sigma, 2.0) ))
    return a*np.exp(b)

x = np.linspace(-5.0*sigma + mi, 5*sigma + mi, num=500)
x_fill = np.linspace(-sigma + mi, sigma + mi, num=200)


plt.ylim(bottom=0,top= max(f(x,sigma,mi))*1.08) #limites em y
#190 e somente um fator de escala para ymax e ymin do grafico aproximadamente 1/0.005
plt.axvline(x=mi - sigma, ymin= 0,  ymax= f(x_fill[0],sigma,mi)*190, color='black', alpha=0.8)
plt.axvline(x=mi + sigma, ymax=f(x_fill[-1],sigma,mi)*190, color='black', alpha=0.8)

#coloca sigmas e mi no grafico
plt.text(x_fill[0]*0.96, f(x_fill[0],sigma,mi), r'$-\sigma$')
plt.text(x_fill[-1]*1.005, f(x_fill[-1],sigma,mi), r'$\sigma$')
plt.text(mi*0.995, f(mi,sigma,mi)*1.04, r'$\mu$')


plt.axvline(x=mi, color='black', ymax= f(mi,sigma,mi)*190 ,alpha=0.5)
plt.fill_between(x_fill, 0.0, f(x_fill,sigma,mi),facecolor='midnightblue', alpha=0.15)   
plt.plot(x, f(x,sigma,mi))

plt.scatter(x_fill[0], f(x_fill[0],sigma,mi),  color="red", label=str(round(x_fill[0],2))+' km')
plt.scatter(x_fill[-1], f(x_fill[-1],sigma,mi),  color="c", label=str(round(x_fill[-1],2))+' km')
plt.scatter(mi, f(mi,sigma,mi),  color="purple", label=str(round(mi,2))+' km')


plt.legend()

plt.xlabel('km')
plt.ylabel('f(x)')
plt.title(r'$\sigma = $'+str(round(sigma,2)))
plt.savefig('questao 3')
plt.show()