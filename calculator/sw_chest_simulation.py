import calculator.sw_dict as sw_dict
import random
from calculator.sw import effctive_hp_calc
import tkinter as tk

import matplotlib.pyplot as plt



class SimuResult:
    def __init__(self, total_list, best_equ, comleted, scorex, useful_prop, super_prop,have_gap,fight_level):
        self.total_list = total_list
        self.best_equ = best_equ
        self.comleted = comleted
        self.scorex = scorex
        self.useful_prop = useful_prop
        self.super_prop = super_prop
        self.have_gap = have_gap
        self.fight_level = fight_level

def sw_simulation(times):
    total_list = []

    for j in range(times):
        fixed_item = []
        if j == 0 :
            fixed_item = ["8铁锭", "铁镐_时运1_效率3", "我的装扮"]
        else:
            pass
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
    useful_prop = get_useful_prop(total_list)
    super_prop = have_super_prop(total_list)
    comleted = None not in best_equ
    have_gap = get_gap(total_list)
    fight_level = 0
    try:
        weapon_damage =  sw_dict.weapons.get(best_equ[4],-1)
        if weapon_damage != -1:
            fight_level = scorex * weapon_damage
    except:
        pass

    return SimuResult(total_list, best_equ, comleted, scorex, useful_prop, super_prop,have_gap,fight_level)

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
            else:
                pass

    best_helmet = get_max_item(helmet_arr, sw_dict.helmets)
    best_chestplate = get_max_item(chestplate_arr, sw_dict.chestplates)
    best_leggings = get_max_item(leggings_arr, sw_dict.leggings)
    best_boots = get_max_item(boots_arr, sw_dict.boots)
    best_weapons = get_max_item(weapons_arr, sw_dict.weapons)

    return [best_helmet, best_chestplate, best_leggings, best_boots, best_weapons]

def get_useful_prop (listx):
    useful_prop = []
    for sublist in listx:
        for item in sublist:
            if item in sw_dict.useful_prop :
                useful_prop.append(item)
    return useful_prop

def have_super_prop(listx):
    res = []
    for sublist in listx:
        for item in sublist:
            if item in sw_dict.super_prop :
                res.append(item)
    return res

def get_max_item(items, item_dict):
    max_value = float('-inf')
    max_item = None
    for item in items:
        if item in item_dict:
            value = item_dict[item]
            if value > max_value:
                max_value = value
                max_item = item
    return max_item
def get_gap(listx):
    for sublist in listx:
        if "金苹果_2" in sublist or "金苹果_4" in sublist or "金苹果_8" in sublist:
            return True

def score(best_equ):
    score1 = sw_dict.helmets.get(best_equ,0)
    score2 = sw_dict.chestplates.get(best_equ,0)
    score3 = sw_dict.leggings.get(best_equ,0)
    score4 = sw_dict.boots.get(best_equ,0)
    total = score1 + score2 + score3 + score4
    return total

def sw_simu_gui():
    root = tk.Tk()
    root.geometry("1000x500")
    button1 = tk.Button(root,text="模拟1次",command=lambda :simu())
    res = None
    def simu():
        nonlocal res
        res = sw_simulation(3)
        sw_simu_label_updater(res,label_set)
    label_set = [tk.Label(root) for _ in range(12)]

    for label in label_set:
        label.pack()

    button1.pack()

    root.mainloop()

def sw_simu_label_updater(res,label_set):
    total_list = res.total_list
    for i, sublist in enumerate(total_list, start=1):
        label_set[i].configure(text=sublist)
    label_set[-5].configure(text=f"\n你有的真神器{res.super_prop}")
    label_set[-4].configure(text=f"你的关键道具为：{res.useful_prop}", fg="red")
    label_set[-3].configure(text=f"你的最好装备：{res.best_equ}", fg="red")
    label_set[-2].configure(text=f'你的缺甲状态为：{not res.comleted}')
    label_set[-1].configure(text=f"你装备的折合血量为{res.scorex:.4f}")

def avg_effective_hp():
    for p in range(12):
        res = 0
        for i in range(1000):
            res += sw_simulation(p).scorex
        print(f"刷新{p}箱子下，平均折合血量{res/1000:.2f}")
    print("---------------------")

def avg_completeness():
    for p in range(12):
        res = 0
        for i in range(1000):
            res += sw_simulation(p).comleted
        print(f"刷新{p}箱子下，平均缺甲率{(1000 - res)/10:.4f}")
    print("----------------------")

def good_equ_rate(eff_hp):
    for p in range(12):
        p = 3
        countx = 0
        for i in range(100000):
            i = sw_simulation(p).scorex
            if i >= eff_hp:
                countx += 1
        print(f"刷新{p}箱子下，平均正常装备（超过{eff_hp}）率：{countx / 1000}")
    print("----------------------")

def get_super_prop_rate():
    print("真神器指秒人斧，附魔金，图腾")
    for p in range(16):
        res = 0
        for i in range(1000):
            a = sw_simulation(p).super_prop
            if a:
                res += 1
        print(f"刷新{p}箱子下，平均拿到真神器率{res/10:.4f}")



def total_data(times):

    for p in range(12):
        res_cpt = 0
        expect_eff_hp = 100
        res_good_rate = 0
        res_super_prop = 0
        res_have_gap = 0
        res_eff_hp = []
        res_fight_level = []
        for i in range(times):
            res = sw_simulation(p)
            res_cpt += res.comleted
            if (res.scorex > expect_eff_hp):
                res_good_rate += 1
            if (res.super_prop):
                res_super_prop += 1
            if (res.have_gap):
                res_have_gap += 1
            res_eff_hp.append(res.scorex)
            res_fight_level.append(res.fight_level)
        res_eff_hp.sort()
        res_fight_level.sort()
        plt.plot(res_fight_level, marker='o')  # marker='o' 表示点的样式为圆圈
        plt.title(f'simulation with {p} chest')
        plt.xlabel('player')
        plt.ylabel('level')
        plt.grid(True)
        plt.show()

        print(f"刷新{p}箱子下，折合血量中位数为{res_eff_hp[int(len(res_eff_hp)/2)]:.4f}")
        print(f"刷新{p}箱子下，战斗力中位数为{res_fight_level[int(len(res_fight_level) / 2)]:.4f}")
        print(f"刷新{p}箱子下，平均正常装备（超过{expect_eff_hp}）率：{res_good_rate / (times/100)}")
        print(f"刷新{p}箱子下，平均折合血量{sum(res_eff_hp)/len(res_eff_hp):.2f}")
        print(f"刷新{p}箱子下，平均战斗力{sum(res_fight_level) / len(res_fight_level):.2f}")
        print(f"刷新{p}箱子下，平均缺甲率{(times - res_cpt) / (times/100):.4f}")
        print("真神器指秒人斧，附魔金，图腾")
        print(f"刷新{p}箱子下，平均拿到真神器率{res_super_prop / (times/100):.4f}")
        print(f"刷新{p}箱子下，没有苹果吃的概率为{(times - res_have_gap) / (times/100):.4f}")
        print("=================================================")


if __name__ == "__main__":
    total_data(10000)
