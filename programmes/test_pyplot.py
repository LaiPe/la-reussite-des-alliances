import numpy as np
import matplotlib.pyplot as plt

x=[]
y=[]
for e in range(2,33):
    x+=[str(e)]
plt.plot(x,y)
plt.xlabel("Nombres de cartes limite pour la victoire")
plt.ylabel("Nombre de bidules")
plt.show()