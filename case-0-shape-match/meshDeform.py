import struct
import mmap
import contextlib
import itertools
import bpy
from mathutils import Matrix




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
bpy.ops.wm.open_mainfile(filepath="BlenderMesh/Mesh/tyrell026_RUN_10.blend")
print('IMPORT COMLETE')




#---DEFORM MESH-------------------------------------------------------------------------------------+
# Import variables to be adjusted
lat_num = open("lattice_number.txt")
lat_dir = open("lattice_direction.txt")
lat_val = open("lattice_value.txt")

lat_number = lat_num.readlines()
lat_direction = lat_dir.readlines()
lat_value = lat_val.readlines()


print('DEFORMING MESH')
for i in range(len(lat_value)):
    bpy.data.lattices["Lattice"].points[int(lat_number[i])].co_deform[int(lat_direction[i])]=float(lat_value[i])
    # bpy.data.lattices["Lattice"].points[1].co_deform[1]=-1
print('MESH DEFORMATION COMPLETE')

#bpy.ops.object.mode_set(mode='OBJECT')


outfile=open('vertices.txt','w')


i=0


obj=bpy.data.objects['Plane'] 
obj.to_mesh(scene=bpy.context.scene, apply_modifiers=True, settings='PREVIEW')

while i <= 81:
    planedata=bpy.data.meshes['Mesh']
    planedata.validate()
    planedata.update()  
    vertdata=planedata.vertices[i]
    outfile.write('%.30f\n' %(vertdata.co.y))
    i=i+1

       
outfile.close() 


#bpy.ops.wm.save_mainfile(filepath="tyrell026_RUN_10_01.blend")
