def initial(iter,costFunction,time_foam,time_pFoam,time_blender,lattice_number,lattice_min,lattice_max,optimizer,converge,):
    iter=1:
    opt_log = file("OptLog.txt", 'a')
        
    for i in range(len(lattice_number)):
        print >>opt_log,('Lattice Point: %.0f, min: %1.4f   max: %1.4f') %(lattice_number[i],lattice_min[i],lattice_max[i])

    print optimizer
    print convergence
    print max func eval
    
    print >> opt_log, ('')
    print >> opt_log, ('')
    print >> opt_log, ('   Iter # |  Function Value    |   Blender   |   Scale   |   Total Deformation   |   paraFoam   |  OpenFOAM')
    print >> opt_log, ('-------------------------------------------------------------')
    opt_log.close()

def regular(iter,costFunction,time_foam,time_pFoam,time_blender):
    time_total.append(time_blender[k-1]+time_scale[k-1]+time_all[k-1])
    opt_log = file("OptLog.txt", 'a')
    print >> opt_log, ('%6.0f %12.4f %12.4f %12.4f %12.4f') %(k,p_Inlet,time_blender[k-1],time_scale[k-1],time_all[k-1])
    opt_log.close()
        
        
