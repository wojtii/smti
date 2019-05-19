from tkinter import Tk, ttk, Label, BOTTOM, SUNKEN, X, W
from Frames.WomenAndMen import People
from Frames.Preferences import Preferences


def handle_tab_changed(event):
    selection = event.widget.select()
    tab = event.widget.tab(selection, "text")
    if tab == "Preferences list":
        preferences.update_screen()


# Main Window
window = Tk()
window.title("SMTI")
window.geometry('640x540')

# Menu Controls
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Women & Men')
tab_control.add(tab2, text='Preferences list')
people = People(tab1)
preferences = Preferences(tab2)

# Status Bar
status = Label(text="", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)
tab_control.bind("<<NotebookTabChanged>>", handle_tab_changed)

# Pack menu and loop window
tab_control.pack(expand=1, fill='both')
window.mainloop()