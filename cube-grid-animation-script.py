import bpy


for obj in bpy.data.objects:
    bpy.data.objects.remove(obj)
    

def create_cube_column():

    bpy.ops.mesh.primitive_cube_add(
    size=1, 
    location=(0, 0, 0)
    )

    for a in range(9):
        bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={

            "linked":False, 
            "mode":'TRANSLATION'

            }, 

        TRANSFORM_OT_translate={

            "value":(-1, -0, -0), 
            "orient_axis_ortho":'X', 
            "orient_type":'GLOBAL', 
            "orient_matrix":(
            
                (1, 0, 0), 
                (0, 1, 0), 
                (0, 0, 1)
                
            ), 
            
            "orient_matrix_type":'GLOBAL', 
            "constraint_axis":(True, False, False), 

            }
        )


def create_cube_row():

    bpy.ops.object.select_by_type(extend=False, type='MESH')
    
    for b in range(9):
        bpy.ops.object.duplicate_move(
        
            OBJECT_OT_duplicate={
            
                "linked":False, 
                "mode":'TRANSLATION'
            
            }, 
            
            TRANSFORM_OT_translate={
                
                "value":(0, 1, 0), 
                "orient_axis_ortho":'X', 
                "orient_type":'GLOBAL', 
                "orient_matrix":(
                    
                    (1, 0, 0), 
                    (0, 1, 0), 
                    (0, 0, 1)
                    
                ), 
                
                "orient_matrix_type":'GLOBAL', 
                "constraint_axis":(False, True, False), 

                
            }
                
        )


def create_cube_grid():

    create_cube_column()

    create_cube_row()

create_cube_grid()


bpy.ops.object.select_by_type(extend=False, type='MESH')
bpy.ops.collection.create(name='Cubes')

    
cubes = bpy.data.collections["Cubes"].objects
offset = 0

for c in cubes:
    c.scale = [0, 0, 0]
    c.keyframe_insert(data_path = "scale", frame = 1 + offset)
    c.scale = [1, 1, 5]
    c.keyframe_insert(data_path = "scale", frame = 50 + offset)
    c.scale = [1, 1, .5]
    c.keyframe_insert(data_path = "scale", frame = 70 + offset)
    c.scale = [1, 1, 1]
    c.keyframe_insert(data_path = "scale", frame = 80 + offset)
    offset += 1
    