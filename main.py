import tkinter as tk
import tkinter.ttk as ttk
import calculator as calc




def main ():
    root = tk.Tk()
    root.attributes("-topmost", True)
    screen_width = root.winfo_screenwidth()
    root.geometry(f"500x500+{screen_width - 550}+100")
    button1 = tk.Button(text="空岛伤害计算器",command=lambda :calc.sw_calculator())
    button1.pack()
    button2 = tk.Button(text="起床攻击计算器",command=lambda :calc.bw_calculator())
    button2.pack()




    root.mainloop()








if __name__ == "__main__":
    main()