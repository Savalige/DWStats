from cv2 import readOpticalFlow
from pathlib import Path
import json

animations = []
names = []

def getSpriteOrder(pos) -> list:
    temp = []
    s = "string name = "
    n = txt.find(s, pos)
    n2 = txt.find('\n', n+len(s))
    temp.append(txt[n+len(s)+1:n2-1])

    tempFrameData = []
    i = txt.find("tk2dSpriteAnimationFrame data",pos)
    while i != -1:
        tempD = {}
        s = "SInt64 m_PathID = "
        n = txt.find(s, i)
        n2 = txt.find("\n", n+len(s))
        tempD["frame_id"] = txt[n+len(s):n2]
        s = "int spriteId = "
        n = txt.find(s, i)
        n2 = txt.find("\n", n+len(s))
        tempD["frame_sprite_id"] = txt[n+len(s):n2]
        i = txt.find("tk2dSpriteAnimationFrame data",n)
        tempFrameData.append(tempD)
    temp.append(tempFrameData)
    return temp

count = 0
def getAnimations() -> list:
    temp = []
    n = p.name.find(".assets-")
    n2 = p.name.find('-', n+len(".assets-"))
    temp.append(p.name[n+len(".assets-"):n2])
    names.append(p.name[n+len(".assets-"):n2])
    s = "tk2dSpriteAnimationFrame data"
    i = txt.find(s)
    tempAnimation = []
    while i != -1:
        tempAnimation.append(getSpriteOrder(i))
        i = txt.find(s,i+len(s))
    temp.append(tempAnimation)
    j = []
    for f in temp[1]:
        j.append({
            "ani_id": temp[0],
            "ani_name": f[0],
            "ani_frame_data": f[1],
        })
    f = open("Animations/"+str(temp[0])+'.JSON', 'w')
    f.write(json.dumps(j))
    f.close()

    return temp

print("STARTING SEARCH")
for p in Path('.').glob('SPRITE/*.txt'):
    #GAMEOBJECT
    txt = p.read_text(encoding="UTF-8",errors="ignore")
    #print(p.name)
    if (txt.find("tk2dSpriteAnimationClip data") != -1):
        animations.append(getAnimations())
    count = count + 1
    if count % 10 == 0:
        print("DONE:" + str(count))
print("DONE")
print(f"Found {len(animations)} objects")

f = open('animation_names.JSON', 'w')
f.write(json.dumps(names))
f.close()

#j = []
#amount = 0
#for e in animations:
#    for f in e[1]:
#        j.append({
#            "ani_id": e[0],
#            "ani_name": f[0],
#            "ani_frame_data": f[1],
#        })
#        amount = amount + len(f[1])

#print(amount)

#f = open('animation_list.JSON', 'w')
#f.write(json.dumps(j))
#f.close()