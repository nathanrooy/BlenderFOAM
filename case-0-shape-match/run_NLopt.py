#-----------------------------------------------------------+
#
#   Nathan Rooy - Cranfield University
#   MSC Thesis - Motorsport Engineering & Management
#   Supported by: Engys
#   July 31, 2012
#
#-----------------------------------------------------------+

#-----------------------------------------------------------+
#
#   Benchmark [0]
#   Shape matching of Tyrrell026 2D airfoil
#
#
#-----------------------------------------------------------+

#---NOTES---------------------------------------------------+
#
#
#
#
#
#
#
#-----------------------------------------------------------+
import shutil
import shapeMatch
import nlopt
import time




#---CONSTANTS-----------------------------------------------+
TARGET=[0.000000000000000000000000000000,
        0.007899999618530273437500000000,
        0.010900000110268592834472656250,
        0.023199999704957008361816406250,
        0.027100000530481338500976562500,
        0.029999999329447746276855468750,
        0.031300000846385955810546875000,
        0.032200001180171966552734375000,
        0.017300000414252281188964843750,
        0.032999999821186065673828125000,
        0.033799998462200164794921875000,
        0.034600000828504562377929687500,
        0.035399999469518661499023437500,
        0.036100000143051147460937500000,
        0.036899998784065246582031250000,
        0.038199998438358306884765625000,
        0.039500001817941665649414062500,
        0.040699999779462814331054687500,
        0.041700005531311035156250000000,
        0.043600000441074371337890625000,
        0.045099999755620956420898437500,
        0.046300001442432403564453125000,
        0.047200001776218414306640625000,
        0.048000000417232513427734375000,
        0.051500000059604644775390625000,
        0.052700001746416091918945312500,
        0.053399998694658279418945312500,
        0.053700000047683715820312500000,
        0.053500000387430191040039062500,
        0.052900001406669616699218750000,
        0.051800001412630081176757812500,
        0.050299998372793197631835937500,
        0.048200000077486038208007812500,
        0.045600000768899917602539062500,
        0.043800000101327896118164062500,
        0.044300004839897155761718750000,
        0.047899998724460601806640625000,
        0.050200000405311584472656250000,
        0.052999999374151229858398437500,
        0.056200001388788223266601562500,
        0.059900000691413879394531250000,
        0.061900001019239425659179687500,
        0.064000003039836883544921875000,
        -0.007600000128149986267089843750,
        -0.010700000450015068054199218750,
        -0.016799999400973320007324218750,
        -0.022800000384449958801269531250,
        -0.026599999517202377319335937500,
        -0.029400000348687171936035156250,
        -0.032000001519918441772460937500,
        -0.034499831497669219970703125000,
        -0.036899998784065246582031250000,
        -0.039299998432397842407226562500,
        -0.041600000113248825073242187500,
        -0.043800000101327896118164062500,
        -0.046000000089406967163085937500,
        -0.048099998384714126586914062500,
        -0.052000001072883605957031250000,
        -0.055700000375509262084960937500,
        -0.059099998325109481811523437500,
        -0.062199998646974563598632812500,
        -0.067599996924400329589843750000,
        -0.071800000965595245361328125000,
        -0.075000002980232238769531250000,
        -0.076899997889995574951171875000,
        -0.077799998223781585693359375000,
        -0.076200000941753387451171875000,
        -0.073200002312660217285156250000,
        -0.069200001657009124755859375000,
        -0.064499996602535247802734375000,
        -0.059000000357627868652343750000,
        -0.045400001108646392822265625000,
        -0.037300001829862594604492187500,
        -0.028500000014901161193847656250,
        -0.018799999728798866271972656250,
        -0.008299999870359897613525390625,
        0.003099999856203794479370117188,
        0.015200000256299972534179687500,
        0.033599998801946640014648437500,
        0.039200000464916229248046875000,
        0.044900000095367431640625000000,
        0.053700000047683715820312500000]

#---4 Lattice Control Points
#lattice_number=[1,2,5,6]
#lattice_direction=[1,1,1,1]         
#lattice_value=[-0.121,-0.265,0.864,0.023] # intitial

#---10 Lattice Control Points
lattice_number=[1,2,3,4,5,8,9,10,11,12]
lattice_direction=[1,1,1,1,1,1,1,1,1,1]         
lattice_value=[-0.286,-0.265,-0.136,-0.198,-0.233,0.959,0.383,0.761,0.208,0.1] # intitial

