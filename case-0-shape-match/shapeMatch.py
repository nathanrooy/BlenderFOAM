#   shapeMatch (Function File)

#   Gets the lattice values from costFunction. From here it writes text files
#   of this data and initilizes meshDeform from the terminal.
import time
import os

def main(lattice_number,lattice_direction,lattice_value):
    #---MESH DEFORMATION----------------------------------------+
    for w in range(len(lattice_value)):
        lat_num = file("lattice_number.txt", 'a')
        lat_dir = file("lattice_direction.txt", 'a')
        lat_val = file("lattice_value.txt", 'a')
    
        print >> lat_num, ('%.f') %(lattice_number[w])
        print >> lat_dir, ('%.f') %(lattice_direction[w])
        print >> lat_val, ('%f') %(lattice_value[w])

        lat_num.close()
        lat_dir.close()
        lat_val.close()

    #print 'Deforming mesh...'
    #e0=time.time()
    os.system('./BlenderMesh/blender -b -P meshDeform.py')
    #time_blender.append(time.time()-e0)


    #---RETURN BACK TO MAIN DIRECTORY
    #os.chdir('../')

    #---Delete old lattice data files
    os.remove("lattice_number.txt")
    os.remove("lattice_direction.txt")
    os.remove("lattice_value.txt")

    #---COLLECT RESULTS
    verts_1 = open("vertices.txt")
    verts_2 = verts_1.readlines()
    os.remove("vertices.txt")
    
    return verts_2
