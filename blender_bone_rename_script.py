import bpy
import re


obj = bpy.context.active_object

if obj and obj.type == 'ARMATURE':
    for bone in obj.data.bones:
        if re.search("right", bone.name, flags=re.IGNORECASE):
            bone.name = re.sub("right", "", bone.name, flags=re.IGNORECASE)
            bone.name += "_R"

        if re.search("left", bone.name, flags=re.IGNORECASE):
            bone.name = re.sub("left", "", bone.name, flags=re.IGNORECASE)
            bone.name += "_L"
else:
    print("Active object is not an armature.")