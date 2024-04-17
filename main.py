from tkinter import *
from tkinter import ttk
from squid_gui_widgets import FC_Widget

root = Tk()
root.title("Friendship Network Visualiser")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky="NSEW")

# New instance of FC_Widget
fcwidget = FC_Widget(mainframe, root)

# Place widgets on root
fcwidget.add_person(0,0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

fcwidget.name_list(1,0,2,0,"Currently, there are...")
fcwidget.name_list(2,0,2,1,"Connected to...")
root.columnconfigure(1, weight=1)

fcwidget.connect_friends(0,1)
root.rowconfigure(1, weight=1)

#fcwidget.connections_list(2,0,3)

fcwidget.show_misc_info(0,2)
fcwidget.name_list(1,2,1,2,"Most popular:")
fcwidget.name_list(2,2,1,3,"In isolation:")
root.rowconfigure(2, weight=1)

root.mainloop()