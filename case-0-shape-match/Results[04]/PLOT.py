from numpy import loadtxt
import matplotlib.pyplot as plt


#---Import Data From Text Source
BOBYQA_X, BOBYQA_Y = loadtxt('NLopt_BOBYQA.txt',unpack=True)
COBYLA_X, COBYLA_Y = loadtxt('NLopt_COBYLA.txt',unpack=True)
MLSL_X, MLSL_Y = loadtxt('NLopt_MLSL.txt',unpack=True)
NELDERMEAD_X, NELDERMEAD_Y = loadtxt('NLopt_NELDERMEAD.txt',unpack=True)
NEWUOA_X, NEWUOA_Y = loadtxt('NLopt_NEWUOA.txt',unpack=True)
PRAXIS_X, PRAXIS_Y = loadtxt('NLopt_PRAXIS.txt',unpack=True)
SBPLX_X, SBPLX_Y = loadtxt('NLopt_SBPLX.txt',unpack=True)

#---NORMALIZE RESULTS
BOBYQA_X_NORM=[]
COBYLA_X_NORM=[]
MLSL_X_NORM=[]
NELDERMEAD_X_NORM=[]
NEWUOA_X_NORM=[]
PRAXIS_X_NORM=[]
SBPLX_X_NORM=[]

for i in range(len(BOBYQA_X)):
    BOBYQA_X_NORM.append(BOBYQA_X[i]-1)
    
for i in range(len(COBYLA_X)):
    COBYLA_X_NORM.append(COBYLA_X[i]-1)

for i in range(len(MLSL_X)):
    MLSL_X_NORM.append(MLSL_X[i]-1)

for i in range(len(NELDERMEAD_X)):
    NELDERMEAD_X_NORM.append(NELDERMEAD_X[i]-1)

for i in range(len(NEWUOA_X)):
    NEWUOA_X_NORM.append(NEWUOA_X[i]-1)

for i in range(len(PRAXIS_X)):
    PRAXIS_X_NORM.append(PRAXIS_X[i]-1)

for i in range(len(SBPLX_X)):
    SBPLX_X_NORM.append(SBPLX_X[i]-1)


#---Plot Data
plt.figure(2)
plt.semilogy(BOBYQA_X_NORM,BOBYQA_Y,'-',color='#FF0000',alpha=0.7)
plt.semilogy(COBYLA_X_NORM,COBYLA_Y,'-',color='#FFFF00',alpha=0.7)
plt.semilogy(MLSL_X_NORM,MLSL_Y,'-',color='#00CC00',alpha=0.7)
plt.semilogy(NELDERMEAD_X_NORM,NELDERMEAD_Y,'-',color='#009999',alpha=0.7)
plt.semilogy(NEWUOA_X_NORM,NEWUOA_Y,'-',color='#0099FF',alpha=0.7)
plt.semilogy(PRAXIS_X_NORM,PRAXIS_Y,'-',color='#0000FF',alpha=0.7)
#plt.semilogy(SBPLX_X,SBPLX_Y,'-',color='#9900CC',alpha=1)
plt.legend(('BOBYQA','COBYLA','MLSL','Nelder-Mead','NEWUOA','PRAXIS','SBPLX'))
plt.xlabel("Design Iteration")
plt.ylabel("Function Value")
plt.grid(True)
plt.savefig('BENCHMARK_0_lattice_04.png')
plt.show()
