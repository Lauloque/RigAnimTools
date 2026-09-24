# SPDX-License-Identifier: GPL-3.0-or-later

import bpy

class RAT_OT_Set_Keyframe_Value(bpy.types.Operator):
    bl_idname = "set_keyframe_value"
    bl_label = "Set keyframe value"
    bl_description = "Sets the selected keyframes' value."
    bl_options = {"UNDO"}

    def execute(self,context):
        for b in bpy.context.selected_objects:
            b.Keyframe.co[1] = 6
        return{'FINISHED'}
    
# not standalone
    
classes = (RAT_OT_Set_Keyframe_Value)

register, unregister = bpy.utils.register_classes_factory(classes)

# /not standalone