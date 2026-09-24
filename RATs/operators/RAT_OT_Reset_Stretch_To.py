# SPDX-License-Identifier: GPL-3.0-or-later

import bpy

class RAT_OT_Reset_Stretch_To(bpy.types.Operator):
    bl_idname = "view3d.reset_stretch_to"
    bl_label = "Reset: Stretch To"
    bl_description = "Resets any \"Stretch To\" constraints"
    bl_options = {"UNDO"}

	def execute(self,context):
		for b in bpy.context.selected_pose_bones:
			for c in b.constraints:
				if c.name == "Stretch To":
					c.rest_length = 0
		return{'FINISHED'}