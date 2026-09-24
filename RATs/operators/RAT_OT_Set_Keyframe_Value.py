import bpy
from bpy.props import FloatProperty


class RAT_OT_Set_Keyframe_Value(bpy.types.Operator):
    bl_idname = "object.set_keyframe_value"
    bl_label = "Set Keyframe Value"
    bl_options = {'REGISTER', 'UNDO'}

    my_float_y : FloatProperty(
        name="Value",
        description="New value for the selected keyframes.",
#        get = active_frame_value
#        set = seleced_frames__new_value
        )

    def cpoints(self, context):
        ctrl_pts = []
        for c in context.selected_visible_fcurves:
            for k in c.keyframe_points:
                if k.select_control_point:
                    ctrl_pts.append(k)
        return ctrl_pts

    @classmethod
    def poll(cls, context):
        areas = ('DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'TIMELINE')
        if context.area.type in areas:
            return True
        else:
            return False

    def invoke(self, context, event):
        wm = context.window_manager
        # return wm.invoke_popup(self, width=100)
        return wm.invoke_props_dialog(self, width=100)
        # voir https://media.discordapp.net/attachments/456165231945842688/657525317593989120/unknown.png?width=1025&height=193

    def execute(self, context):
        sel = self.cpoints(context)

        for k in sel:
            k.co = (k.co.x, self.my_float_y)
            k.handle_left = (k.handle_left.x, self.my_float_y)
            k.handle_right = (k.handle_left.y, self.my_float_y)
        return {'FINISHED'}

    def draw(self, context):
        lay = self.layout
        lay.row().prop(self, "my_float_y")


def register():
    bpy.utils.register_class(RAT_OT_Set_Keyframe_Value)


def unregister():
    bpy.utils.unregister_class(RAT_OT_Set_Keyframe_Value)


if __name__ == "__main__":
    register()

# test call
# bpy.ops.object.simple_operator()
