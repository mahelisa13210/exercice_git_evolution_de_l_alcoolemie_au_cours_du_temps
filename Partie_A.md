### A - Absorption de l'alool à travers la paroi stomacale

On cherche dans ce paragraphe à étudier la loi cinétique modélisant le processus d'absorption, c’est à dire que l’on cherche à déterminer son ordre (si elle en possède un) et sa constante de vitesse $k$.

Pour cela, on réalise l’expérience suivante : on fait boire à un homme (initialement à jeun, c’est à dire l’estomac vide) une boisson alcoolisée de volume $V = 250\  mL$ contenant $1\ mole$ d’éthanol. On mesure alors  la  concentration  $c_1$ de l’éthanol dans  l’estomac  de  l’homme  en  fonction  du  temps.  

Les  résultats obtenus sont regroupés dans le tableau ci-dessous:

<table>
   <tr>
       <td>$t$ (en min)</td>
       <td>0</td>
       <td>1,73</td>
       <td>2,8</td>
       <td>5,5</td>
       <td>18</td>
       <td>22</td>
   </tr>
   <tr>
       <td>$c_1$ (en mol/L)</td>
       <td>à déterminer</td>
       <td>3,0</td>
       <td>2,5</td>
       <td>1,6</td>
       <td>0,2</td>
       <td>0,1</td>
   </tr>
</table>

**Question 1.** Utiliser  ces  données  pour  prouver  graphiquement que  la  réaction  d’absorption  de  l’alcool  dans  le  sang  suit  une  loi  cinétique  d’ordre  $1$,  et déterminer sa constante de vitesse $k_1$ (en précisant son unité).

NB. On fera appel pour cela à la fonction [linregress](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html) du sous-module `stats` de SciPy.

**Rappel**

Notons $c_1(t)$ la concentration de l’alcool dans l’estomac au cours du temps et $v_1=-\frac{dc_1}{dt}$ la vitesse d’absorption de l’alcool au niveau de la paroi de l’estomac.

Si la réaction est d’ordre 1, on aura aussi $v_1=kc_1(t)$ et $c_1(t)$ sera donc solution de l’équation différentielle :

$$\frac{dc_1(t)}{dt}+kc_1(t)= 0$$ qui se résout immédiatement en : $$c_1(t) =c_{1,0}.exp^{-kt}$$

où c$_{1,0}$ est la concentration initiale.

Ainsi, si la réaction est bien d’ordre 1, on aura :

$$ln(\frac{c_1(t)}{c_{1,0}})=-kt$$


**Question 2.** Calculer  la  valeur  (en  minutes)  du  temps  de demi-réaction $t_{1/2,1}$ de la réaction d’absorption  de l’alcool dans le sang.