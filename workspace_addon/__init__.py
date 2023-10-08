# "Addon to make make life easier for toyxyz's 
# controlnet blend file. You can get it free here 
# https://toyxyz.gumroad.com/l/ciojz but always 
# great to support great work. 
# 
# So, if you can send him some monies :) "
# This addon by Kewk
#
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
#  along with this program; if not, see <http://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####


bl_info = {
    "name": "View Layer List",
    "author": "Kewk",
    "version": (1, 0),
    "blender": (3, 6, 1),
    "location": "Outliner > Tool > View Layer List",
	"description": "Quality of life addon for toyxyz's controlnet blend file. You can get it free here https://toyxyz.gumroad.com/l/ciojz but always great to support great work. Kick him down some monies if you can :) ",
    "category": "Tool",
}

import bpy

class ViewLayerListPanel(bpy.types.Panel):
    bl_label = "View Layer List"
    bl_idname = "OBJECT_PT_view_layer_list"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene

        for vl in scene.view_layers:
            row = layout.row()
            row.label(text=vl.name)
            row.prop(vl, "use", text="")

def register():
    bpy.utils.register_class(ViewLayerListPanel)

def unregister():
    bpy.utils.unregister_class(ViewLayerListPanel)

if __name__ == "__main__":
    register()
