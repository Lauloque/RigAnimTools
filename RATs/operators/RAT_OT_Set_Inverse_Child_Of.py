# SPDX-License-Identifier: GPL-3.0-or-later

import bpy

class RAT_OT_Set_Inverse_Child_Of(bpy.types.Operator):
    bl_idname = "view3d.set_inverse_child_of"
    bl_label = "Set Inverse: Child Of"
    bl_description = "Sets the inverse of any \"Child Of\" constraints"
    bl_options = {"UNDO"}

    def execute(self,context):
        obj = context.active_object
        armature = obj.data

        # Take a copy of current collections and their vis
        collections = list(armature.collections_all)
        org_visibility = [collection.is_visible for collection in collections]

        # Show all layers
        for collection in collections:
            collection.is_visible = True

        for bone in obj.pose.bones:
            for constraint in bone.constraints:
                if constraint.type == "CHILD_OF":
                    obj.data.bones.active = bone.bone

                    bpy.ops.constraint.childof_set_inverse(
                        constraint=constraint.name,
                        owner="BONE",
                    )

        # Reset back to orginal layer state
        for collection, visible in zip(collections, org_visibility):
            collection.is_visible = visible

        return {"FINISHED"}