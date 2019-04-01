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


#---Plot Data
plt.figure(2)
plt.semilogy(BOBYQA_X,BOBYQA_Y,'-',color='#FF0000',alpha=0.7)
plt.semilogy(COBYLA_X,COBYLA_Y,'-',color='#FFFF00',alpha=0.7)
plt.semilogy(MLSL_X,MLSL_Y,'-',color='#00CC00',alpha=0.7)
plt.semilogy(NELDERMEAD_X,NELDERMEAD_Y,'-',color='#009999',alpha=0.7)
plt.semilogy(NEWUOA_X,NEWUOA_Y,'-',color='#0099FF',alpha=0.7)
plt.semilogy(PRAXIS_X,PRAXIS_Y,'-',color='#0000FF',alpha=0.7)
plt.semilogy(SBPLX_X,SBPLX_Y,'-',color='#9900CC',alpha=0.7)
plt.legend(('BOBYQA','COBYLA','MLSL','Nelder-Mead','NEWUOA','PRAXIS','SBPLX'))
plt.xlabel("Design Iteration")
plt.ylabel("Function Value")
plt.grid(True)
plt.savefig('BENCHMARK_0_lattice_10.png')
plt.show()
