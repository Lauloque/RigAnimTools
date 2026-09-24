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

import bpy

class RAT_OT_Set_Inverse_Child_Of(bpy.types.Operator):
	bl_idname = "view3d.set_inverse_child_of"
	bl_label = "Set Inverse: Child Of"
	bl_description = "Sets the inverse of any \"Child Of\" constraints"

	def execute(self,context):
		ob = bpy.context.active_object

		# Take a copy of current layers
		org_layers = ob.data.layers[:]

		# Show all layers
		for i in range(len(org_layers)):
			ob.data.layers[i] = True

		for b in ob.pose.bones:
			for c in b.constraints:
				if c.type == "CHILD_OF":
		 			context_py = bpy.context.copy()
		 			context_py["constraint"] = c
		 			ob.data.bones.active = b.bone
		 			bpy.ops.constraint.childof_set_inverse(context_py,
		 			constraint="Child Of", owner='BONE')

		# Reset back to orginal layer state
		for i in range(len(org_layers)):
			ob.data.layers[i] = org_layers[i]
		return{'FINISHED'}