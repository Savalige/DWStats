from cv2 import readOpticalFlow
import pandas as pd
from pathlib import Path
import json

stats = []
objects = []
crafting = []
stats = []
repair = []
transform = []
meshRenderer = []
meshFilter = []
spriteCollection = []
spriteAnimation = []
animationData = []
sounds = []
movementVariables = []
tagPenalties = []
sm_sub_ite = []
dropTable = []
char_stats = []
radius = []
selectability_n_highlight = []
inventory = []
activeEffects = []
playerRecognition = []
manualListener = []
rigidbody = []
capsuleCollider = []
boxCollider = []
meshCollider = []
sphereCollider = []
biom = []
biomPresets = []
locationPresets = []
mustSpawnLocations = []

def getID(holder):
    temp = []
    n = p.name.find(".assets-")
    n2 = p.name.find('-', n+len(".assets-"))
    temp.append(p.name[n+len(".assets-"):n2])
    i = txt.find("m_PathID = ",txt.find("m_GameObject"))
    i2 = txt.find('\n', i+len("m_PathID = "))
    temp.append(txt[i+len("m_PathID = "):i2].replace('"',''))
    holder.append(temp)

def getTexture(holder, text):
    temp = []
    n = txt.find("m_PathID = ",txt.find(text))
    n2 = txt.find('\n', n+len("m_PathID = "))
    temp.append(txt[n+len("m_PathID = "):n2])
    i = txt.find("m_PathID = ",txt.find("m_GameObject"))
    i2 = txt.find('\n', i+len("m_PathID = "))
    temp.append(txt[i+len("m_PathID = "):i2].replace('"',''))
    holder.append(temp)

def getPresets(holder, text, obj):
    s = txt.find("int size = ", txt.find(text))
    s2 = txt.find('\n', s+len("int size = "))
    size = int(txt[s+len("int size = "):s2])
    n2 = txt.find(text) + len(text)
    for i in range(size):
        temp = []
        n = txt.find("m_PathID = ",n2)
        n2 = txt.find('\n', n+len("m_PathID = "))
        temp.append(txt[n+len("m_PathID = "):n2].replace('"',''))
        temp.append(obj)
        holder.append(temp)
    
    


