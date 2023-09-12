from tkinter import *
from tkinter import ttk

ALL_BUTTONS_TEXT = ['1', '2', '3', ' + ', '4', '5', '6', ' - ', '7', '8', '9', '*', '.', '0', ' / ', ' = ']

root = Tk()
root.title("Tkinter calculator")
root.geometry("600x800")

for c in range(4): root.columnconfigure(index=c, weight=1)
for r in range(5): root.rowconfigure(index=r, weight=1)

entry_field = Entry(font=('Consolas 60'), justify=CENTER)
entry_field.grid(row=0, column=0, columnspan=4, ipadx=0, ipady=0, padx=0, pady=0, sticky=NSEW)


def add_character_to_entry_field(character: str):
	entry_field.insert(END, character)


def add_buttons_to_window(column_count, index):
	button_text = ALL_BUTTONS_TEXT[index - 4]
	button = ttk.Button(text=button_text, command=lambda: add_character_to_entry_field(button_text))
	button.grid(row=index // column_count, column=index % column_count, ipadx=0, ipady=0, padx=0, pady=0, sticky=NSEW)


for i in range(4, 20):
	add_buttons_to_window(4, i)

root.mainloop()
