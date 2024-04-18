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

nl1 = fcwidget.name_list(1,0,2,"Currently, there are...")
nl2 = fcwidget.name_list(2,0,2,"Connected to...")
root.columnconfigure(1, weight=1)

fcwidget.connect_friends(0,1)
root.rowconfigure(1, weight=1)

#fcwidget.connections_list(2,0,3)

tfl, awl = fcwidget.show_misc_info(0,2)
nl3 = fcwidget.name_list(1,2,2,"Most popular:")
nl4 = fcwidget.name_list(2,2,2,"In isolation:")
root.rowconfigure(2, weight=1)

fcwidget.import_label_list([nl1,nl2,nl3,nl4,tfl,awl])

fcwidget.graph_generate(0,3)

root.resizable(width=False, height=False)
root.iconbitmap(default="icon.ico")
root.mainloop()