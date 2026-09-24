# SPDX-License-Identifier: GPL-3.0-or-later

import bpy

class RAT_OT_Set_Inverse_Child_Of(bpy.types.Operator):
    bl_idname = "view3d.set_inverse_child_of"
    bl_label = "Set Inverse: Child Of"
    bl_description = "Sets the inverse of any \"Child Of\" constraints"
    bl_options = {"UNDO"}

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