# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

bl_info = {
    "name": "NW STL format",
    "author": "Guillaume Bouchard (Guillaum), modified by Niklas Wikstrom",
    "version": (1, 0),
    "blender": (2, 5, 8),
    "api": 35622,
    "location": "File > Import-Export > Stl",
    "description": "NWs Extended Import-Export STL files",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "support": 'OFFICIAL',
    "category": "Import-Export"}

# @todo write the wiki page

"""
Import-Export STL files (binary or ascii)

- Import automatically remove the doubles.
- Export can export with/without modifiers applied
- Export can export to multi solid stl. ASCII only

Issues:

Import:
    - Does not handle the normal of the triangles
    - Does not handle endien
"""

if "bpy" in locals():
    import imp
    if "stl_utils" in locals():
        imp.reload(stl_utils)
    if "blender_utils" in locals():
        imp.reload(blender_utils)

import os

import bpy
from bpy.props import StringProperty, BoolProperty, CollectionProperty
from bpy_extras.io_utils import ExportHelper, ImportHelper


class ImportSTL(bpy.types.Operator, ImportHelper):
    '''Load STL triangle mesh data'''
    bl_idname = "import_mesh.stl"
    bl_label = "My Import STL"

    filename_ext = ".stl"

    filter_glob = StringProperty(default="*.stl", options={'HIDDEN'})

    files = CollectionProperty(name="File Path",
                          description="File path used for importing the STL file",
                          type=bpy.types.OperatorFileListElement)

    directory = StringProperty(subtype='DIR_PATH')

    def execute(self, context):
        from . import stl_utils
        from . import blender_utils

        paths = [os.path.join(self.directory, name.name) for name in self.files]

        if not paths:
            paths.append(self.filepath)

        if bpy.ops.object.mode_set.poll():
            bpy.ops.object.mode_set(mode='OBJECT')

        if bpy.ops.object.select_all.poll():
            bpy.ops.object.select_all(action='DESELECT')

        for path in paths:
            objName = bpy.path.display_name(os.path.basename(path))
            tris, pts = stl_utils.read_stl(path)

            blender_utils.create_and_link_mesh(objName, tris, pts)

        return {'FINISHED'}

class ExportSTL(bpy.types.Operator, ExportHelper):
    '''
    Save STL triangle mesh data from the active object
    Each mesh object kept separated as solid sections
    '''
    bl_idname = "export_named_mesh.stl"
    bl_label = "Export STL, optionally with separate solids"

    filename_ext = ".stl"

    ascii = BoolProperty(
            name="Ascii",
            description="Export to ASCII",
            default=True)

    ascii_solids = BoolProperty(
            name="Multi solids (ASCII only)",
            description="Multi solids. No effect if not ASCII.",
            default=True)

    apply_modifiers = BoolProperty(
            name="Apply Modifiers",
            description="Apply the modifiers before saving",
            default=True)

    def execute(self, context):
        from . import stl_utils
        from . import blender_utils
        import itertools

        if self.ascii and self.ascii_solids:
            fh = open(self.filepath,'w')
            for ob in context.scene.objects:
                if ob.type == "MESH":
                    faces = blender_utils.faces_from_mesh(ob, self.apply_modifiers)
                    stl_utils.append_stl_solid( fh, ob.name, faces)
                    

        else:
            faces = itertools.chain.from_iterable(
                    blender_utils.faces_from_mesh(ob, self.apply_modifiers)
                    for ob in context.scene.objects if ob.type == "MESH")
            stl_utils.write_stl(self.filepath, faces, self.ascii)


        return {'FINISHED'}


def menu_import(self, context):
    self.layout.operator(ImportSTL.bl_idname,
                         text="Stl (.stl)").filepath = "*.stl"


def menu_export(self, context):
    default_path = os.path.splitext(bpy.data.filepath)[0] + ".stl"
    self.layout.operator(ExportSTL.bl_idname,
                         text="Stl solids (.stl)").filepath = default_path


def register():
    bpy.utils.register_module(__name__)

    bpy.types.INFO_MT_file_import.append(menu_import)
    bpy.types.INFO_MT_file_export.append(menu_export)


def unregister():
    bpy.utils.unregister_module(__name__)

    bpy.types.INFO_MT_file_import.remove(menu_import)
    bpy.types.INFO_MT_file_export.remove(menu_export)


if __name__ == "__main__":
    register()
