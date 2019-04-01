#-----------------------------------------------------------+
#
#   Nathan Rooy - Cranfield University
#   MSC Thesis - Motorsport Engineering & Management
#   Supported by: Engys
#   August 3, 2012
#
#-----------------------------------------------------------+

#-----------------------------------------------------------+
#
#   Benchmark [4]
#   Shape optimization of Formula Ford airbox
#
#-----------------------------------------------------------+

#---NOTES---------------------------------------------------+
#
#   1) set terminal to current directory ("cd Desktop/ffAirbox_opt/")
#   2) run with following terminal command "python RUN_NLopt.py"
#   3) An error will emerge if the folder iter_0001 already exists
#   4) Must delete created folders (iter_0001,iter_0002,...,ect) after every session   
#
#-----------------------------------------------------------+

import os
import shutil
import time
import meshDeform
import getResults
import runOpenFOAM
import nlopt

#---CONSTANTS-----------------------------------------------+

#---3 Lattice Control Points
lattice_number=[18,18,5,1,3]
lattice_direction=[1,2,2,2,2]         
lattice_value=[0.0,0.0,-0.5,-0.5,-0.5] # intitial guess
lattice_name=[111,111,111,222,222]

#---5 Lattice Control Points




#---Main Cost Function--------------------------------------+
iter=0
def CostFunction(x0,grad):
    global lattice_number
    global lattice_direction
    global lattice_name
    global iter
    lattice_value=x0
    e0_T=time.time()
    
    #---Deform Mesh
    e0=time.time()
    time_some=meshDeform.main(lattice_number,lattice_direction,lattice_value,lattice_name)
    time_Deform=time.time()-e0
    
    #---DUPLICATE INITIAL CASE IN NEW FOLDER
    foldername_new='iter_'+str(iter).zfill(4)                  # duplicates initial OpenFOAM case folder
    shutil.copytree('initial',foldername_new)

    #---MOVE NEWLY DEFORMED MESH TO NEW ITERATION FOLDER
    print 'Moving new mesh into current iteration directory -----------------------'
    shutil.move('BlenderMesh/Mesh/airBoxMesh_oriented.stl',foldername_new +'/constant/triSurface/')  # move over newly defomed mesh into current iteration folder

    #---Run OpenFOAM
    e0=time.time()
    time_mesh_foam=runOpenFOAM.main(foldername_new)
    time_MeshFOAM=time.time()-e0
    
    #---Get Results
    answer=getResults.main(foldername_new)

    #---Cost Function
    response=(answer[1]/answer[0])+500.00

    #---Misc...
    time_Total=time.time()-e0_T

    #---Add Log Entry
    opt_log = file("NLopt_COBYLA.txt", 'a')
    print >> opt_log, ('%6.0f %16.10f %16.10f %16.10f %16.10f %16.10f %16.10f %16.10f %16.10f %16.10f %16.10f %16.10f') %(iter,response,answer[0],answer[1],x0[0],x0[1],x0[2],x0[3],x0[4],time_Deform,time_MeshFOAM,time_Total)
    opt_log.close()

    #---Remove Previous Iteration Folder
    if iter>1:
        iter2=iter-1
        shutil.rmtree('iter_'+str(iter2).zfill(4))
    
    # iteration counter
    iter=iter+1
    
    return response


#---OPTIMIZATION STUFF--------------------------------------+

dimensions=len(lattice_number)

#---GLOBAL OPTIMIZATION ALGORITHMS
#opt = nlopt.opt(nlopt.GN_ORIG_DIRECT, dimensions)          # Direct Original
#opt = nlopt.opt(nlopt.GN_ORIG_DIRECT_L, 3)                 # Direct-L Original
#opt = nlopt.opt(nlopt.GN_DIRECT, dimensions)               # Direct
#opt = nlopt.opt(nlopt.GN_DIRECT_L, dimensions)             # Direct-L
#opt = nlopt.opt(nlopt.GN_DIRECT_NOSCAL, dimensions)        # Direct   [no scale]
#opt = nlopt.opt(nlopt.GN_DIRECT_L_NOSCAL, 3)               # Direct-L [no scale]
#opt = nlopt.opt(nlopt.GN_DIRECT_L_RAND, dimensions)        # Direct-L RANDOM
#opt = nlopt.opt(nlopt.GN_DIRECT_L_RAND_NOSCAL, dimensions) # Direct-L RANDOM [no scale]
#opt = nlopt.opt(nlopt.GN_CRS2_LM, dimensions)              # Controlled Random Search (CRS) + Local Mutation
#opt = nlopt.opt(nlopt.GN_MLSL, dimensions)                 # MLSL (Multi-Level Single-Linkage)
#opt = nlopt.opt(nlopt.GD_MLSL_LDS, dimensions)             # MLSL (Multi-Level Single-Linkage) + LDS (Low-discrepancy sequence)...SHIT!
#opt = nlopt.opt(nlopt.GN_ISRES, dimensions)                #
#opt = nlopt.opt(nlopt.LN_AUGLAG, dimensions)               # Augmented Lagrangian algorithm

#---LOCAL DERIVATIVE-FREE OPTIMIZATION ALGORITHMS (FIND SLSQP)
#opt = nlopt.opt(nlopt.LN_BOBYQA, dimensions)               # BOBYQA	YES
opt = nlopt.opt(nlopt.LN_COBYLA, dimensions)               # COBYLA	NO
#opt = nlopt.opt(nlopt.LN_NELDERMEAD, dimensions)           # Nelder-Mead Simplex, use Sbplx instead...
#opt = nlopt.opt(nlopt.LN_NEWUOA, dimensions)               # NEWUOA
#opt = nlopt.opt(nlopt.LN_NEWUOA_BOUND, dimensions)         # NEWUOA+bound constraints
#opt = nlopt.opt(nlopt.LN_PRAXIS, dimensions)               # PRAXIS	YES
#opt = nlopt.opt(nlopt.LN_SBPLX, dimensions)                # Sbplx (based on Subplex)


#---Bounds + Objective
opt.set_min_objective(CostFunction)
min_A=[-1.25,-0.7,-1.0,-1.0,-1.0]   # 5 Lattice Control Points
min_B=[ 1.25, 1.0, 1.0, 0.0, 0.0]   # 5 Lattice Control Points
opt.set_lower_bounds(min_A)
opt.set_upper_bounds(min_B)

#---Stopping Criteria
#opt.set_stopval(1e-3)                                       # stop when function value of 1e-8 has been surpassed
opt.set_maxeval(250)                                        # maximum evaluations
opt.set_xtol_abs(1e-3)                                      

#opt.remove_inequality_constraints()
#opt.remove_equality_constraints()


x = opt.optimize(lattice_value)                             #initialize optimization

#---PRINT RESULTS-------------------------------------------+
print "\nMethod: ",opt.get_algorithm()
print "Method: ",opt.get_algorithm_name()
print "Dimensions: ",opt.get_dimension()
print "bound min: ",opt.get_lower_bounds()
print "bound max: ",opt.get_upper_bounds()
print "Stop Val.: ",opt.get_stopval()




    
