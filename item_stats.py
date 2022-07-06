import pandas as pd
from pathlib import Path

str_list = [' type = "','int damage = ', 'int damageDurabilityDrain = ',
'int barricadeDamage = ','int barricadeDamageDurabilityDrain = ',
'specialDamage = ','specialDamageDurabilityDrain =','int specialBarricadeDamage = ',
'int specialBarricadeDamageDurabilityDrain = ','float maxDurability = ',
'float durabilityDrain = ','float recoilAmount = ','UInt8 hasAmmo = ','int clipSize = ',
'int projectileAmount = ','int burstAmount = ','float fireRate = ','float aimFOV = ',
'string ammoType = ','float handling = ','float zoom = ','float staminaAttackDrain = ',
'float staminaSpecialAttackDrain = ','UInt8 isMelee = ','int canAttackFrame = ',
'int weakAttackAimFrame = ','weakAttackStartFrame = ','int value = ',

'maxAmount = ','stackable = ','isAmmo = ','isArmor = ','armorValue = ',
'addsPoisonImmunity =','useable = ','useableText = ','useableIcon = ',]
stats = []

for s in range(len(str_list)):
    stats.append([])

for p in Path('.').glob('STATS/*.txt'):
    if (p.read_text().find("isAmmo") != -1):
        for s in range(len(str_list)):
            i = p.read_text().find(str_list[s], 3)
            i2 = p.read_text().find('\n', i+len(str_list[s]))
            stats[s].append(p.read_text()[i+len(str_list[s]):i2].replace('"',''))
    else:
        print(f"{p.name}: NOT ITEM")
print("DONE")
#print(stats)

col1 = "name"
col2 = "damage"
col3 = "damageDurabilityDrain"
col4 = "barricadeDamage"
col5 = "barricadeDamageDurabilityDrain"
col6 = "specialDamage"
col7 = "specialDamageDurabilityDrain"
col8 = "specialBarricadeDamage"
col9 = "specialBarricadeDamageDurabilityDrain"
col10 = "maxDurability"
col12 = "recoilAmount"
col13 = "hasAmmo"
col14 = "clipSize"
col15 = "projectileAmount"
col17 = "fireRate"
col18 = "aimFOV"
col19 = "ammoType"
col20 = "handling"
col21 = "zoom"
col22 = "staminaAttackDrain"
col23 = "staminaSpecialAttackDrain"
col24 = "isMelee"
col25 = "canAttackFrame"
col26 = "weakAttackAimFrame"
col27 = "weakAttackStartFrame"
col28 = "value"
col29 = "maxAmount"
col30 = "stackable"
col31 = "isAmmo"
col32 = "isArmor"
col33 = "armorValue"
col34 = "addsPoisonImmunity"
col35 = "useable"
col36 = "useableText"
col37 = "useableIcon"



data = pd.DataFrame({col1:stats[0],col2:stats[1],col3:stats[2],col4:stats[3],col5:stats[4],
col6:stats[5],col7:stats[6],col8:stats[7],col9:stats[8],col10:stats[9],col12:stats[11],
col13:stats[12],col4:stats[13],col15:stats[14],col17:stats[16],col18:stats[17],
col19:stats[18],col20:stats[19],col21:stats[20],col22:stats[21],col23:stats[22],
col24:stats[23],col25:stats[24],col26:stats[25],col27:stats[26],col28:stats[27],
col29:stats[28],col30:stats[29],col31:stats[30],col32:stats[31],col33:stats[32],
col34:stats[33],col35:stats[34],col36:stats[35],col37:stats[36]})
data.to_excel('item_stat_data.xlsx', sheet_name='Sheet 1', index=False)