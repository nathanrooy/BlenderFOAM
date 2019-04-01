from numpy import loadtxt
from numpy import max
from numpy import mean
import matplotlib.pyplot as plt


#---Import Data From Text Source
BOBYQA_X, BOBYQA_SD, BOBYQA_P, BOBYQA_TIME = loadtxt('NLopt_BOBYQA.txt',unpack=True, usecols=[0,1,2,10])
COBYLA_X, COBYLA_SD, COBYLA_P, COBYLA_TIME = loadtxt('NLopt_COBYLA.txt',unpack=True, usecols=[0,2,3,11])
#MLSL_X, MLSL_Y, MLSL_TIME = loadtxt('OptLog_MLSL.txt',unpack=True, usecols=[0,1,16])
#NELDERMEAD_X, NELDERMEAD_Y, NELDERMEAD_TIME = loadtxt('OptLog_NELDERMEAD.txt',unpack=True, usecols=[0,1,16])
NEWUOA_X, NEWUOA_SD, NEWUOA_P, NEWUOA_TIME = loadtxt('NLopt_NEWUOA.txt',unpack=True, usecols=[0,2,3,11])
#PRAXIS_X, PRAXIS_Y, PRAXIS_TIME = loadtxt('OptLog_PRAXIS.txt',unpack=True, usecols=[0,1,16])
#SBPLX_X, SBPLX_Y = loadtxt('OptLog_SBPLX.txt',unpack=True, usecols=[0,1,16])



#---NORMALIZE RESPONSE VALULES
BOBYQA_P_NORM=[]
BOBYQA_SD_NORM=[]
COBYLA_P_NORM=[]
COBYLA_SD_NORM=[]
NEWUOA_P_NORM=[]
NEWUOA_SD_NORM=[]

global LD_INITIAL
P_INITIAL=-56.5050000000
SD_INITIAL=277.6707620626


for i in range(len(BOBYQA_P)):
    BOBYQA_P_NORM.append(((BOBYQA_P[i]-P_INITIAL)/P_INITIAL)*100)
    BOBYQA_SD_NORM.append(((SD_INITIAL-BOBYQA_SD[i])/SD_INITIAL)*100)
    
for i in range(len(COBYLA_P)):
    COBYLA_P_NORM.append(((COBYLA_P[i]-P_INITIAL)/P_INITIAL)*100)
    COBYLA_SD_NORM.append(((SD_INITIAL-COBYLA_SD[i])/SD_INITIAL)*100)
    
for i in range(len(NEWUOA_P)):
    NEWUOA_P_NORM.append(((NEWUOA_P[i]-P_INITIAL)/P_INITIAL)*100)
    NEWUOA_SD_NORM.append(((SD_INITIAL-NEWUOA_SD[i])/SD_INITIAL)*100)    

#---PRINT RESULTS
print ('---Pressure Improvements [%]---')
print ('BOBYQA optimum: %.10f') %(max(BOBYQA_P_NORM))
print ('COBYLA optimim: %.10f') %(max(COBYLA_P_NORM))
print ('NEWUOA optimim: %.10f') %(max(NEWUOA_P_NORM))

print ('---SD Improvements [%]---')
print ('BOBYQA optimum: %.10f') %(max(BOBYQA_SD_NORM))
print ('COBYLA optimim: %.10f') %(max(COBYLA_SD_NORM))
print ('NEWUOA optimim: %.10f') %(max(NEWUOA_SD_NORM))


print ('---Iterations---')
print ('BOBYQA: %.0f') %(len(BOBYQA_P_NORM))
print ('COBYLA: %.0f') %(len(COBYLA_P_NORM))
print ('NEWUOA: %.0f') %(len(NEWUOA_P_NORM))

print ('---Average Iteration Time (sec)---')
print ('BOBYQA: %.10f') %(mean(BOBYQA_TIME))
print ('COBYLA: %.10f') %(mean(COBYLA_TIME))
print ('NEWUOA: %.10f') %(mean(NEWUOA_TIME))




#---Plot Data: Pressure
plt.figure(1)
plt.plot(BOBYQA_X,BOBYQA_P_NORM,'-',color='#FF0000',alpha=1.0)
plt.plot(COBYLA_X,COBYLA_P_NORM,'-',color='#FFFF00',alpha=1.0)
#plt.semilogy(MLSL_X,MLSL_Y,'-',color='#00CC00',alpha=0.7)
#plt.semilogy(NELDERMEAD_X,NELDERMEAD_Y,'-',color='#009999',alpha=0.7)
plt.plot(NEWUOA_X,NEWUOA_P_NORM,'-',color='#0099FF',alpha=1.0)
#plt.semilogy(PRAXIS_X,PRAXIS_Y,'-',color='#0000FF',alpha=0.7)
#plt.semilogy(SBPLX_X,SBPLX_Y,'-',color='#9900CC',alpha=1)
plt.legend(('BOBYQA','COBYLA','NEWUOA'), loc=7)
#plt.axis([0,45,-300,200])
plt.xlabel("Design Iteration")
plt.ylabel("Pressure Loss Improvement (%)")
plt.grid(True)
plt.savefig('BENCHMARK_4_CONVERGENCE_P.png')

#---Plot Data: SD
plt.figure(2)
plt.plot(BOBYQA_X,BOBYQA_SD_NORM,'-',color='#FF0000',alpha=1.0)
plt.plot(COBYLA_X,COBYLA_SD_NORM,'-',color='#FFFF00',alpha=1.0)
#plt.semilogy(MLSL_X,MLSL_Y,'-',color='#00CC00',alpha=0.7)
#plt.semilogy(NELDERMEAD_X,NELDERMEAD_Y,'-',color='#009999',alpha=0.7)
plt.plot(NEWUOA_X,NEWUOA_SD_NORM,'-',color='#0099FF',alpha=1.0)
#plt.semilogy(PRAXIS_X,PRAXIS_Y,'-',color='#0000FF',alpha=0.7)
#plt.semilogy(SBPLX_X,SBPLX_Y,'-',color='#9900CC',alpha=1)
plt.legend(('BOBYQA','COBYLA','NEWUOA'), loc=7)
#plt.axis([0,45,-300,200])
plt.xlabel("Design Iteration")
plt.ylabel("Flow Uniformity Improvement (%)")
plt.grid(True)
plt.savefig('BENCHMARK_4_CONVERGENCE_SD.png')

#---Plot Data: NEWUOA PERETO FRONT

    
plt.figure(3)
plt.scatter(BOBYQA_P_NORM,BOBYQA_SD_NORM,color='#FF0000',alpha=1.0)
plt.scatter(COBYLA_P_NORM,COBYLA_SD_NORM,color='#FFFF00',alpha=1.0)
plt.scatter(NEWUOA_P_NORM,NEWUOA_SD_NORM,color='#0099FF',alpha=1.0)
plt.legend(('BOBYQA','COBYLA','NEWUOA'), loc=4)
plt.axis([-50,150,-10,30])
#ax = plt.gca()
#ax.set_ylim(ax.get_ylim()[::-1])

plt.xlabel("Pressure Loss Improvement (%)")
plt.ylabel("Flow Uniformity Improvement (%)")
plt.grid(True)
plt.savefig('BENCHMARK_4_NEWUOA_PARETO.png')
plt.show()
