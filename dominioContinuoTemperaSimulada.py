import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return x**2*np.sin(4*np.pi*x) -\
        y*np.sin(4*np.pi*y+np.pi)+1
                                            
x_axis = np.linspace(-1,2,1000)

X,Y = np.meshgrid(x_axis,x_axis)

Z  = f(X,Y)

x_l = np.array([-1,-1]) 
x_u = np.array([2,2]) 

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot_surface(X,Y,Z,cmap='gray',alpha=.1,rstride=30,cstride=30,edgecolor='k')

x_opt = np.random.uniform(-1,2,size=(2,))
f_opt = f(x_opt[0],x_opt[1])

ax.scatter(x_opt[0],x_opt[1],f_opt,color='red',marker="o",edgecolor='k')
T = 100
sigma = .5
heuristicas = []
for i in range(1000):

    n = np.random.normal(0,scale=sigma,size=(2,))
    x_cand = x_opt + n

    for j in range(x_cand.shape[0]):
        if(x_cand[j] < x_l[j]):
            x_cand[j] = x_l[j]
        if(x_cand[j]>x_u[j]):
            x_cand[j] = x_u[j]

    f_cand = f(x_cand[0],x_cand[1])
    P_ij = np.exp(-(f_cand-f_opt)/T)
    heuristicas.append(f_opt)
    if f_cand<f_opt or P_ij >= np.random.uniform(0,1):
        x_opt = x_cand
        f_opt = f_cand
    
        ax.scatter(x_opt[0],x_opt[1],f_opt,color='red',marker="o",edgecolor='k')

    T = T*.89

ax.scatter(x_opt[0],x_opt[1],f_opt,color='red',s=120,marker="x",edgecolor='k',linewidth=4)

plt.show()


plt.plot(heuristicas)
plt.show()