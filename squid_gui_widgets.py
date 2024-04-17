from tkinter import *
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from friend_connections import Friend_Connection

class FC_Widget:
    def __init__(self, mainframe, window):
        self.fc = Friend_Connection()
        self.mainframe = mainframe
        self.window = window

    def refresh_window(self):
        self.window.update()
        self.window.update_idletasks()
    
    def add_person(self, mf_column, mf_row):
        self.mainframe_add_person = ttk.Frame(self.mainframe, relief=SOLID, padding=10)
        ttk.Label(self.mainframe_add_person,text="Enter the name of the new person:",justify=RIGHT).grid(column=0,row=0,columnspan=2,sticky="EW")

        #Lable to describe input.
        ttk.Label(self.mainframe_add_person,text="New person's name is ").grid(column=0,row=1,sticky="EW")

        # Field to input name.
        name = StringVar()
        name_entry = ttk.Entry(self.mainframe_add_person,textvariable=name)
        name_entry.grid(column=1,row=1,sticky="EW")

        # Button to confirm and add the name.
        ttk.Button(self.mainframe_add_person,text="Confirm",command=lambda: self.fc.add_new_person(name.get())).grid(column=0,row=2,columnspan=2,sticky="EW")

        self.mainframe_add_person.grid(column=mf_column,row=mf_row,sticky=NW,padx=5,pady=5)

    def _refresh_name_list(self, list_index):
        if list_index == 0:
            friend_list = self.fc.return_friends()
        elif list_index == 1:
            friend_list = self.fc.return_friend_connections()
        elif list_index == 2:
            friend_list = self.fc.return_highest_friend_count()
        elif list_index == 3:
            friend_list = self.fc.return_isolated()
            
        num_name = len(friend_list)
        if num_name == 0:
            friend_list_str = "None!"
        elif num_name == 1:
            friend_list_str = friend_list_str = f'1. {friend_list[0]}'
        else:
            friend_list_str = f'1. {friend_list[0]}'
            for num in range(1,num_name):
                friend_list_str += f'\n{num+1}. {friend_list[num]}'
        return friend_list_str

    def name_list(self, mf_column, mf_row, mf_rowspan, list_index, title):
        self.mainframe_name_list = ttk.Frame(self.mainframe, relief=SOLID, padding=10, width=225)

        ttk.Label(self.mainframe_name_list,text=title,justify=LEFT).grid(column=0,row=0,sticky="EW")

        name_box = ttk.Label(self.mainframe_name_list,relief=SUNKEN, background="white")
        
        ttk.Button(self.mainframe_name_list,text="Refresh!",command=lambda: name_box.configure(text=self._refresh_name_list(list_index))).grid(column=1,row=0,sticky="E")
        
        name_box.grid(column=0,row=1,columnspan=2,sticky=NSEW,padx=5,pady=5)
        
        self.mainframe_name_list.grid(column=mf_column,row=mf_row,rowspan=mf_rowspan,sticky=NSEW,padx=5,pady=5)
        self.mainframe_name_list.grid_propagate(False)
        self.mainframe_name_list.columnconfigure(0,weight=1)
        self.mainframe_name_list.columnconfigure(1,weight=1)
        self.mainframe_name_list.rowconfigure(1,weight=1)
    
    def _plot_fc(self):
        # Code from https://networkx.org/documentation/stable/auto_examples/drawing/plot_weighted_graph.html        
        G = nx.Graph()
        print(self.fc.return_friend_connections())

        for person in self.fc.return_friends():
            G.add_node(person)

        for connection in self.fc.return_friend_connections():
            G.add_edge(connection[0], connection[1], weight=connection[2])

        avg_weight = self.fc.return_average_weight()
        elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > avg_weight]
        esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= avg_weight]

        pos = nx.spring_layout(G, seed=1)

        # nodes
        nx.draw_networkx_nodes(G, pos, node_size=700)

        # edges
        nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
        nx.draw_networkx_edges(
            G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
        )

        # node labels
        nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
        # edge weight labels
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels)

        ax = plt.gca()
        ax.margins(0.08)
        plt.axis("off")
        plt.tight_layout()
        plt.show()
    
    def fc_graph(self, mf_col, mf_row, mf_col_span):
        self.mainframe_graph = ttk.Frame(self.mainframe, relief=SOLID, padding=10)

        butt = ttk.Button(self.mainframe_graph,text="Generate!",command=self._plot_fc())
        butt.grid(column=1,row=0,sticky=E)

        self.mainframe_graph.grid(column=mf_col,row=mf_row,colspan=mf_col_span,sticky=EW,padx=5,pady=5)

    def connect_friends(self, mf_col, mf_row):
        self.mainframe_connect_friends = ttk.Frame(self.mainframe, relief=SOLID, padding=10)

        ttk.Label(self.mainframe_connect_friends,text="Connect some friends!",justify=LEFT).grid(column=0,row=0,columnspan=4,sticky=EW)
        ttk.Label(self.mainframe_connect_friends,text="Refer to the name list for the numbers.",justify=LEFT).grid(column=0,row=1,columnspan=4,sticky=EW)

        ttk.Label(self.mainframe_connect_friends,text="Connecting",justify=LEFT).grid(column=0,row=2,sticky=W)
        ttk.Label(self.mainframe_connect_friends,text="and",justify=LEFT).grid(column=2,row=2)
        index1 = IntVar()
        index2 = IntVar()
        weight = IntVar()
        ttk.Entry(self.mainframe_connect_friends,textvariable=index1,width=2).grid(column=1,row=2,sticky=EW)
        ttk.Entry(self.mainframe_connect_friends,textvariable=index2,width=2).grid(column=3,row=2,sticky=EW)
        ttk.Entry(self.mainframe_connect_friends,textvariable=weight,width=2).grid(column=2,row=3,columnspan=2,sticky=EW)
        ttk.Label(self.mainframe_connect_friends,text="with strength (weight) of . . .").grid(column=0,row=3,columnspan=2,sticky=W)

        ttk.Button(self.mainframe_connect_friends,text="Confirm",command=lambda: self.fc.connect_friends(index1.get(),index2.get(),weight.get())).grid(column=0,row=4,columnspan=4,sticky=EW)

        self.mainframe_connect_friends.columnconfigure(0,weight=0)
        self.mainframe_connect_friends.columnconfigure(1,weight=1)
        self.mainframe_connect_friends.columnconfigure(2,weight=0)
        self.mainframe_connect_friends.columnconfigure(3,weight=1)

        self.mainframe_connect_friends.grid(column=mf_col,row=mf_row,sticky=NSEW,padx=5,pady=5)

    def connections_list(self, mf_column, mf_row, mf_rowspan):
        self.mainframe_connect_list = ttk.Frame(self.mainframe, relief=SOLID, padding=10, width=225)

        ttk.Label(self.mainframe_connect_list,text="Connected to...",justify=LEFT).grid(column=0,row=0,sticky="EW")

        name_box = ttk.Label(self.mainframe_connect_list,relief=SUNKEN, background="white")
        
        ttk.Button(self.mainframe_connect_list,text="Refresh!",command=lambda: name_box.configure(text=self._refresh_connections_list())).grid(column=1,row=0,sticky="E")
        
        name_box.grid(column=0,row=1,columnspan=2,sticky=NSEW,padx=5,pady=5)
        
        self.mainframe_connect_list.grid(column=mf_column,row=mf_row,rowspan=mf_rowspan,sticky=NSEW,padx=5,pady=5)
        self.mainframe_connect_list.grid_propagate(False)
        self.mainframe_connect_list.columnconfigure(0,weight=1)
        self.mainframe_connect_list.columnconfigure(1,weight=1)
        self.mainframe_connect_list.rowconfigure(1,weight=1)

    def _refresh_misc_info(self):
        new_data =  [self.fc.return_total_number_of_friendships(),
                     self.fc.return_highest_friend_count(),
                     self.fc.return_isolated(),
                     self.fc.return_average_weight()]
        
        
    def show_misc_info(self, mf_col, mf_row):
        self.mainframe_show_misc_info = ttk.Frame(self.mainframe, relief=SOLID, padding=10)
        self.mainframe_show_misc_info.columnconfigure(0,weight=1)

        # data_list = [total friends, most popular, isolated, average weight]
        data_list = [self.fc.return_total_number_of_friendships(),self.fc.return_highest_friend_count(),
                self.fc.return_isolated(),self.fc.return_average_weight()]

        ttk.Label(self.mainframe_show_misc_info,text="Misc. Information",justify=LEFT).grid(column=0,row=0,sticky=EW)
        ttk.Label(self.mainframe_show_misc_info,text="Total number of friendships:").grid(column=0,row=1,sticky=EW)
        ttk.Label(self.mainframe_show_misc_info,text="Most popular person(s):").grid(column=0,row=2,sticky=EW)
        ttk.Label(self.mainframe_show_misc_info,text="Isolated person(s):").grid(column=0,row=3,sticky=EW)
        ttk.Label(self.mainframe_show_misc_info,text="Average weight:").grid(column=0,row=4,sticky=EW)
        
        ttk.Label(self.mainframe_show_misc_info,text=data_list[0]).grid(column=1,row=1,sticky=EW)
        ttk.Label(self.mainframe_show_misc_info,text=data_list[1]).grid(column=1,row=2,sticky=EW)
        ttk.Label(self.mainframe_show_misc_info,text=data_list[2]).grid(column=1,row=3,sticky=EW)
        ttk.Label(self.mainframe_show_misc_info,text=data_list[3]).grid(column=1,row=4,sticky=EW)

        ttk.Button(self.mainframe_show_misc_info,text="Refresh!").grid(column=1,row=0,sticky=E)

        self.mainframe_show_misc_info.grid(column=mf_col,row=mf_row,sticky=NSEW,padx=5,pady=5)