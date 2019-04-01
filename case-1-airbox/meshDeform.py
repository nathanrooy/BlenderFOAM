def main(lattice_number,lattice_direction,lattice_value,lattice_name):
#---MESH DEFORMATION----------------------------------------+
    for w in range(len(lattice_value)):
        lat_num = file("lattice_number.txt", 'a')
        lat_dir = file("lattice_direction.txt", 'a')
        lat_val = file("lattice_value.txt", 'a')
	lat_nme = file("lattice_name.txt", 'a')
    
        print >> lat_num, ('%.f') %(lattice_number[w])
        print >> lat_dir, ('%.f') %(lattice_direction[w])
        print >> lat_val, ('%f') %(lattice_value[w])
	print >> lat_nme, ('%.f') %(lattice_name[w])

        lat_num.close()
        lat_dir.close()
        lat_val.close()
	lat_nme.close()

    print 'Deforming mesh...'
    import os
    os.system('./BlenderMesh/blender -b -P lattice.py') # deform origional blender mesh and export to a new stl

    #Delete old lattice data files
    os.remove("lattice_number.txt")
    os.remove("lattice_direction.txt")
    os.remove("lattice_value.txt")
    os.remove("lattice_name.txt")

    #---SCALE NEWLY DEFORMED BLENDER MESH TO METERS-------------+
    print 'Scalling mesh from [mm]->[m]'
    os.system('surfaceConvert BlenderMesh/Mesh/airBoxMesh.stl BlenderMesh/Mesh/airBoxMesh_oriented.stl -scale 0.001') # [only works from terminal...]
    os.remove('BlenderMesh/Mesh/airBoxMesh.stl') # delete blender mesh that was not converted to [m]

    return 
