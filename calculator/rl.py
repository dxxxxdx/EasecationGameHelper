import tkinter as tk
from tkinter import ttk

def rl_calculator():
    root = tk.Tk()

    root.title("数值模拟器")
    root.geometry("500x500")

    label1 = tk.Label(root, text=f"怪物的折合血量：")
    label2 = tk.Label(root, text=f"玩家的攻击力")
    label1.pack(pady=10)
    label2.pack(pady=10)

    def pop_up(list1, list2):
        # 创建弹窗
        popup = tk.Toplevel(root)
        popup.title("计算结果")
        popup.geometry("500x400")

        # print1的输出内容
        label1 = tk.Label(popup, text="print1输出内容", font=("Arial", 12, "bold"))
        label1.pack(pady=5)
        text1 = tk.Text(popup, wrap="word", height=10, width=60)
        text1.pack(pady=5)
        for item in list1:
            text1.insert("end", f"玩家攻击力为{item[1]}下，需要{item[0]}回合\n")
        text1.config(state="disabled")  # 禁止编辑

        # print2的输出内容
        label2 = tk.Label(popup, text="print2输出内容 (无技能)", font=("Arial", 12, "bold"))
        label2.pack(pady=5)
        text2 = tk.Text(popup, wrap="word", height=10, width=60)
        text2.pack(pady=5)
        for item in list2:
            text2.insert("end", f"(无技能)玩家攻击力为{item[1]}下，需要{item[0]}回合\n")
        text2.config(state="disabled")  # 禁止编辑

        # 关闭按钮
        close_button = tk.Button(popup, text="关闭", command=popup.destroy)
        close_button.pack(pady=10)

    def get_number(*args):
        mon_hp = scale_hp.get()
        mon_def = scale_def.get()
        hero_atk = scale_hero_atk.get()
        combo_rate = scale_combo_rate.get() / 100

        mon_eff_hp = mon_hp / ((100 - mon_def) / 100)
        label1.config(text=f"怪物的折合血量：{mon_eff_hp:.2f}")

        lim_results = lim_calculator(mon_hp, mon_def, hero_atk, combo_rate, with_skill=True)
        lim_results2 = lim_calculator(mon_hp, mon_def, hero_atk, combo_rate, with_skill=False)

        # 显示弹窗
        pop_up(lim_results, lim_results2)

    # 滑动条设置
    scale_hp = tk.Scale(root, from_=1, to=100, orient="horizontal", length=300, label="怪物血量")
    scale_def = tk.Scale(root, from_=0, to=99, orient="horizontal", length=300, label="怪物防御（百分比）")
    scale_hero_atk = tk.Scale(root, from_=1, to=30, orient="horizontal", length=300, label="玩家攻击力")
    scale_combo_rate = tk.Scale(root, from_=0, to=100, orient="horizontal", length=300, label="连击倍率（百分比）")

    button = tk.Button(root, text="开始计算", command=get_number)

    scale_hp.pack(pady=10)
    scale_def.pack(pady=10)
    scale_hero_atk.pack(pady=10)
    scale_combo_rate.pack(pady=10)
    button.pack(pady=10)

    root.mainloop()


def fight_simulator(mon_hp, mon_def, hero_atk, skill_param, with_skill=False):
    turn = 0
    skilltimes = 0
    info = []
    current_hp = mon_hp

    while True:
        temp = current_hp
        current_hp -= hero_atk * (100 - mon_def) * 0.01
        turn += 1
        #模拟战斗，以下是战斗逻辑

        if current_hp <= 0:
            info.append((turn, 0))
            break
        if current_hp <= 15 < temp:
            skilltimes += 2

        if skilltimes >= 1 and with_skill:
            current_hp -= hero_atk * (100 - mon_def) * 0.01 * skill_param


        #下面别搞

        info.append((turn, current_hp))

    return info


def lim_calculator(mon_hp, mon_def, hero_atk, combo_rate, with_skill):
    lim_list = []

    while hero_atk <= 30:
        info = fight_simulator(mon_hp, mon_def, hero_atk, combo_rate, with_skill)
        turn_to_kill = next((turn for turn, hp in info if hp <= 0), None)
        if turn_to_kill is not None:
            if not lim_list or lim_list[-1][0] != turn_to_kill:
                lim_list.append((turn_to_kill, hero_atk))

        hero_atk += 1

    return lim_list


if __name__ == '__main__':
    rl_calculator()
