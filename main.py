from tkinter import *
from tkinter import ttk

ALL_BUTTONS_TEXT = ['1', '2', '3', ' + ', '4', '5', '6', ' - ', '7', '8', '9', '*', '.', '0', ' / ', ' = ']

root = Tk()
root.title("Tkinter calculator")
root.geometry("400x500")

for c in range(4): root.columnconfigure(index=c, weight=1)
for r in range(5): root.rowconfigure(index=r, weight=1)

entry_text = StringVar()
entry_field = Entry(font=('Consolas 30'), justify=CENTER, textvariable=entry_text)
entry_field.grid(row=0, column=0, columnspan=4, ipadx=0, ipady=0, padx=0, pady=0, sticky=NSEW)


def equals_button_command():
	output_entry_text = 'empty'
	try:
		output_entry_text = eval(entry_field.get())
	except ZeroDivisionError:
		output_entry_text = 'Division by zero.'
	except OverflowError:
		output_entry_text = 'Result is too large.'
	except (ValueError, SyntaxError, NameError):
		output_entry_text = 'Enter an evaluation.'
	entry_text.set(output_entry_text)


def add_character_to_entry_field(character: str):
	entry_field.insert(END, character)


def add_buttons_to_window(column_count, index):
	button_text = ALL_BUTTONS_TEXT[index - 4]
	text_button_command = None
	if index < len(ALL_BUTTONS_TEXT) + 3:
		text_button_command = lambda: add_character_to_entry_field(button_text)
	else:
		text_button_command = equals_button_command
	button = ttk.Button(text=button_text, command=text_button_command)
	button.grid(row=index // column_count, column=index % column_count, ipadx=0, ipady=0, padx=0, pady=0, sticky=NSEW)


for i in range(4, 20):
	add_buttons_to_window(4, i)

root.bind('<Return>', lambda e: equals_button_command())

root.mainloop()
