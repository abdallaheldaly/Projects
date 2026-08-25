import bpy
import random
import math

# تنضيف المشهد
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

random.seed(42)


def new_collection(name):
    col = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(col)
    return col


def link_to_collection(obj, col):
    for c in obj.users_collection:
        c.objects.unlink(obj)
    col.objects.link(obj)


def make_material(name, base_color, metallic=0.0, roughness=0.5,
                   use_wood_grain=False, use_ridges=False, use_studs_pattern=False):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    nodes.clear()

    out = nodes.new("ShaderNodeOutputMaterial")
    out.location = (600, 0)

    bsdf = nodes.new("ShaderNodeBsdfPrincipled")
    bsdf.location = (300, 0)
    bsdf.inputs["Base Color"].default_value = (*base_color, 1.0)
    bsdf.inputs["Metallic"].default_value = metallic
    bsdf.inputs["Roughness"].default_value = roughness
    links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])

    tex_coord = nodes.new("ShaderNodeTexCoord")
    tex_coord.location = (-600, 0)

    mapping = nodes.new("ShaderNodeMapping")
    mapping.location = (-400, 0)
    links.new(tex_coord.outputs["Object"], mapping.inputs["Vector"])

    if use_wood_grain:
        wave = nodes.new("ShaderNodeTexWave")
        wave.location = (-150, 150)
        wave.wave_type = 'BANDS'
        wave.inputs["Scale"].default_value = 8.0
        wave.inputs["Distortion"].default_value = 4.0
        links.new(mapping.outputs["Vector"], wave.inputs["Vector"])

        ramp = nodes.new("ShaderNodeValToRGB")
        ramp.location = (100, 250)
        ramp.color_ramp.elements[0].color = (*[c * 0.6 for c in base_color], 1.0)
        ramp.color_ramp.elements[1].color = (*base_color, 1.0)
        links.new(wave.outputs["Fac"], ramp.inputs["Fac"])
        links.new(ramp.outputs["Color"], bsdf.inputs["Base Color"])

        bump = nodes.new("ShaderNodeBump")
        bump.location = (100, -150)
        bump.inputs["Strength"].default_value = 0.15
        links.new(wave.outputs["Fac"], bump.inputs["Height"])
        links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])

    elif use_ridges:
        wave = nodes.new("ShaderNodeTexWave")
        wave.location = (-150, 150)
        wave.wave_type = 'BANDS'
        wave.bands_direction = 'X'
        wave.inputs["Scale"].default_value = 20.0
        links.new(mapping.outputs["Vector"], wave.inputs["Vector"])

        bump = nodes.new("ShaderNodeBump")
        bump.location = (100, -150)
        bump.inputs["Strength"].default_value = 0.35
        links.new(wave.outputs["Fac"], bump.inputs["Height"])
        links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])

    elif use_studs_pattern:
        voro = nodes.new("ShaderNodeTexVoronoi")
        voro.location = (-150, 150)
        voro.inputs["Scale"].default_value = 6.0
        links.new(mapping.outputs["Vector"], voro.inputs["Vector"])

        bump = nodes.new("ShaderNodeBump")
        bump.location = (100, -150)
        bump.inputs["Strength"].default_value = 0.25
        links.new(voro.outputs["Distance"], bump.inputs["Height"])
        links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])

    return mat


def add_panel(name, collection, location, rotation_euler, size=(1.0, 2.2, 0.06), material=None):
    bpy.ops.mesh.primitive_cube_add(size=1, location=location)
    obj = bpy.context.active_object
    obj.name = name
    obj.scale = (size[0] / 2, size[1] / 2, size[2] / 2)
    obj.rotation_euler = rotation_euler
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

    if material:
        obj.data.materials.append(material)

    link_to_collection(obj, collection)
    return obj


def add_cylinder(name, collection, location, radius, depth, rotation_euler=(0, 0, 0), material=None):
    bpy.ops.mesh.primitive_cylinder_add(radius=radius, depth=depth, location=location)
    obj = bpy.context.active_object
    obj.name = name
    obj.rotation_euler = rotation_euler
    if material:
        obj.data.materials.append(material)
    link_to_collection(obj, collection)
    return obj


def add_torus(name, collection, location, major_radius, minor_radius, rotation_euler=(0, 0, 0), material=None):
    bpy.ops.mesh.primitive_torus_add(location=location, major_radius=major_radius, minor_radius=minor_radius)
    obj = bpy.context.active_object
    obj.name = name
    obj.rotation_euler = rotation_euler
    if material:
        obj.data.materials.append(material)
    link_to_collection(obj, collection)
    return obj


