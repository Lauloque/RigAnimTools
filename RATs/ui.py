# SPDX-License-Identifier: GPL-3.0-only

import bpy
from bpy.types import Panel
from bpy.types import Context
from .bl_logger import logger

from .operators.RAT_OT_Reset_Stretch_To import RAT_OT_Reset_Stretch_To
from .operators.RAT_OT_Set_Inverse_Child_Of import RAT_OT_Set_Inverse_Child_Of
from .operators.RAT_OT_Clear_Inverse_Child_Of import RAT_OT_Clear_Inverse_Child_Of


class VIEW3D_PT_rat_main(Panel):
    bl_idname = "POSE_PT_rat_main"
    bl_label = "RigAnimTools"
    bl_category = "Anim"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_context = "posemode"


    def draw(self, context):
        layout = self.layout

        layout.operator("view3d.reset_stretch_to")
        layout.operator("view3d.set_inverse_child_of")
        layout.operator("view3d.clear_inverse_child_of")

panels = [
    VIEW3D_PT_rat_main
]

def update_panel(self, context: Context) -> None:
    """Update tab in which to place the panel"""
    try:
        # Ensure 'panels' is defined or imported
        # from .ui import panels  # Import panels from the appropriate module

        for panel in panels:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)

        for panel in panels:
            addon = context.preferences.addons[__package__]
            panel.bl_category = addon.preferences.category
            bpy.utils.register_class(panel)

    except Exception as e:
        message = "Updating Panel locations has failed"
        logger.error(
            "\n[{}]\n{}\n\nError:\n{}".format(__package__, message, e)
        )

classes = (
        RAT_OT_Reset_Stretch_To,
        RAT_OT_Set_Inverse_Child_Of,
        RAT_OT_Clear_Inverse_Child_Of,
        VIEW3D_PT_rat_main
        )

register, unregister = bpy.utils.register_classes_factory(classes)