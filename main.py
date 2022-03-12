import os
from typing import Text
from program import program
import re
import tkinter as tk
from tkinter.filedialog import askopenfilename

class StationeryFunctions:

    def __init__(self, text):

        self.text = text

        self.create_binding_keys()

        self.binding_functions_config()

        self.join_function_with_main_stream()

    def join_function_with_main_stream(self):

        self.text.storeobj['Copy'] = self.copy

        self.text.storeobj['Cut'] = self.cut

        self.text.storeobj['Paste'] = self.paste

        self.text.storeobj['SelectAll'] = self.select_all

        self.text.storeobj['DeselectAll'] = self.deselect_all

        return

    def binding_functions_config(self):

        self.text.tag_configure("sel", background="skyblue")

        return

    def copy(self, event):

        self.text.event_generate("&lt;&lt;Copy>>")

        return

    def paste(self, event):

        self.text.event_generate("&lt;&lt;Paste>>")

        return

    def cut(self, event):

        self.text.event_generate("&lt;&lt;Cut>>")

        return

    def create_binding_keys(self):

        for key in ["&lt;Control-a>","&lt;Control-A>"]:

            self.text.master.bind(key, self.select_all)

        for key in ["&lt;Button-1>","&lt;Return>"]:

            self.text.master.bind(key, self.deselect_all)

        return

    def select_all(self, event):

        self.text.tag_add("sel",'1.0','end')

        return

    def deselect_all(self, event):

        self.text.tag_remove("sel",'1.0','end')

        return

def open_file():

    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

    if not filepath:

        return

    txt_edit.delete(1.0, tk.END)

    with open(filepath, "r") as input_file:

        text = input_file.read()

        txt_edit.insert(tk.END, text)

def save_file():

    with open(os.path.abspath("input.txt"), "w") as output_file:

        text = txt_edit.get(1.0, tk.END)

        mips = text.split('\n')

        output_file.write(text)

    #os.system("python program.py < input.txt > output.txt")

    filepath = os.path.abspath("output.txt")

    txt_edit.delete(1.0, tk.END)

    with open(filepath, "r") as input_file:

        text = input_file.read()

        txt_edit.insert(tk.END, text)
    
    clock = int(entry.get())

    result, tcpu = program(mips, clock)

    for i in result:

        txt_edit.insert(tk.END, i)

    txt_edit.insert(tk.END, tcpu)


window = tk.Tk()

window.title("Mips to Binary")

window.rowconfigure(0, minsize=480, weight=1)

window.columnconfigure(1, minsize=480, weight=1)

txt_edit = tk.Text(window)

fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)

btn_open = tk.Button(fr_buttons, text="Open", command=open_file)

btn_save = tk.Button(fr_buttons, text="Translate", command=save_file)

txt_clock = tk.Label(fr_buttons, text="Frecuency")

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")

txt_edit.grid(row=0, column=1, sticky="nsew")

txt_clock.place(x=4, y=75, width=60)

entry = tk.Entry(window)

entry.place(x=7, y=103, width=60)

window.mainloop()
