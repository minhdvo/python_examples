# LBM in 2D
# fluid passes a single cylinder

#!/usr/bin/csh
import numpy as np
import matplotlib.pyplot as plt
import sys
e=np.array([[0,0],[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,1],[-1,-1],[1,-1]])
w=np.array([4./9.,1./9.,1./9.,1./9.,1./9.,1./36.,1./36.,1./36.,1./36.])
opp=np.array([0,3,4,1,2,7,8,5,6])

# initial set-up
Lx=500+800
lattice_size=25.
ny=int(Lx/lattice_size)
nx=int(Lx/lattice_size)
x_obs=(nx-1)/2.0
y_obs=(ny-1)/2.0
r_obs=250/lattice_size
omega=1.0

image=np.zeros((ny,nx))
u=np.zeros((2,ny,nx))
rho=np.ones((ny,nx))
Feq=np.zeros((9,ny,nx))
rho_0=1.0
beta=5.5e-12

# function for equilibrium density
def computefeq(rho,u):         
        u_sq=u[0]**2+u[1]**2
        for k in range(0,9):
           u_xy=u[0]*e[k,0]+u[1]*e[k,1]
           Feq[k]=w[k]*rho*(1.0+3.0*u_xy+4.5*u_xy**2-1.5*u_sq)
        return Feq

# function for density and velocity
def computemacros(f):              
              rho=np.sum(f,0)
              u[0]=np.sum(f[k]*e[k,0] for k in range(0,9))/rho
              u[1]=np.sum(f[k]*e[k,1] for k in range(0,9))/rho
              return rho,u

# boundaries conditions
def inletoutletboundaries(beta,rho_0,rho_out,rho_in,f,fnew):
  f[1,:,0]=fnew[1,:,nx-1]*(rho_0 + 3.*beta)/rho_out
  f[5,1:,0]=fnew[5,0:ny-1,nx-1]*(rho_0 + 3.*beta)/rho_out
  f[8,0:ny-1,0]=fnew[8,1:,nx-1]*(rho_0 + 3.*beta)/rho_out
  
  f[3,:,nx-1]=fnew[3,:,0]*(rho_0 - 3.*beta*float(nx))/rho_in
  f[6,1:,nx-1]=fnew[6,0:ny-1,0]*(rho_0 - 3.*beta*float(nx))/rho_in
  f[7,0:ny-1,nx-1]=fnew[7,1:,0]*(rho_0 - 3.*beta*float(nx))/rho_in
  return f

for i in range(0,ny):
   for j in range(0,nx):
      if((i-y_obs)**2+(j-x_obs)**2<=r_obs**2):
             image[i,j]=1
post=np.transpose(np.nonzero(image))

l=[]; m=[]; n=[]
for i in range(0,len(post[:,0])):
   for k in range(1,9):
        if(image[post[i,0]+e[k,1],post[i,1]+e[k,0]] - image[post[i,0]-e[k,1],post[i,1]-e[k,0]]==-1):
                                  l.append(k); m.append(post[i,0]); n.append(post[i,1])

Feq=computefeq(1.0,u)
f=Feq.copy()
fnew=Feq.copy()
rho,u=computemacros(f)
time=0
err=1

# main loop
while(time<int(1e4)):

  # calculate equilibrium f
  Feq=computefeq(rho,u)    

  # calculate fnew from collision step
  for k in range(0,9):fnew[k]=(1.0-omega)*f[k]+omega*Feq[k] 
  rho_out=np.mean(rho[:,nx-1])
  rho_in=np.mean(rho[:,0])

  # streaming step
  for k in range(0,9): f[k]=np.roll(np.roll(fnew[k],e[k,1],axis=0),e[k,0],axis=1) 
  f=inletoutletboundaries(beta,rho_0,rho_out,rho_in,f,fnew)
  f[[2,5,6],0,:]=f[[4,7,8],0,:]
  f[[4,7,8],ny-1,:]=f[[2,5,6],ny-1,:]
  rho,u=computemacros(f)
  time+=1

#write data
rho_mean=np.mean(rho)
u_mean=np.mean(u[0])
g=open("vel.txt",'w')
g.write("mean velcity is %e \n" % u_mean)
for i in range(0,ny):
  for j in range(0,nx):
      g.write("%d %d  %e %e %e  \n" %(j*12.5e-9,i*12.5e-9,426.62*u[0,i,j],426.62*u[1,i,j],rho[i,j]))
g.close()

# plot figure
y_analytic=np.arange(float(ny))
u_analytic=3.*beta*y_analytic*(float(ny-1)-y_analytic)/rho_mean

plt.plot(1e8*u[0,:,25],'-r', label='from LBM')
plt.plot(1e8*u_analytic,'b--',lw=2,label="from analytical")
plt.ylabel(r"$v_z$(in lattice units)")
plt.xlabel("z(in lattice units)")
plt.legend(loc='best')
plt.xlim([0,51])
plt.savefig("slit.png",dpi=600)
plt.show()
