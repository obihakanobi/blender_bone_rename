bl_info = {
    "name": "Auto Rename Bones (L/R)",
    "author": "Hakan Yurt",
    "version": (1, 1),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > Tool Tab",
    "description": "Rename bones using L/R or remove custom text",
    "category": "Rigging",
}

import bpy
import re


# -------------------------
# Properties
# -------------------------
class BoneRenameProperties(bpy.types.PropertyGroup):
    remove_text: bpy.props.StringProperty(
        name="Text to Remove",
        description="Text that will be removed from bone names",
        default=""
    )


# -------------------------
# Operator: L/R Rename
# -------------------------
class OBJECT_OT_auto_rename_bones(bpy.types.Operator):
    bl_idname = "object.auto_rename_bones"
    bl_label = "Auto Rename L/R"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object

        if not obj or obj.type != 'ARMATURE':
            self.report({'WARNING'}, "Active object is not an armature.")
            return {'CANCELLED'}

        for bone in obj.data.bones:
            if re.search("right", bone.name, flags=re.IGNORECASE):
                bone.name = re.sub("right", "", bone.name, flags=re.IGNORECASE)
                bone.name = bone.name.strip() + "_R"

            if re.search("left", bone.name, flags=re.IGNORECASE):
                bone.name = re.sub("left", "", bone.name, flags=re.IGNORECASE)
                bone.name = bone.name.strip() + "_L"

        return {'FINISHED'}


# -------------------------
# Operator: Remove Custom Text
# -------------------------
class OBJECT_OT_remove_custom_text(bpy.types.Operator):
    bl_idname = "object.remove_custom_text"
    bl_label = "Remove Text from Bones"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object
        props = context.scene.bone_rename_props

        if not obj or obj.type != 'ARMATURE':
            self.report({'WARNING'}, "Active object is not an armature.")
            return {'CANCELLED'}

        if not props.remove_text:
            self.report({'WARNING'}, "No text specified.")
            return {'CANCELLED'}

        pattern = re.compile(re.escape(props.remove_text), re.IGNORECASE)

        for bone in obj.data.bones:
            new_name = re.sub(pattern, "", bone.name)
            bone.name = new_name.strip()

        return {'FINISHED'}


# -------------------------
# UI Panel
# -------------------------
class VIEW3D_PT_auto_rename_bones_panel(bpy.types.Panel):
    bl_label = "Auto Bone Renamer"
    bl_idname = "VIEW3D_PT_auto_rename_bones_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tool"

    def draw(self, context):
        layout = self.layout
        props = context.scene.bone_rename_props

        layout.label(text="Left / Right Rename")
        layout.operator("object.auto_rename_bones", icon='ARMATURE_DATA')

        layout.separator()

        layout.label(text="Custom Text Removal")
        layout.prop(props, "remove_text")
        layout.operator("object.remove_custom_text", icon='X')


# -------------------------
# Register
# -------------------------
classes = (
    BoneRenameProperties,
    OBJECT_OT_auto_rename_bones,
    OBJECT_OT_remove_custom_text,
    VIEW3D_PT_auto_rename_bones_panel,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.bone_rename_props = bpy.props.PointerProperty(type=BoneRenameProperties)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.bone_rename_props


if __name__ == "__main__":
    register()