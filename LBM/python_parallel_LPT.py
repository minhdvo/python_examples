# parallel code for tracking NP
# the interaction of NP and post is considered by using model 2
# there are random and lubrication force

#!/bin/csh/usr
import numpy as np
from multiprocessing import Pool
import random

# initial set up
njobs=400
maxiter=int(5e7)
atot=450.
ai=200.
beta=1.25
Lx=500. + spacing
inv_ai=1./ai
x0=Lx/2.
y0=Lx/2.
eta=0.216181
dt=100.
tau=6.*np.pi*eta*ai
fB2_ini=np.sqrt(2.*dt/tau)
z1=dt/tau

f=np.loadtxt("filename",skiprows=1)
fun1=ip.interp2d(f[:,0],f[:,1],f[:,2])
fun2=ip.interp2d(f[:,0],f[:,1],f[:,3])

y_init=Lx/2.*np.linspace(0,1,njobs)

A=beta**2/(1.+beta)**2
B=(1.+7.*beta+beta**2)/(5.*(1.+beta)**3)
C=(1.+18.*beta-29.*beta**2+18.*beta**3+beta**4)/(21.*(1.+beta)**4)
D=4.*beta*(2.+beta+2.*beta**2)/(15.*(1.+beta)**3)
E=4.*(16.-45.*beta+58.*beta**2-45.*beta**3+16.*beta**4)/(375.*(1.+beta)**4)
emin=0.002*beta/(1.+beta)
emax=0.1*beta/(1.+beta)

# interaction model
def model2(i):
  time=0
  xt=0;yt=y_init[i]
  g=open("file%d.txt"% i,'w')
  while(time<maxiter):
	  x=xt%Lx; y=yt%Lx
          dx=x-x0; dy=y-y0
          r_ij=(dx**2+dy**2)**0.5
          s_ij=r_ij-atot
          e=s_ij*inv_ai

          n1=fB2_ini*random.normalvariate(0.0,1.0)
          n2=fB2_ini*random.normalvariate(0.0,1.0)

          if(e<emax):
             inv_r=1./r_ij
             n_x = dx*inv_r
             n_y = dy*inv_r
             if(e>emin):
                 logterm=np.log(e)
                 tau_sh =(-D*logterm- E*e*logterm)
                 tau_sq =(A/e - B*logterm- C*e*logterm)
                 m=-A/e**2-B/e-C*logterm-C
                 mat_inv=1./(1.+tau_sh)/(1.+tau_sq)
                 slope=z1*mat_inv*((tau_sh-tau_sq)*inv_r - m*(1+tau_sh)/(1.+tau_sq)*inv_ai)
             else:
                 logterm=np.log(emin)
                 tau_sh = (-D*logterm - E*emin*logterm)
                 tau_sq = (A/emin - B*logterm - C*emin*logterm)
                 mat_inv=1./(1.+tau_sh)/(1.+tau_sq)
                 slope=z1*mat_inv*(tau_sh-tau_sq)*inv_r
	     M11=(1.+tau_sq*n_y**2+tau_sh*n_x**2)*mat_inv
             M22=(1.+tau_sq*n_x**2+tau_sh*n_y**2)*mat_inv
             M12=(-tau_sq+tau_sh)*n_x*n_y*mat_inv
             m11=np.sqrt(M11)
             m12=M12/m11
             m22=np.sqrt(M22-m12**2)

             if(s_ij<0):
                    fHS_x=-dt * n_x * s_ij
                    fHS_y=-dt * n_y * s_ij
                    xt = xt + m11*n1 + M11*fHS_x + M12*fHS_y + slope*n_x + fun1(x,y)*dt
                    yt = yt + m12*n1 + m22*n2 + M12*fHS_x + M22*fHS_y + slope*n_y + fun2(x,y)*dt
             else:
                    xt = xt + m11*n1 + slope*n_x + fun1(x,y)*dt
		    yt=yt + m12*n1 + m22*n2 + slope*n_y + fun2(x,y)*dt
          else:
                 xt = n1 + xt + fun1(x,y)*dt
		 yt = n2 + yt + fun2(x,y)*dt
          if(time%1000==0):
             g.write("%d %e  %e \n"%(time,xt,yt))
          time=time+1
  g.close()

# call 20 cores
if __name__ == '__main__':
       pool=Pool(20)
       pool.map(model2,range(njobs))
       pool.close()
       pool.join()
