# bpy.context.object.co[1] = 2.3

#bpy.ops.transform.translate(value=(0, 0.795772, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)


# ***** BEGIN GPL LICENSE BLOCK *****
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ***** END GPL LICENCE BLOCK *****

# not standalone
bl_info = {
        "name": "RAT Set keyframe value",
        "description": "A regroupment of little tools to automate redundant and boring rigging tasks (isn't that what programs are made for in the first place ?).",
        "author": "-L0Lock-",
        "version": (0, 2),
        "blender": (2, 80, 0),
        "location": "Pose Mode > Sidebar > RiggingTools tab",
        "warning": "made by a python noob",
        "wiki_url": "https://github.com/L0Lock/RigAnimTools",
        "tracker_url": "https://github.com/L0Lock/RigAnimTools/issues",
        "support": "COMMUNITY",
        "category": "Rigging"
        }
# /not standalone

import bpy

class RAT_OT_Set_Keyframe_Value(bpy.types.Operator):
    bl_idname = "set_keyframe_value"
    bl_label = "Set keyframe value"
    bl_description = "Sets the selected keyframes' value."

    def execute(self,context):
        for b in bpy.context.selected_objects:
            b.Keyframe.co[1] = 6
        return{'FINISHED'}
    
# not standalone
    
classes = (RAT_OT_Set_Keyframe_Value)

register, unregister = bpy.utils.register_classes_factory(classes)

# /not standalone