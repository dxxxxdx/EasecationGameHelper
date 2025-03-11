import tkinter as tk
from tkinter import ttk
import math

armor_values1 = {
    "空":7 ,
    "锁链": 9,
    "铁": 11,
    "钻石": 13
}
armor_values2 = {
    "空":0,
    "保护1":4,
    "保护2":8,
    "保护3":12,
    "保护4":16
}

root = tk.Tk()
root.title("数值模拟器")
root.geometry("300x500")
armor_label1 = tk.Label(root, text="选择护甲种类:")
armor_label1.pack()

armor_combobox1 = ttk.Combobox(root, values=list(armor_values1.keys()))
armor_combobox1.pack()
armor_combobox2 = ttk.Combobox(root, values=list(armor_values2.keys()))
armor_combobox2.pack()

label1 = tk.Label(text="攻击临界计算：")
label1.pack()
weapon_combobox = ttk.Combobox(root, values=[4,5,6,7,8,9])
weapon_combobox.current(1)
weapon_combobox.pack()

def calculate_armor_values(event=None):
    a = armor_combobox1.get()
    b = armor_combobox2.get()
    res_arm = armor_values1.get(a,0)
    res_enc = armor_values2.get(b,0)


    total_hp  = (20) / ((100 - res_arm * 4) / 100) / ((100 - res_enc * 4) / 100)
    result_label.config(text=f"折合血量为：{total_hp:.2f}")

    lim = []
    weapon_damage = weapon_combobox.get()
    for i in range(8):
        critical_value = math.ceil(total_hp / (i + 4))
        lim.append(critical_value)
        if weapon_damage and int(weapon_damage) == (i + 4):
            lim[-1] = f"[{critical_value}]"

    result_label2.config(text=f"临界表：{lim}")
    result_label3.config(text=f"每刀伤害：{int(weapon_damage)* ((100 - res_arm * 4) / 100) * ((100 - res_enc * 4) / 100):.2f}")

# 绑定事件
armor_combobox1.bind("<<ComboboxSelected>>", calculate_armor_values)
armor_combobox2.bind("<<ComboboxSelected>>", calculate_armor_values)
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
