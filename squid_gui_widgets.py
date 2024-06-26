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

    def import_label_list(self, lbl_lst):
        self.label_list = lbl_lst
    
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
        ttk.Button(self.mainframe_add_person,text="Confirm",
                   command=lambda: [self.fc.add_new_person(name.get()),
                                    name_entry.delete(0,END),
                                    self._refresh_name_list()]
                                    ).grid(column=0,row=2,columnspan=2,sticky="EW")

        self.mainframe_add_person.grid(column=mf_column,row=mf_row,sticky=NW,padx=5,pady=5)

    def _refresh_name_list(self):
        for index in range(4):
            if index == 0:
                friend_list = self.fc.return_friends()
            elif index == 1:
                friend_list = self.fc.return_friend_connections()
            elif index == 2:
                friend_list = self.fc.return_highest_friend_count()
            elif index == 3:
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
            
            self.label_list[index].configure(text=friend_list_str)
            self.label_list[4].configure(text=self.fc.return_total_number_of_friendships())
            self.label_list[5].configure(text=self.fc.return_average_weight())

    def name_list(self, mf_column, mf_row, mf_rowspan, title):
        self.mainframe_name_list = ttk.Frame(self.mainframe, relief=SOLID, padding=10, width=225)

        ttk.Label(self.mainframe_name_list,text=title,justify=LEFT).grid(column=0,row=0,sticky="EW")

        name_box = ttk.Label(self.mainframe_name_list,relief=SUNKEN, background="white")
        
        name_box.grid(column=0,row=1,columnspan=2,sticky=NSEW,padx=5,pady=5)
        
        self.mainframe_name_list.grid(column=mf_column,row=mf_row,rowspan=mf_rowspan,sticky=NSEW,padx=5,pady=5)
        self.mainframe_name_list.grid_propagate(False)
        self.mainframe_name_list.columnconfigure(0,weight=1)
        self.mainframe_name_list.columnconfigure(1,weight=1)
        self.mainframe_name_list.rowconfigure(1,weight=1)

        return name_box
    
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

        # Frame to contain input fields
        mainframe_input_field = ttk.Frame(self.mainframe_connect_friends)
        mainframe_input_field.columnconfigure(1,weight=1)
        mainframe_input_field.columnconfigure(3,weight=1)

        ttk.Label(mainframe_input_field,text="Connecting",justify=LEFT).grid(column=0,row=0,sticky=W)
        ttk.Label(mainframe_input_field,text="and ",justify=LEFT).grid(column=2,row=0)
        index1 = IntVar()
        index2 = IntVar()
        weight = IntVar()
        index1_entry = ttk.Entry(mainframe_input_field,textvariable=index1,width=2)
        index2_entry = ttk.Entry(mainframe_input_field,textvariable=index2,width=2)
        weight_entry = ttk.Entry(self.mainframe_connect_friends,textvariable=weight,width=2)
        index1_entry.grid(column=1,row=0,sticky=EW)
        index2_entry.grid(column=3,row=0,sticky=EW)
        weight_entry.grid(column=2,row=3,columnspan=2,sticky=EW)
        ttk.Label(self.mainframe_connect_friends,text="with strength (weight) of. . .").grid(column=0,row=3,columnspan=2,sticky=W)

        mainframe_input_field.grid(column=0,row=2,columnspan=4,sticky=EW)

        ttk.Button(self.mainframe_connect_friends,text="Confirm",
                   command=lambda: [self.fc.connect_friends(index1.get(),index2.get(),weight.get()),
                                    self._refresh_name_list(),
                                    index1_entry.delete(0,END),
                                    index2_entry.delete(0,END),
                                    weight_entry.delete(0,END)]
                                    ).grid(column=0,row=4,columnspan=4,sticky=EW)

        self.mainframe_connect_friends.columnconfigure(0,weight=0)
        self.mainframe_connect_friends.columnconfigure(1,weight=1)
        self.mainframe_connect_friends.columnconfigure(2,weight=0)
        self.mainframe_connect_friends.columnconfigure(3,weight=1)

        self.mainframe_connect_friends.grid(column=mf_col,row=mf_row,sticky=NSEW,padx=5,pady=5)

    def show_misc_info(self, mf_col, mf_row):
        self.mainframe_show_misc_info = ttk.Frame(self.mainframe, relief=SOLID, padding=10,height=77)
        self.mainframe_show_misc_info.columnconfigure(0,weight=1)

        ttk.Label(self.mainframe_show_misc_info,text="Misc. Information",justify=LEFT).grid(column=0,row=0,sticky=EW)
        ttk.Label(self.mainframe_show_misc_info,text="Total number of friendships:").grid(column=0,row=1,sticky=EW)
        ttk.Label(self.mainframe_show_misc_info,text="Average weight:").grid(column=0,row=2,sticky=EW)
        
        total_friendship_label  = ttk.Label(self.mainframe_show_misc_info,text=0,justify=RIGHT)
        average_weight_label    = ttk.Label(self.mainframe_show_misc_info,text=0,justify=RIGHT)
        total_friendship_label.grid(column=1,row=1,sticky=E)
        average_weight_label.grid(column=1,row=2,sticky=E)

        self.mainframe_show_misc_info.grid(column=mf_col,row=mf_row,sticky=NSEW,padx=5,pady=5)
        self.mainframe_show_misc_info.grid_propagate(False)

        return total_friendship_label, average_weight_label

    def graph_generate(self,mf_column,mf_row):
        self.graph_generate = ttk.Frame(self.mainframe, relief=SOLID, padding=10)

        ttk.Label(self.graph_generate,text="Visual Friendship Graph",justify=LEFT).grid(column=0,row=0,sticky=NSEW)
        ttk.Button(self.graph_generate,text="GENERATE!",command=lambda:self._plot_fc()).grid(column=0,row=1,sticky=NSEW)

        self.graph_generate.columnconfigure(0,weight=1)

        self.graph_generate.grid(column=mf_column,row=mf_row,sticky=NSEW,padx=5,pady=5)