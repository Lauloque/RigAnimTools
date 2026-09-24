# SPDX-License-Identifier: GPL-3.0-or-later

import bpy

_classes = None

def register():
    """Register"""
    # --- Always register zone ---
    # only things that are safe in background mode AND still useful there
    # e.g. properties or operators that make sense to run from CLI
    # add your Always-zone registration here

    # ---- nothing in this addon should be used in cli afaict

    global _classes

    # --- GUI-mode-only register zone ---
    if not bpy.app.background:
        # Move only the internal imports used by this GUI-mode-only zone
        # e.g. from . import ui, panels, gpu_stuff

        from .operators.RAT_OT_Reset_Stretch_To import RAT_OT_Reset_Stretch_To
        from .operators.RAT_OT_Set_Inverse_Child_Of import RAT_OT_Set_Inverse_Child_Of
        from .operators.RAT_OT_Clear_Inverse_Child_Of import RAT_OT_Clear_Inverse_Child_Of
        from .ui import VIEW3D_PT_rat_main
        
        from .preferences import AddonPrefs

        _classes = (
            RAT_OT_Reset_Stretch_To,
            RAT_OT_Set_Inverse_Child_Of,
            RAT_OT_Clear_Inverse_Child_Of,
            VIEW3D_PT_rat_main,
            AddonPrefs,
        )

        # Add your GUI-mode-only registration here
        for cls in _classes:
            try:
                bpy.utils.register_class(cls)
            except Exception as e:
                print(f"[{__package__}] Error registering class {cls.__name__}: {e}")
        pass
    else:
        print(f"[{__package__}] skipping GUI-mode-only registration: Blender is in background mode.")



def unregister():
    """Unregister"""

    global _classes
    
    # --- GUI-mode-only unregister zone ---
    if not bpy.app.background and _classes is not None:
        # add your GUI-mode-only unregister here
        for cls in reversed(_classes):
            try:
                bpy.utils.unregister_class(cls)
            except Exception as e:
                print(f"[{__package__}] Error unregistering class {cls.__name__}: {e}")
        del bpy.types.Scene.CRM_Properties
        pass

    # --- Always unregister zone ---
    # Add your Always-zone unregister here