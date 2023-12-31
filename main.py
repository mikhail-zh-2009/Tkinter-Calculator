"""
Tkinter calculator by Mikhail Zhizhikin, 2023.
This application is the simple calculator made by me using the Python and its Tkinter library.
I made it to learn the Tkinter.
"""

from tkinter import *
from tkinter import ttk

ALL_BUTTONS_TEXT = ['1', '2', '3', '+', '(',
                    '4', '5', '6', '-', ')',
                    '7', '8', '9', '*', 'e',
                    '.', '0', '/', '=', 'C']

root = Tk()
root.title("Tkinter calculator")
root.geometry("800x800")

style = ttk.Style()
style.theme_use('alt')
style.configure('TButton', background = 'black', foreground = 'white', font='Arial 15', width = 20, borderwidth=0, focusthickness=0, focuscolor='none')
style.map('TButton', background=[('active', '#888')])

# Configuring the grid to place widgets beautifully.
for c in range(5): root.columnconfigure(index=c, weight=1)
for r in range(5): root.rowconfigure(index=r, weight=1)

# To see evaluation that we write.
entry_text = StringVar()
entry_field = Entry(font=('Consolas 30'), bg='black', fg='white', borderwidth=0, justify=CENTER, textvariable=entry_text)
entry_field.grid(row=0, column=0, columnspan=5, sticky=NSEW)


def equals_button_command():
	output_entry_text = '...'
	try:
		# Solve evaluation in text field to output.
		output_entry_text = eval(entry_field.get())
	except ZeroDivisionError:
		output_entry_text = 'Division by zero.'
	except OverflowError:
		output_entry_text = 'Result is too large.'
	except (ValueError, SyntaxError, NameError):
		output_entry_text = 'Enter an evaluation.'
	# Output result in text field.
	entry_text.set(output_entry_text)


# To add characters to text field using buttons.
def add_character_to_entry_field(character: str):
	entry_field.insert(END, character)


# To place button widgets in window.
def add_buttons_to_window(column_count, index):
	# We substract 5 from index, because first 5 columns of grid is used by text field.
	button_text = ALL_BUTTONS_TEXT[index - 5]
	text_button_command = None
	# If index position in text list equals 4 ('C' button) we clear screen.
	if index == len(ALL_BUTTONS_TEXT) + 4:
		text_button_command = lambda: entry_text.set('')
	# Or index button is '=', we solve the evaluation
	elif index == len(ALL_BUTTONS_TEXT) + 3:
		text_button_command = equals_button_command
	# If not, we just add button's character to entry field
	else:
		text_button_command = lambda: add_character_to_entry_field(button_text)
	button = ttk.Button(root, text=button_text, command=text_button_command)
	button.grid(row=index // column_count, column=index % column_count, sticky=NSEW)


for i in range(5, 25):
	add_buttons_to_window(5, i)

# To solve the evaluation by pressing enter.
root.bind('<Return>', lambda e: equals_button_command())

root.mainloop()