removeList = []
print("STARTING SEARCH")
count = 0
for p in Path('.').glob('ID_SEARCH/*.txt'):
    #GAMEOBJECT
    txt = p.read_text(encoding="UTF-8",errors="ignore")

    if (txt.find("GameObject Base") != -1):
        temp = []
        i = txt.find('m_Name = "')
        i2 = txt.find('\n', i+len('m_Name = "'))
        temp.append(txt[i+len('m_Name = "'):i2].replace('"',''))
        n = p.name.find(".assets-")
        n2 = p.name.find('-', n+len(".assets-"))
        temp.append(p.name[n+len(".assets-"):n2])
        i = txt.find("m_PathID = ")
        while(i != -1):
            i2 = txt.find('\n', i+len("m_PathID = "))
            temp.append(txt[i+len("m_PathID = "):i2].replace('"',''))
            i = txt.find("m_PathID = ",i2)
        objects.append(temp)
    #SCRIPTS
    elif (txt.find("MonoBehaviour Base") != -1):
        temp = []
        #STATS
        if (txt.find("isAmmo") != -1):
            getID(stats)
        #CRAFTING
        elif (txt.find("CraftingRequirement requirements") != -1 and txt.find("craftTime = ") != -1):
            getID(crafting)
        #REPAIR
        elif (txt.find("CraftingRequirement requirements") != -1 and txt.find("craftTime = ") == -1):
            getID(repair)
        elif (txt.find("tk2dSpriteCollectionData> collection") != -1):
            getTexture(spriteCollection, "tk2dSpriteCollectionData> collection")
        elif (txt.find("tk2dSpriteAnimation> library") != -1):
            getTexture(spriteAnimation, "tk2dSpriteAnimation> library")
        elif (txt.find(" idleSoundMinInterval = ") != -1):
            getID(sounds)
        elif (txt.find("UInt8 canSearch = ") != -1):
            getID(movementVariables)
        elif (txt.find("vector tagPenalties") != -1):
            getID(tagPenalties)
        elif (txt.find("float bezierTangentLength = ") != -1):
            getID(sm_sub_ite)
        elif (txt.find("InventoryRandomPreset> data") != -1):
            getID(dropTable)
        elif (txt.find("float maxHealth = ") != -1 and txt.find("float maxStamina = ") != -1):
            getID(char_stats)
        elif (txt.find("float radius = ") != -1):
            getID(radius)
        elif (txt.find("cannotBeSelectedByIdleController = ") != -1):
            getID(selectability_n_highlight)
        elif (txt.find("int invType = ") != -1):
            getID(inventory)
        elif (txt.find("vector activeEffects") != -1):
            getID(activeEffects)
        elif (txt.find("inSightOfPLayerEveryFrameCheck = ") != -1):
            getID(playerRecognition)
        elif (txt.find("isManualListener = ") != -1):
            getID(manualListener)
        elif (txt.find("vector biomePresets") != -1 and txt.find("vector locationPresets") != -1):
            getID(biom)
            getPresets(biomPresets, "vector biomePresets", biom[len(biom)-1][1])
            getPresets(locationPresets, "vector locationPresets", biom[len(biom)-1][1])
            getPresets(mustSpawnLocations, "vector mustSpawnLocations", biom[len(biom)-1][1])
        
    #TRANSFORM
    elif (txt.find("Transform Base") != -1):
        getID(transform)
    #MESHRENDERER
    elif (txt.find("MeshRenderer Base") != -1):
        getID(meshRenderer)
    elif (txt.find("MeshFilter Base") != -1):
        getID(meshFilter)
    elif (txt.find("Rigidbody Base") != -1):
        getID(rigidbody)
    elif (txt.find("CapsuleCollider Base") != -1):
        getID(capsuleCollider)
    elif (txt.find("BoxCollider Base") != -1):
        getID(boxCollider)
    elif (txt.find("MeshCollider Base") != -1):
        getID(meshCollider)
    elif (txt.find("SphereCollider Base") != -1):
        getID(sphereCollider)
    else:
        removeList.append(p.name)
    count = count + 1
    if count % 1000 == 0:
        print("DONE:" + str(count))
print("DONE")
print(f"Found {len(objects)} objects. Searched {count} files")


holder = [stats, crafting, repair, transform, inventory, dropTable, char_stats, meshRenderer, meshFilter, #9
spriteCollection, spriteAnimation, sounds, movementVariables, tagPenalties, sm_sub_ite, radius, #7
selectability_n_highlight, activeEffects, playerRecognition, manualListener, rigidbody, capsuleCollider, #6
boxCollider, meshCollider, sphereCollider, biom, biomPresets, locationPresets, mustSpawnLocations] #7

size = 0
for h in holder:
    size = size + len(h)
size = size + len(objects)
print(f"Total files used {size}")

obj_data = []
for h in range(len(holder) + 2):
    obj_data.append([])

col1 = "Object"
col6 = "ID"
col2 = "Object Stats"
col3 = "Crafting"
col4 = "Repair"
col5 = "Transform"
col7 = "Inventory"
col8 = "Drop Table"
col9 = "Character Stats"
col10 = "Mesh Renderer"
col11 = "Mesh Filter"
col12 = "Sprite Collection"
col13 = "Sprite Animation"
col14 = "Sounds"
col22 = "Movement Variables"
col15 = "Tag Penalties"
col16 = "Smooth subdivision iteration"
col17 = "Radius"
col18 = "Selectability and Highlight"
col19 = "Active Effects"
col20 = "Player Recognition"
col21 = "Manual Listener"
col22 = "Rigidbody"
col23 = "Capsule Collider"
col24 = "Box Collider"
col25 = "Mesh Collider"
col26 = "Sphere Collider"
col27 = "Sounds"
col28 = "Biom"
col29 = "Biom Presets"
col30 = "Location Presets"
col31 = "Must Spawn Locations"

