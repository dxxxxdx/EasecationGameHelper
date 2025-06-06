import tkinter as tk


def intro_term():
    root = tk.Tk()
    root.attributes("-topmost", True)
    screen_width = root.winfo_screenwidth()
    root.geometry(f"500x700+{screen_width - 550}+100")
    label1 = tk.Label(root,text="\n以下内容由ai生成\n\n\n"
                                "临界效应是指，当玩家的攻击力达到某个临界点时，击败敌人所需的回合数会显著减少。\n"
                                "具体来说，当玩家的攻击力每增加一点，击败敌人所需的回合数会减少。\n"
                                "这种现象被称为临界效应。\n"
                                "例如：一位45血量的生物，8点伤害武器需要6刀，而9点伤害武器则需要5刀\n"
                                "两种武器所差的“1”刀，即体现了临界效应\n"
                                "一般而言，折合血量越高，临界效应越明显\n"
                                "临界表列出了玩家面对不同伤害时，可以承受的刀数\n\n\n")
    label2 = tk.Label(root,text="百分比减伤是指在游戏中，玩家可以通过装备或技能减少受到的伤害。\n"
                                "例如，某个装备可以减少10%的伤害，那么玩家受到的伤害会减少10%。\n"
                                "假设玩家的实际血量为20，装备提供80%的减伤\n"
                                "折合血量 为 20 / （1-80%），也就是100\n"
                                "也就是说，这位玩家会需要100点伤害才能死亡\n"
                                "（本计算器仅计算正常玩家收到的一般物理伤害）\n")
    label3 = tk.Label(root,text="哈基米德第四公式\n"
                                "对于空岛战争这样的游戏，我们可以用 折合血量 * 武器攻击力 计算玩家战斗力\n"
                                "为什么可以这么做呢？原因就在于不考虑对手能力的时候，折合血量阶梯正比于输出时间\n"
                                "而攻击力则是输出效率，二者相乘表示玩家相对输出能力\n"
                                "（名词 “阶梯正比”指的是向上取整的正比例函数，数值稠密时可以作为正比对待）")
    label1.pack()
    label2.pack()
    label3.pack()
    button1 = tk.Button(root,text="我知道了",command=lambda :on_close(),padx=20,pady=20)
    def on_close():
        root.destroy()
    button1.pack()
    root.mainloop()