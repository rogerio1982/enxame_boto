import random
import numpy as np 

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

#function that models the problem
def fit(x,y):
	return x**2 + y**2

#init random
popx= []
popy= []

tam=100
targetx=50#random.randint(0, 100)
targety=50#random.randint(0, 100)

for x in range(tam):
	popx.append(random.randint(0, 100))
	popy.append(random.randint(0, 100))

#print
plt.clf()
plt.plot(popx, popy, '+')
plt.plot(targetx, targety, '*')
plt.show()

#intera sobre os poraque
inter=0
bestx = besty =0
r=8
detect = 0
while inter<100:
	
	for x in range(tam):
		#print ("fim ", popx[x], popy[x])
		#ativar sonar do boto 
		calc= (popx[x] - targetx)**2 + (popy[x]  - targety)**2 
		if (calc< r**2):
			#print("#detect presa ",inter,x,popx[x], popy[x])
			bestx=popx[x] 
			besty=popy[x] 	
			detect +=1
			for a in range(tam):
				#chamar os outros botos
				#vi(t+1) = vi(t) + φ1 * (pB-xi(t)) + φ2 * (gB – xi(t))
				popx[a]= bestx-random.random()+0.2
				popy[a]= besty-random.random()+0.2
	#print ("detect ", detect)
	inter+=1
#print
plt.clf()
plt.plot(popx, popy, '+')
plt.plot(targetx, targety, '*')
plt.show()