for o in objects:
    temp = []
    obj_data[0].append(o[0])
    obj_data[1].append(int(o[1]))
    found = False
    for x in range(len(holder)):
        for y in range(len(holder[x])):
            if (holder[x][y] != [] and o[1] == holder[x][y][1]):
                if (found):
                    print(f"Multiple {x + 2} found in :{o[1]}")
                    for o2 in range(len(obj_data)):
                        if (o2 != x + 2 and o2 != 0 and o2 != 1):
                            obj_data[o2].append(0)
                    obj_data[0].append(o[0])
                    obj_data[1].append(int(o[1]))
                obj_data[x+2].append(int(holder[x][y][0]))
                found = True
        if (found == False):
            obj_data[x+2].append(0)
        found = False
#print(obj_data)

#text = ""
#for r in removeList:
#    text = text + r + "\n"

#f = open('check.txt', 'w')
#f.write(text)
#f.close()

j = []

"id_id"
"id_name"
"id_object_stats" 
"id_crafting" 
"id_repair" 
"id_transform" 
"id_inventory" 
"id_drop_table" 
"id_character_stats" 
"id_mesh_renderer" 
"id_mesh_filter" 
"id_sprite_collection" 
"id_sprite_animation" 
"id_tag_penalties" 
"id_smooth_subdivision_iteration" 
"id_radius" 
"id_selectability_and_highlight" 
"id_active_effects" 
"id_player_recognition" 
"id_manual_listener" 
"id_rigidbody" 
"id_capsule_collider" 
"id_box_collider" 
"id_mesh_collider" 
"id_sphere_collider"
"id_sounds" 
"id_biom"
"id_biom_presets"
"id_location_presets"
"id_must_spawn_locations"

for o in range(len(objects)):
    j.append({
        "id_id":obj_data[1][o],
        "id_name":obj_data[0][o],
        "id_object_stats":obj_data[2][o],
        "id_crafting":obj_data[3][o],
        "id_repair":obj_data[4][o],
        "id_transform":obj_data[5][o],
        "id_inventory":obj_data[6][o],
        "id_drop_table":obj_data[7][o],
        "id_character_stats":obj_data[8][o],
        "id_mesh_renderer":obj_data[9][o],
        "id_mesh_filter":obj_data[10][o],
        "id_sprite_collection":obj_data[11][o],
        "id_sprite_animation":obj_data[12][o],
        "id_sounds":obj_data[13][o],
        "id_movement_variables":obj_data[14][o],
        "id_tag_penalties":obj_data[15][o],
        "id_smooth_subdivision_iteration":obj_data[16][o],
        "id_radius":obj_data[17][o],
        "id_selectability_and_highlight":obj_data[18][o],
        "id_active_effects":obj_data[19][o],
        "id_player_recognition":obj_data[20][o],
        "id_manual_listener":obj_data[21][o],
        "id_rigidbody":obj_data[22][o],
        "id_capsule_collider":obj_data[23][o],
        "id_box_collider":obj_data[24][o],
        "id_mesh_collider":obj_data[25][o],
        "id_sphere_collider":obj_data[26][o],
        "id_biom":obj_data[27][o],
        "id_biom_presets":obj_data[28][o],
        "id_location_presets":obj_data[29][o],
        "id_must_spawn_locations":obj_data[30][o]
    })

f = open('id_list.JSON', 'w')
f.write(json.dumps(j))
f.close()

data = pd.DataFrame({col1:obj_data[0],col6:obj_data[1],col2:obj_data[2],col3:obj_data[3],col4:obj_data[4],
col5:obj_data[5],col7:obj_data[6],col8:obj_data[7],col9:obj_data[8],col10:obj_data[9],
col11:obj_data[10],col12:obj_data[11],col13:obj_data[12],col15:obj_data[14],col16:obj_data[15],
col17:obj_data[16],col18:obj_data[17],col19:obj_data[18],col20:obj_data[19],col21:obj_data[20],
col22:obj_data[21],col23:obj_data[22],col24:obj_data[23],col25:obj_data[24],col26:obj_data[25],
col27:obj_data[26],col28:obj_data[27],col29:obj_data[28],col30:obj_data[29],col31:obj_data[30]})
data.to_excel('object_id_data.xlsx', sheet_name='Sheet 1', index=False)