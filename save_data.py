import GenshinInfoCrawer
import os
import json
import sys


#数据的保存目录
path_name = "datas"


data_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], path_name)

def write_json(dic, filename, write_path):
    jsObj = json.dumps(dic, ensure_ascii=False,sort_keys=False, indent=4)
    filename=filename + ".json"
    if not os.path.exists(write_path):
        os.makedirs(write_path)
    file = os.path.join(write_path, filename)
    fileObject = open(file, 'w+', encoding='utf-8')  
    fileObject.write(jsObj)  
    fileObject.close()

if os.path.exists(data_path):
    inputs = input("检测到已存在数据文件夹！是否更新？(Y/n)：")
    if inputs.lower() == "y" or inputs.lower() == "yes":
        data = GenshinInfoCrawer.GenshinInfoCrawer()
        weapon_info=data.get_weapon_info()
        characters=data.get_character_info()
        weapons = {**weapon_info["单手剑"], **weapon_info["双手剑"]}
        weapons = {**weapons, **weapon_info["长柄武器"]}
        weapons = {**weapons, **weapon_info["法器"]}
        for i in range(len(list(weapons.keys()))):
            name = list(weapons.keys())[i]
            weapon_data = weapons[name]
            write_path = os.path.join(data_path, "weapons", name)
            write_json(weapon_data, 'zh_CN', write_path)
        for i in range(len(list(characters.keys()))):
            name = list(characters.keys())[i]
            character_data = characters[name]
            if name == "旅行者（空/荧）":
                name = "旅行者"
                write_path = os.path.join(data_path, "characters", name)
                write_json(character_data, 'zh_CN', write_path)
            else:
                write_path = os.path.join(data_path, "characters", name)
                write_json(character_data, 'zh_CN', write_path)
    elif inputs.lower() == "n" or inputs.lower() == "no":
        exit()
    else:
        print("输入无效!")
else:
    data = GenshinInfoCrawer.GenshinInfoCrawer()
    weapon_info=data.get_weapon_info()
    characters=data.get_character_info()
    weapons = {**weapon_info["单手剑"], **weapon_info["双手剑"]}
    weapons = {**weapons, **weapon_info["长柄武器"]}
    weapons = {**weapons, **weapon_info["法器"]}
    weapons = {**weapons, **weapon_info["弓"]}
    for i in range(len(list(weapons.keys()))):
        name = list(weapons.keys())[i]
        weapon_data = weapons[name]
        write_path = os.path.join(data_path, "weapons", name)
        write_json(weapon_data, 'zh_CN', write_path)
    for i in range(len(list(characters.keys()))):
        name = list(characters.keys())[i]
        character_data = characters[name]
        write_path = os.path.join(data_path, "characters", name)
        write_json(character_data, 'zh_CN', write_path)
    
    
   

# 米游社数据分武器/角色保存v1.0.8
# 米游社数据爬取：https://github.com/SAGIRI-kawaii/GenshinInfoCrawer
