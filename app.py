# Step 1: Importing packages
import tkinter as tk
from functools import partial

operation = 0

# Step 7: Retrieve, Calculate and display
def display_btn(clicked_button):
    current_text = lbl.cget("text")
    new_text = f"{current_text}{clicked_button}"
    lbl.config(text=new_text)

    global operation
    if "=" in new_text:
        operation = eval(new_text[:-1])  # Evaluate the expression excluding the '='
        new_text = f"{operation}"
        lbl.config(text=new_text)
    else:
        operation = new_text

# Step 8: Clear Display
def clear_dis():
    lbl.config(text="")

# Step 2 : Create Main Window
root = tk.Tk()
root.resizable(False, False)

# Step 3: Create a label
lbl = tk.Label(root, text="")
lbl.grid(row=0, column=0, columnspan=4, padx=1, pady=(5, 1))

# Step 4: Create number buttons
buttons = {}
for i in range(1, 10):
    buttons[i] = tk.Button(root, text=f"{i}", height=2, width=4, command=lambda num=i: display_btn(num))
    buttons[i].grid(row=(i - 1) // 3 + 1, column=(i - 1) % 3, padx=1, pady=1)

# Step 5: Create operator buttons
operators = ["+", "-", "*", "/"]
for i, op in enumerate(operators):
    cmd = partial(display_btn, op)
    btn_op = tk.Button(root, text=op, height=2, width=4, command=cmd)
    btn_op.grid(row=i + 1, column=3, padx=1, pady=1)

# Step 6: Create rest of the widgets
btn0 = tk.Button(root, text="0", height=2, width=4, command=lambda: display_btn("0"))
btn0.grid(row=4, column=1, padx=1, pady=(1, 5))

btnDot = tk.Button(root, text=".", height=2, width=4, command=lambda: display_btn("."))
btnDot.grid(row=4, column=0, padx=1, pady=(1, 5))

btnAC = tk.Button(root, text="AC", height=2, width=4, command=clear_dis)
btnAC.grid(row=4, column=2, padx=1, pady=(1, 5))

btnEqu = tk.Button(root, text="=", height=2, width=4, command=lambda: display_btn("="))
btnEqu.grid(row=0, column=3, padx=1, pady=(5, 1))

root.mainloop()
