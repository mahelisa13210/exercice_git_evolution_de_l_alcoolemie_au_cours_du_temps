# Question 3. A l’aide de ces données, déterminer l’ordre de cette réaction ainsi que sa constante de vitesse k2.

import numpy as np

t2 = np.array([0, 	120, 	240, 	360, 	480, 	600, 	720])
c2 = np.array([0.05, 	0.0413, 	0.0326, 	0.0239, 	0.0152, 	0.0065, 	0])

c20 = c2[0]
x2 = np.linspace(t2[0], t2[-1], 1000)

lr2 = scipy.stats.linregress(t2,c2)
slope = lr2[0]
intercept = lr2[1]
k2 = abs(slope)

print("Le coefficient de corrélation vaut {:0.6f}".format(abs(lr2.rvalue)))
print("La constante de vitesse de la réaction d'absorption vaut k2 = {:0.6f} min-1".format(k2))


plt.figure()
plt.plot(x2, slope*x2+intercept,'gray',linestyle = '--', label='régression linéaire',alpha=0.5)
plt.scatter(t2,c2, c='orange', label='c2 = f(t2)')
plt.plot(t2,c2, c='orange', alpha = 0.5)
plt.legend()
plt.grid(True)
plt.show

# Question 4. Calculer  en  minutes  le  temps  de  demi  réaction $t_{1/2,2}$ de cette réaction et comparez le au temps de demi-réaction de l’absorption de l’alcool $t_{1/2,1}$. Commentaire?

t_demi_2 = (c20/2 - intercept)/slope
print(f"Le temps de demie-réaction d'élimination de l'alcool t_1/2_2  = {t_demi_2} minutes")

#Il faut presque 10 fois plus de temps pour éliminer la moitié de l'alcool présent dans le sang que pour l'absorber.