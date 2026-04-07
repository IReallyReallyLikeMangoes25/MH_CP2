# MH 1st gui notes
import tkinter as tk

root = tk.Tk()

root.title("Testing")
root.configure(background = "orange")
root.minsize(250, 250)
root.maxsize(1000, 1000)
# dimensions followed by x and y
root.geometry("300x300+100+100")
label = tk.Label(root, text = "This is currently working!", font = ("Times New Roman", 14, "bold"))
label.config(fg = "blue", background = "green")
label.pack()
image = tk.PhotoImage(file = "notes/images/falling-bread-bread.gif")
tk.Label(root, image = image).pack()
# stuff about buttons
root.count = 0
def add():
    root.count += 1
    num["text"] = root.count
    
btn = tk.Button(root, text = "Add", command = add)
btn.pack()
num = tk.Label(root, text = "0")
num.pack()
label.pack()

root.mainloop()