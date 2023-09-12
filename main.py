from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Tkinter calculator")
root.geometry("800x600")

for c in range(4): root.columnconfigure(index=c, weight=1)
for r in range(5): root.rowconfigure(index=r, weight=1)

entry_field = Entry(font='Consolas 60', justify=CENTER)
entry_field.grid(row=0, column=0, columnspan=4, ipadx=0, ipady=0, padx=0, pady=0, sticky=NSEW)


def add_character_to_entry_field(character: str):
	entry_field.insert(END, character)


for r in range(1, 4):
	for c in range(3):
		btn_num = ttk.Button(text=f"{r*3+c-2}", command=lambda: add_character_to_entry_field(f"{r*3+c-2}"))
		btn_num.grid(row=r, column=c, ipadx=0, ipady=0, padx=0, pady=0, sticky=NSEW)

btn_plus = ttk.Button(text="+")
btn_plus.grid(row=1, column=3, ipadx=0, ipady=0, padx=0, pady=0, sticky=NSEW)

btn_minus = ttk.Button(text="-")
btn_minus.grid(row=2, column=3, ipadx=0, ipady=0, padx=0, pady=0, sticky=NSEW)

btn_multiply = ttk.Button(text="*")
btn_multiply.grid(row=3, column=3, ipadx=0, ipady=0, padx=0, pady=0, sticky=NSEW)

btn_divide = ttk.Button(text="/")
btn_divide.grid(row=4, column=3, ipadx=0, ipady=0, padx=0, pady=0, sticky=NSEW)

btn_equals = ttk.Button(text="=")
btn_equals.grid(row=4, column=2, ipadx=0, ipady=0, padx=0, pady=0, sticky=NSEW)

btn_point = ttk.Button(text=".")
btn_point.grid(row=4, column=1, ipadx=0, ipady=0, padx=0, pady=0, sticky=NSEW)

btn0 = ttk.Button(text="0")
btn0.grid(row=4, column=0, ipadx=0, ipady=0, padx=0, pady=0, sticky=NSEW)


root.mainloop()