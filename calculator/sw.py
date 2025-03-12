import tkinter as tk
from tkinter import ttk
import math

armor_values1 = {
    "空": [0, 0, 0],
    "锁链头盔_保护4": [2, 4, 0],
    "铁头盔_保护3": [2, 3, 0],
    "金头盔_超级": [2, 0, 0],
    "金头盔_火焰保护10": [2, 0, 0],
    '铁头盔_投射物保护6_爆炸保护6': [2,0,0],
    "钻石头盔": [3, 0, 0],
    "钻石头盔_保护1": [3, 1, 0],
    "下界合金头盔": [3, 0, 2],
    "下界合金头盔_保护2": [3, 2, 2]
}

armor_values2 = {
    "空": [0, 0, 0],
    "锁链胸甲_保护4": [5, 4, 0],
    "铁胸甲_保护3": [6, 3, 0],
    "钻石胸甲": [8, 0, 0],
    "钻石胸甲_保护1": [8, 1, 0],
    "下界合金胸甲": [8, 0, 4],
    "下界合金胸甲_保护2": [8, 2, 4]
}

armor_values3 = {
    "空": [0, 0, 0],
    "锁链护腿_保护4": [4, 4, 0],
    "铁护腿_保护3": [5, 3, 0],
    "铁护腿_火焰保护6_爆炸保护6": [5, 0, 0],
    "钻石护腿": [6, 0, 0],
    "钻石护腿_保护1": [6, 1, 0],
    "下界合金护腿": [6, 0, 2],
    "下界合金护腿_保护2": [6, 2, 2]
}

armor_values4 = {
    "空": [0, 0, 0],
    "锁链靴子_保护4": [1, 4, 0],
    "铁靴_保护3": [2, 3, 0],
    "钻石靴": [3, 0, 0],
    "钻石靴_保护1": [3, 1, 0],
    "下界合金靴": [3, 0, 2],
    "下界合金靴_保护2": [3, 2, 2],
    "抗性鞋": [3, 2, 0]
}
def sw_calculator():


    root = tk.Tk()
    root.title("数值模拟器")
    root.geometry("300x500")
    armor_label1 = tk.Label(root, text="选择护甲种类: ")
    armor_label1.pack()

    armor_combobox1 = ttk.Combobox(root, values=list(armor_values1.keys()))
    armor_combobox1.pack()
    armor_combobox2 = ttk.Combobox(root, values=list(armor_values2.keys()))
    armor_combobox2.pack()
    armor_combobox3 = ttk.Combobox(root, values=list(armor_values3.keys()))
    armor_combobox3.pack()
    armor_combobox4 = ttk.Combobox(root, values=list(armor_values4.keys()))
    armor_combobox4.pack()
    label1 = tk.Label(root,text="攻击临界计算：")
    label1.pack()
    weapon_combobox = ttk.Combobox(root, values=[5,6,7,8,9,10,11,12])
    weapon_combobox.current(3)
    weapon_combobox.pack()

    def calculate_armor_values(event=None):
        a = armor_combobox1.get()
        b = armor_combobox2.get()
        c = armor_combobox3.get()
        d = armor_combobox4.get()
        values_a = armor_values1.get(a, [0, 0, 0])
        values_b = armor_values2.get(b, [0, 0, 0])
        values_c = armor_values3.get(c, [0, 0, 0])
        values_d = armor_values4.get(d, [0, 0, 0])

        # 将数组中的值相加
        total_values = [sum(x) for x in zip(values_a, values_b, values_c, values_d)]
        res_arm = total_values[0]
        res_enc = total_values[1]
        bouns_hp = total_values[2]

        total_hp  = (20 + bouns_hp) / ((100 - res_arm * 4) / 100) / ((100 - res_enc * 4) / 100)
        result_label.config(text=f"折合血量为：{total_hp:.2f}")

        # 计算临界表并标注武器伤害
        lim = []
        weapon_damage = weapon_combobox.get()
        for i in range(8):
            critical_value = math.ceil(total_hp / (i + 5))
            lim.append(critical_value)
            if weapon_damage and int(weapon_damage) == (i + 5):
                lim[-1] = f"[{critical_value}]"

        result_label2.config(text=f"临界表：{lim}")
        result_label3.config(text=f"每刀伤害：{int(weapon_damage)* ((100 - res_arm * 4) / 100) * ((100 - res_enc * 4) / 100):.2f}")

    # 绑定事件
    armor_combobox1.bind("<<ComboboxSelected>>", calculate_armor_values)
    armor_combobox2.bind("<<ComboboxSelected>>", calculate_armor_values)
    armor_combobox3.bind("<<ComboboxSelected>>", calculate_armor_values)
    armor_combobox4.bind("<<ComboboxSelected>>", calculate_armor_values)
    weapon_combobox.bind("<<ComboboxSelected>>", calculate_armor_values)

    calculate_button = tk.Button(root, text="计算总防御力", command=calculate_armor_values)
    calculate_button.pack()
    result_label = tk.Label(root, text="折合血量为：")
    result_label.pack()
    result_label2 = tk.Label(root, text="临界数值：")
    result_label2.pack()
    result_label3 = tk.Label(root, text="")
    result_label3.pack()

    root.mainloop()




def effctive_hp_calc(best_equ):
    arr = [
        armor_values1.get(best_equ[0], [0, 0, 0]),
        armor_values2.get(best_equ[1], [0, 0, 0]),
        armor_values3.get(best_equ[2], [0, 0, 0]),
        armor_values4.get(best_equ[3], [0, 0, 0])
    ]

    armor_value = 0
    enc_value = 0
    bouns_hp = 0
    for i in arr:
        armor_value += i[0]
        enc_value += i[1]
        bouns_hp += i[2]
    total_hp = (20 + bouns_hp) / ((100 - armor_value * 4) / 100) / ((100 - enc_value * 4) / 100)

    return total_hp




