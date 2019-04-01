import bpy
import struct
import mmap
import contextlib
import itertools


print('OPENING BLENDER')
# Check Blender version-----------------------------------------------------------------------------+
version=[2,58,0]
(a,b,c)=bpy.app.version
if a<version[0] or (b==version[1] and c<version[2]):
    msg='Blender too old: %s < %s' % ((a,b,c), tuple(version))
    raise NameError(msg)
else: 
    print ("Blender version - OK")
    
#---OPEN PARAMETRIC MESH----------------------------------------------------------------------------+
print('IMPORTING PARAMETRIC MESH')
bpy.ops.wm.open_mainfile(filepath="BlenderMesh/Mesh/airbox_lattice2.blend")
print('IMPORT COMLETE')


#---DEFORM MESH-------------------------------------------------------------------------------------+
# Import variables to be adjusted
lat_num = open("lattice_number.txt")
lat_dir = open("lattice_direction.txt")
lat_val = open("lattice_value.txt")
lat_nme = open("lattice_name.txt")

lat_number = lat_num.readlines()
lat_direction = lat_dir.readlines()
lat_value = lat_val.readlines()
lat_name = lat_nme.readlines()

# Change lattice control points
print('DEFORMING MESH2')
for i in range(len(lat_value)):
    bpy.data.lattices[str(int(lat_name[i]))].points[int(lat_number[i])].co_deform[int(lat_direction[i])]=float(lat_value[i])
    
print('MESH DEFORMATION COMPLETE')

# Change vertex control points
#bpy.data.meshes['Monkey'].vertices[10].co[1]=1.0

#---Export mesh for OpenFOAM------------------------------------------------------------------------+

# go object mode again
bpy.ops.export_named_mesh.stl(filepath="BlenderMesh/Mesh/airBoxMesh.stl", check_existing=False, ascii=True, apply_modifiers=True)

# Exit Blender
print('MESH MORPHING COMPLETE')
print('CLOSING BLENDER')
#sys.exit()
#bpy.ops.wm.quit_blender()