#---Main Cost Function---------------------------------------+
iter=1
def CostFunction(x0,grad):
    global lattice_number
    global lattice_direction
    global TARGET
    global iter
    lattice_value=x0

    e0_T=time.time()

    #---Deform Mesh
    verts=shapeMatch.main(lattice_number,lattice_direction,lattice_value)
    
    #---Cost Function
    errorTemp=[]
    for i in range(len(TARGET)):
        errorTemp.append((float(TARGET[i])-float(verts[i]))**2)
    answer=sum(errorTemp)

    #---Misc...
    time_Total=time.time()-e0_T

    #---Add Log Entry
    opt_log = file("NLopt_CRS.txt", 'a')
    print >> opt_log, ('%6.0f %16.10f %16.10f') %(iter,answer,time_Total)
    opt_log.close()
    

    #---Iteration counter
    iter=iter+1
    return answer

#---OPTIMIZATION STUFF--------------------------------------+

dimensions=len(lattice_number)

#---GLOBAL OPTIMIZATION ALGORITHMS
#opt = nlopt.opt(nlopt.GN_ORIG_DIRECT, dimensions)          # Direct Original
#opt = nlopt.opt(nlopt.GN_ORIG_DIRECT_L, dimensions)                 # Direct-L Original
#opt = nlopt.opt(nlopt.GN_DIRECT, dimensions)               # Direct
#opt = nlopt.opt(nlopt.GN_DIRECT_L, dimensions)             # Direct-L
#opt = nlopt.opt(nlopt.GN_DIRECT_NOSCAL, dimensions)        # Direct   [no scale]
#opt = nlopt.opt(nlopt.GN_DIRECT_L_NOSCAL, 3)               # Direct-L [no scale]
opt = nlopt.opt(nlopt.GN_DIRECT_L_RAND, dimensions)        # Direct-L RANDOM
#opt = nlopt.opt(nlopt.GN_DIRECT_L_RAND_NOSCAL, dimensions) # Direct-L RANDOM [no scale]
#opt = nlopt.opt(nlopt.GN_CRS2_LM, dimensions)              # Controlled Random Search (CRS) + Local Mutation
#opt = nlopt.opt(nlopt.GN_MLSL, dimensions)                 # MLSL (Multi-Level Single-Linkage)
#opt = nlopt.opt(nlopt.GD_MLSL_LDS, dimensions)             # MLSL (Multi-Level Single-Linkage) + LDS (Low-discrepancy sequence)...SHIT!
#opt = nlopt.opt(nlopt.GN_ISRES, dimensions)                #
#opt = nlopt.opt(nlopt.LN_AUGLAG, dimensions)               # Augmented Lagrangian algorithm

#---LOCAL DERIVATIVE-FREE OPTIMIZATION ALGORITHMS (FIND SLSQP)
#opt = nlopt.opt(nlopt.LN_BOBYQA, dimensions)               # BOBYQA
#opt = nlopt.opt(nlopt.LN_COBYLA, dimensions)               # COBYLA
#opt = nlopt.opt(nlopt.LN_NELDERMEAD, dimensions)           # Nelder-Mead Simplex, use Sbplx instead...
#opt = nlopt.opt(nlopt.LN_NEWUOA, dimensions)               # NEWUOA
#opt = nlopt.opt(nlopt.LN_NEWUOA_BOUND, dimensions)         # NEWUOA+bound constraints
#opt = nlopt.opt(nlopt.LN_PRAXIS, dimensions)               # PRAXIS
#opt = nlopt.opt(nlopt.LN_SBPLX, dimensions)                # Sbplx (based on Subplex)


#---Bounds + Objective
opt.set_min_objective(CostFunction)
#min_A=[-0.5,-0.5,-0.5,-0.5]   # Lattice Control Points
#min_B=[ 1.0, 1.0, 1.0, 1.0]   # Lattice Control Points
min_A=[-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5]   # Lattice Control Points
min_B=[ 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]   # Lattice Control Points
opt.set_lower_bounds(min_A)
opt.set_upper_bounds(min_B)

#---Stopping Criteria
opt.set_stopval(1e-3)                                       # stop when function value of 1e-8 has been surpassed
opt.set_maxeval(10000)                                       # maximum evaluations

#opt.remove_inequality_constraints()
#opt.remove_equality_constraints()


x = opt.optimize(lattice_value)                             #initialize optimization

#---PRINT RESULTS-----------------------------------------------------------------------   
print "\nMethod: ",opt.get_algorithm()
print "Method: ",opt.get_algorithm_name()
print "Dimensions: ",opt.get_dimension()
print "bound min: ",opt.get_lower_bounds()
print "bound max: ",opt.get_upper_bounds()
print "Stop Val.: ",opt.get_stopval()
print "optimum  : ",opt.last_optimum_value()
print "max func. evaluations: ",opt.get_maxeval()
print "optimization parameter tolerance: ",opt.get_xtol_abs()




    
