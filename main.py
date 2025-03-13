import tkinter as tk
import tkinter.ttk as ttk
import calculator as calc
from intro_term import intro_term




def main ():
    root = tk.Tk()
    root.attributes("-topmost", True)
    screen_width = root.winfo_screenwidth()
    root.geometry(f"500x500+{screen_width - 550}+100")
    label1 = tk.Label(root,text="EASECATION游戏助手",font=("", 24))
    label1.pack()
    button1 = tk.Button(root,text="空岛伤害计算器",command=lambda :calc.sw_calculator(),padx=30,pady=30)
    button1.pack()
    button2 = tk.Button(root,text="起床攻击计算器",command=lambda :calc.bw_calculator(),padx=30,pady=30)
    button2.pack()
    button3 = tk.Button(root,text="空岛开箱模拟器",command=lambda :calc.sw_simu_gui(),padx=30,pady=30)
    button3.pack()
    button4 = tk.Button(root,text="术语介绍",command=lambda :intro_term(),padx=30,pady=30)
    button4.pack()

    root.mainloop()








if __name__ == "__main__":
    main()