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

class RAT_OT_Reset_Stretch_To(bpy.types.Operator):
	bl_idname = "view3d.reset_stretch_to"
	bl_label = "Reset: Stretch To"
	bl_description = "Resets any \"Stretch To\" constraints"

	def execute(self,context):
		for b in bpy.context.selected_pose_bones:
			for c in b.constraints:
				if c.name == "Stretch To":
					c.rest_length = 0
		return{'FINISHED'}