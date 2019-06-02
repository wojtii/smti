import tkinter as tk
from data import p, men, women, update_global_pref
from tkinter import Label, W, N, E, Button, Listbox, END, messagebox
from tkinter.ttk import Combobox
from solver import solve


class Preferences:
    def __init__(self, tab):
        # Scroll Bar
        yscroll = tk.Scrollbar(tab, orient=tk.VERTICAL)
        xscroll = tk.Scrollbar(tab, orient=tk.HORIZONTAL)
        yscroll.pack(side=tk.RIGHT, fill=tk.Y)
        xscroll.pack(side=tk.BOTTOM, fill=tk.X)

        self.canvas = tk.Canvas(tab)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas['yscrollcommand'] = yscroll.set
        self.canvas['xscrollcommand'] = xscroll.set
        yscroll['command'] = self.canvas.yview
        xscroll['command'] = self.canvas.xview

        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window(4, 4, window=self.frame, anchor='nw')
        self.frame.bind("<Configure>", self._on_frame_configure)

        # Set preferences for ...
        preferences_label = Label(self.frame, text="Preferences for: ")
        preferences_label.grid(column=0, row=0, padx=25, pady=4, sticky=W)
        self.people_list = Combobox(self.frame)
        self.people_list.grid(column=1, row=0, padx=5, pady=4, sticky=W)
        self.autoCreatedWidgets = []
        add_pref = Button(self.frame, text="Add Preference", width=20, command=lambda: self.add_pref())
        add_pref.grid(column=1, row=1000, pady=25, padx=27, sticky=N + W)

        # Preferences window
        self.frame.columnconfigure(3, weight=1)
        self.pref_box = Listbox(self.frame, width=80, height=10)
        self.pref_box.grid(column=0, columnspan=3,  row=1001, pady=25, padx=27, sticky=E+W)
        self.currentSex = 'Man'
        self.currentPref = ''

        # Solve them all
        solve_btn = Button(self.frame, text="Solve", width=20, command=lambda: self.solve())
        solve_btn.grid(column=1, row=1002, pady=25, padx=27, sticky=N + W)

    def _on_frame_configure(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def update_screen(self):
        # Combo box update
        self.people_list.destroy()
        self.people_list = Combobox(self.frame, values=women+men)
        self.people_list.grid(column=1, row=0, padx=5, pady=4, sticky=W)
        self.people_list.bind("<<ComboboxSelected>>", self.selected)

    # Handle select event on combo box
    def selected(self, event):
        # Destroy previous widgets
        for widget in self.autoCreatedWidgets:
            widget.destroy()
        self.autoCreatedWidgets.clear()

        # Get Selection and generate widget to set preference
        self.currentPref = event.widget.get()
        if self.currentPref in men:
            prefl = women
            self.currentSex = 'Man'
            ordinal = [self.int2ordinal(i) for i in range(1, 1 + len(women))]
        else:
            prefl = men
            self.currentSex = 'Woman'
            ordinal = [self.int2ordinal(i) for i in range(1, 1 + len(men))]

        ordinal.append("--")
        for index, human in enumerate(prefl):
            l = Label(self.frame, text="I choose " + human + " as my ")
            l.grid(row=index+1, sticky=W)
            c = Combobox(self.frame, values=ordinal)
            c.grid(row=index+1, column=1)
            self.autoCreatedWidgets.append(l)
            self.autoCreatedWidgets.append(c)

    def add_pref(self):
        pref_str = ['_' for _ in range(len(men))]
        pref_int = [-1 for _ in range(len(men))]
        index = 0
        for widget in self.autoCreatedWidgets:
            if 'label' not in str(widget).split(".")[-1]:
                choose = self.ordinal2int(widget.get())
                if self.currentSex == 'Man':
                    index_current_pref = men.index(self.currentPref)
                else:
                    index_current_pref = women.index(self.currentPref)
                if self.currentSex == 'Man' and choose > -1:
                    pref_str[choose] = women[index]
                    pref_int[choose] = index
                elif self.currentSex == 'Woman' and choose > -1:
                    pref_str[choose] = men[index]
                    pref_int[choose] = index
                index += 1
        update_global_pref({index_current_pref: list(filter(lambda x: x >= 0, pref_int))}, self.currentSex)
        self.update_pref_box()

    def update_pref_box(self):
        self.pref_box.delete(0, END)
        for key in p['women']:
            prefs = [men[x] for x in p['women'][key]]
            line = women[key] + ': ' + str(prefs)
            self.pref_box.insert(END, line)

        for key in p['men']:
            prefs = [women[x] for x in p['men'][key]]
            line = men[key] + ': ' + str(prefs)
            self.pref_box.insert(END, line)

    def solve(self):
        res = solve(p)
        messagebox.showinfo("Results of matching", str(res))

    @staticmethod
    def int2ordinal(num):
        num = str(num)
        if len(num) > 2:
            end_digits = int(num) % 100
        else:
            end_digits = int(num) % 10
        if end_digits == 1:
            return (num + "st")
        if end_digits == 2:
            return (num + "nd")
        if end_digits == 3:
            return (num + "rd")
        else:
            return (num + "th")

    @staticmethod
    def ordinal2int(ordinal):
        if ordinal and ordinal != "--":
            ordinal = ordinal.replace("st", "").replace("nd", "").replace("rd", "").replace("th", "")
        else:
            return -1
        return int(ordinal) - 1
