#**Question 1.** Utiliser  ces  données  pour  prouver  graphiquement que  la  réaction  d’absorption  de  l’alcool  dans  le  sang  suit  une  loi  cinétique  d’ordre  $1$,  et déterminer sa constante de vitesse $k_1$ (en précisant son unité).

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

c10 = 1/0.250
print("La concentration initiale d'alcool dans l'estomac est de", c10, "mol/L")


t1 = np.array([0, 1.73, 2.8, 5.5, 18, 22])
c1 = np.array([4.0, 3.0, 2.5, 1.6, 0.2, 0.1])

x = np.linspace(t1[0], t1[-1], 1000)



lr1 = scipy.stats.linregress(t1,np.log(c1/c10))
print(lr1)
slope = lr1[0]
intercept = lr1[1]
k1 = abs(slope)
print("Le coefficient de corrélation vaut {:0.6f}".format(abs(lr1.rvalue)))
print("La constante de vitesse de la réaction d'absorption vaut k1 = {:0.4f} min-1".format(k1))


plt.plot(t1,np.log(c1/c10),color='orange', linestyle='--')
plt.scatter(t1,np.log(c1/c10),color='orange', marker='X')

plt.plot(x, slope*x+intercept,'gray',label='régression linéaire',alpha=0.5)

plt.grid()
plt.title("Concentration de l’éthanol dans l’estomac de l’homme en fonction du temps")
plt.xlabel("Temps (min)")
plt.ylabel("Concentration d'alcool dans l'estomac (mol/L)")
plt.ylim(min(np.log(c1/c10)-0.5), max(np.log(c1/c10))+0.5)
plt.xlim(min(t1-0.2), max(t1+0.2))

plt.show()


#**Question 2.** Calculer  la  valeur  (en  minutes)  du  temps  de demi-réaction $t_{1/2,1}$ de la réaction d’absorption  de l’alcool dans le sang.

tdemi1 = np.log(2)/k1
print("Le temps de demi-réaction vaut {:0.3f} min".format(tdemi1))