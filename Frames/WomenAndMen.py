from data import men, women
from tkinter import Label, Listbox, Entry, messagebox, Button, END, E, W, N, HORIZONTAL
from tkinter.ttk import Separator


class People:
    def __init__(self, tab):

        # List of women
        women_label = Label(tab, text="Women")
        women_label.grid(column=0, row=0, padx=25, pady=4, sticky=W)
        self.women_list = Listbox(tab, width=35, height=10)
        self.women_list.grid(column=0, row=1, padx=25)

        # Add Woman
        add_woman_label = Label(tab, text="Add Woman")
        add_woman_label.grid(column=1, row=0, padx=25, pady=4, sticky=W)
        self.add_woman_entry = Entry(tab, width=24)
        self.add_woman_entry.grid(column=1, row=1, padx=27, sticky=N+W)
        add_woman_btn = Button(tab, text="Add Woman", width=20, command=lambda: self.add("woman", self.add_woman_entry.get()))
        add_woman_btn.grid(column=1, row=1, pady=25, padx=27, sticky=N+W)

        tab.columnconfigure(3, weight=1)
        Separator(tab, orient=HORIZONTAL).grid(row=2, pady=20, columnspan=4, sticky=E+W)

        # List of men
        men_label = Label(tab, text="Men")
        men_label.grid(column=0, row=3, padx=25, sticky=W)
        self.men_list = Listbox(tab, width=35, height=10)
        self.men_list.grid(column=0, row=4, padx=25)

        # Add Man
        add_man_label = Label(tab, text="Add Man")
        add_man_label.grid(column=1, row=3, padx=25, sticky=W)
        self.add_man_entry = Entry(tab, width=24)
        self.add_man_entry.grid(column=1, row=4, padx=27, sticky=N + W)
        add_man_btn = Button(tab, text="Add Man", width=20, command=lambda: self.add("man", self.add_man_entry.get()))
        add_man_btn.grid(column=1, row=4, pady=25, padx=27, sticky=N + W)

    def add(self, sex, name):
        if len(name) < 3:
            messagebox.showinfo("Name is too short", "Please provide real name")
            return

        if sex == "woman":
            women.append(name)
            self.women_list.insert(END, name)
            self.add_woman_entry.delete(0, END)
        else:
            men.append(name)
            self.men_list.insert(END, name)
            self.add_man_entry.delete(0, END)
