import calculator.sw_dict as sw_dict
import random
from calculator.sw import effctive_hp_calc


def sw_simulation(times):
    total_list = []
    for j in range(times):
        fixed_item = ["8铁锭", "铁镐_时运1_效率3", "我的装扮"]
        fixed_item.extend(get_item(sw_dict.block_dict, 2))
        fixed_item.extend(get_item(sw_dict.prop_dict, 1))
        fixed_item.extend(get_item(sw_dict.thrown_dict, 1))
        fixed_item.extend(get_item(sw_dict.misc_dict, 2))
        fixed_item.extend(get_armour("b", 4))

        random_item = []
        dict_list = [sw_dict.block_dict, sw_dict.prop_dict, sw_dict.thrown_dict, sw_dict.misc_dict,
                     sw_dict.potion_dict, sw_dict.tool_dict, sw_dict.sp_dict, "armour_a", "armour_b", "0"]
        extra_weight = [5, 13, 10, 20, 3, 10, 1, 3, 18, 17]
        for i in range(8):
            tar_dict = random.choices(dict_list, weights=extra_weight, k=1)[0]  # 需要从列表中提取实际的值
            if tar_dict == "armour_a":
                random_item.extend(get_armour("a", 1))
            elif tar_dict == "armour_b":
                random_item.extend(get_armour("b", 1))
            elif tar_dict == "0":
                pass
            else:
                random_item.extend(get_item(tar_dict, 1))
        total_list.append(random_item)
        total_list.append(fixed_item)

    best_equ = orgnize_armour(total_list)
    scorex = effctive_hp_calc(best_equ)
    if None in best_equ:
        comleted = 0
    else:
        comleted = 1
    return (total_list,best_equ,comleted,scorex)


def get_item(type_dict, times=1):
    name_list = list(type_dict.keys())
    weight_list = list(type_dict.values())
    res = random.choices(name_list, weights=weight_list, k=times)
    return res


def get_armour(type_a_b, times=1):
    armour_list = [sw_dict.level_1_dict, sw_dict.level_2_dict, sw_dict.level_3_dict, sw_dict.level_4_dict,
                   sw_dict.level_5_dict, sw_dict.level_6_dict, sw_dict.level_7_dict, sw_dict.level_8_dict,
                   sw_dict.level_9_dict, sw_dict.level_10_dict]
    armour_weight_a = [0, 0, 0, 0, 10, 10, 20, 25, 20, 15]
    armour_weight_b = [15, 20, 23, 10, 10, 10, 5, 4, 2, 1]
    if type_a_b == "a":
        tar_dict = random.choices(armour_list, weights=armour_weight_a, k=1)[0]  # 需要从列表中提取实际的值
    elif type_a_b == "b":
        tar_dict = random.choices(armour_list, weights=armour_weight_b, k=1)[0]  # 需要从列表中提取实际的值
    else:
        tar_dict = None

    res = random.choices(list(tar_dict.keys()), weights=list(tar_dict.values()), k=times)
    return res


def orgnize_armour(listx):
    helmet_arr = []
    chestplate_arr = []
    leggings_arr = []
    boots_arr = []
    weapons_arr = []

    for sublist in listx:
        for item in sublist:
            if item in sw_dict.helmets:
                helmet_arr.append(item)
            elif item in sw_dict.chestplates:
                chestplate_arr.append(item)
            elif item in sw_dict.leggings:
                leggings_arr.append(item)
            elif item in sw_dict.boots:
                boots_arr.append(item)
            elif item in sw_dict.weapons:
                weapons_arr.append(item)

    best_helmet = get_max_item(helmet_arr, sw_dict.helmets)
    best_chestplate = get_max_item(chestplate_arr, sw_dict.chestplates)
    best_leggings = get_max_item(leggings_arr, sw_dict.leggings)
    best_boots = get_max_item(boots_arr, sw_dict.boots)
    best_weapons = get_max_item(weapons_arr, sw_dict.weapons)

    return [best_helmet, best_chestplate, best_leggings, best_boots, best_weapons]


def get_max_item(items, item_dict):
    # 初始化最大值和对应的元素
    max_value = float('-inf')
    max_item = None
    # 遍历列表中的元素
    for item in items:
        # 检查元素是否在字典中
        if item in item_dict:
            # 获取元素对应的值
            value = item_dict[item]
            # 更新最大值和对应的元素
            if value > max_value:
                max_value = value
                max_item = item
    return max_item

def score(best_equ):
    score1 = sw_dict.helmets.get(best_equ,0)
    score2 = sw_dict.chestplates.get(best_equ,0)
    score3 = sw_dict.leggings.get(best_equ,0)
    score4 = sw_dict.boots.get(best_equ,0)
    total = score1 + score2 + score3 + score4
    return total


def test ():
    a1 = 0
    maxx = 0
    for i1 in range(100):
        res = sw_simulation(3)
        a1 += res
        if res > maxx:
            maxx = res

    print(maxx)
    print(a1/100)




if __name__ == "__main__":
    test()