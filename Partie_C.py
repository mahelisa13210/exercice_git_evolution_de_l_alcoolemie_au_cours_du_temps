d = 6/100
rhoeth = 0.79*1e3 #g/L
C0m = rhoeth * d # en g/L
Meth = 2*12 +  6*1 + 16
C0 = C0m/Meth
print("La concentration massique de l'éthanol dans la bière est de {} g/L ".format(C0m))
print("La concentration molaire de l'éthanol dans la bière est de {:0.3f} mol/L ".format(C0))

V0 = 50*1e-2 # L
Ve = V0*d # L 
Vs =  40 # L 
t = np.arange(0,260,0.5)
print(C0 * Ve/Vs)
print(1-np.exp(-k1*1),k2)
c = C0 * (V0/Vs) * (1-np.exp(-abs(k1)*t)) - abs(k2)*t
plt.figure(figsize=(8,5))
plt.plot(t, c, color='orange', linestyle = '--', label= "C0 : Concentration d'éthanol dans le sang")
plt.scatter(t,c, color ='orange', marker='X', alpha = 1, linewidth = 0.5)
plt.legend()
plt.ylim(0, max(c)+ 5*max(c)/100)
plt.xlim(0,250)

plt.xlabel('Temps (min)')
plt.ylabel(f"Concentration d'éthanol dans le sang C0 (mol/L)")
plt.grid(True)
plt.show()


cmax = max(c)
print("La valeur de concentration en éthanol maximale d'Alice est de {:0.4f} mol/L".format(cmax))

tmax = t[np.ndarray.argmax(c)]
print("L'instant auquel la concentration en éthanol est maximale dans le sang d’Alice est t = {:0.1f} 
min".format(tmax))

Climmass = 0.5 # en g/L
Climmol = Climmass/Meth # en mol/L
print(Climmol)

if Climmol > cmax : 
    print(f"Alice peut conduire {tmax:0.1f} minutes après avoir consommé ses deux bières ({Climmol}>{cmax})")
else :
    print(f"Alice ne peut pas conduire après {tmax:0.1f} minutes, {cmax:0.4f}>{Climmol:0.4f}")

import numpy as np

idx_cmax = np.argmax(c)


# 2. On cherche les indices après le pic (t > t_cmax) ET où la concentration est autorisée (c < Climmol)
indx = np.where((t > tmax) & (c < Climmol))[0]

if len(indx) > 0 :
    idx_tok = indx[0]
    tok = t[idx_tok]
    print("Le temps au bout duquel Alice aura le droit de prendre le volant est t = {:0.1f} min".format(tok))
else:
    print("Alice n'atteint jamais la limite Climmol dans l'intervalle de temps fourni.")