# مواد الخامات
mat_wood_dark = make_material("Mat_Wood_Dark", (0.10, 0.07, 0.05), metallic=0.0, roughness=0.55, use_wood_grain=True)
mat_wood_medium = make_material("Mat_Wood_Medium", (0.28, 0.17, 0.10), metallic=0.0, roughness=0.5, use_wood_grain=True)
mat_wood_light = make_material("Mat_Wood_Light", (0.55, 0.40, 0.27), metallic=0.0, roughness=0.45, use_wood_grain=True)
mat_metal_dark_ridged = make_material("Mat_Metal_Dark_Ridged", (0.05, 0.05, 0.06), metallic=0.85, roughness=0.35, use_ridges=True)
mat_metal_stud = make_material("Mat_Metal_Stud", (0.35, 0.34, 0.33), metallic=0.9, roughness=0.3, use_studs_pattern=True)
mat_frame_black = make_material("Mat_Frame_Black", (0.02, 0.02, 0.02), metallic=0.6, roughness=0.4)
mat_handle = make_material("Mat_Handle_Brass", (0.6, 0.45, 0.2), metallic=1.0, roughness=0.2)


# مجموعة الشرائح المتراصة
fan_col = new_collection("Door_Slabs_Fan")

slab_materials = [mat_wood_medium, mat_wood_dark, mat_metal_dark_ridged, mat_wood_light, mat_metal_stud]
slab_names = [
    "Slab_01_Wood_Medium",
    "Slab_02_Wood_Dark",
    "Slab_03_Metal_Ridged",
    "Slab_04_Wood_Light",
    "Slab_05_Metal_Stud",
]

n = len(slab_materials)
spacing_x = 0.28
base_angle_deg = -18

for i in range(n):
    x = i * spacing_x
    y = -i * 0.05
    z = 1.1
    angle = math.radians(base_angle_deg + i * 2)
    add_panel(
        name=slab_names[i],
        collection=fan_col,
        location=(x, y, z),
        rotation_euler=(0, angle, 0),
        size=(0.9, 2.1, 0.045),
        material=slab_materials[i],
    )


# الباب النهائي المجمّع
final_col = new_collection("Final_Door")

door_x_offset = 4.0

add_panel(
    name="Frame_Outer",
    collection=final_col,
    location=(door_x_offset, 0, 1.15),
    rotation_euler=(0, 0, 0),
    size=(1.35, 2.5, 0.10),
    material=mat_frame_black,
)

add_panel(
    name="Main_Panel_Dark_Wood",
    collection=final_col,
    location=(door_x_offset - 0.15, 0, 1.15),
    rotation_euler=(0, 0, 0),
    size=(1.05, 2.35, 0.06),
    material=mat_wood_dark,
)

add_panel(
    name="Vertical_Wood_Strip",
    collection=final_col,
    location=(door_x_offset + 0.28, 0, 1.15),
    rotation_euler=(0, 0, 0),
    size=(0.14, 2.35, 0.075),
    material=mat_wood_medium,
)

add_panel(
    name="Metal_Ridged_Accent",
    collection=final_col,
    location=(door_x_offset - 0.42, 0, 1.15),
    rotation_euler=(0, 0, 0),
    size=(0.08, 2.35, 0.075),
    material=mat_metal_dark_ridged,
)

add_torus(
    name="Handle_Ring_Upper",
    collection=final_col,
    location=(door_x_offset + 0.28, -0.045, 1.75),
    major_radius=0.09,
    minor_radius=0.018,
    rotation_euler=(math.radians(90), 0, 0),
    material=mat_handle,
)

add_torus(
    name="Handle_Ring_Lower",
    collection=final_col,
    location=(door_x_offset + 0.28, -0.045, 0.55),
    major_radius=0.09,
    minor_radius=0.018,
    rotation_euler=(math.radians(90), 0, 0),
    material=mat_handle,
)

stud_positions_z = [0.35, 0.85, 1.45, 1.95]
for idx, sz in enumerate(stud_positions_z):
    add_cylinder(
        name=f"Stud_{idx+1:02d}",
        collection=final_col,
        location=(door_x_offset - 0.15, -0.035, sz),
        radius=0.02,
        depth=0.02,
        rotation_euler=(math.radians(90), 0, 0),
        material=mat_metal_stud,
    )


# إضاءة وكاميرا
bpy.ops.object.light_add(type='AREA', location=(door_x_offset, -3.5, 3.0))
key_light = bpy.context.active_object
key_light.name = "Light_Key"
key_light.data.energy = 800
key_light.data.size = 2.5
key_light.rotation_euler = (math.radians(60), 0, 0)

bpy.ops.object.light_add(type='AREA', location=(-0.5, -3.0, 2.5))
fill_light = bpy.context.active_object
fill_light.name = "Light_Fill"
fill_light.data.energy = 300
fill_light.data.size = 2.0
fill_light.rotation_euler = (math.radians(65), 0, 0)

bpy.ops.object.camera_add(location=(2.0, -6.5, 1.6), rotation=(math.radians(90), 0, 0))
cam = bpy.context.active_object
cam.name = "Camera_Main"
bpy.context.scene.camera = cam

print("== ULTRA Doors scene built successfully ==")