import networkx as nx
import matplotlib.pyplot as plt

class menu_template:
    def __init__(self):
        self.option_list = ""

    def _choice_prompt (self):
    # Returns a single digit integer, numeric choice.
        choice_num = input(">>> ")
        while len(choice_num) != 1 and not choice_num.isnumeric():
            print("Unknown choice!")
            choice_num = input(">>> ")
        return int(choice_num)
    
    def _print_options_with_choice_prompt (self):
        print("\n___________________________\n")
        print(self.option_list,end='\n\n')
        return self._choice_prompt()

    def _check_valid (self, max_num_options, user_choice):
        if not str(user_choice).isnumeric():
            return False
        elif int(user_choice) > 0 and int(user_choice) <= max_num_options: 
            return True
        else:
            print("Input invalid!")
            return False

import friend_connections as fc
class Friend_Connection_Menu (menu_template):
    def __init__(self):
        self.option_list = "Friend Connection Graph:\n \
    1. Add a person\n \
    2. Add a connection\n \
    3. See the list of persons\n \
    4. See the list of connections\n \
    5. View the graph\n \
    6. Exit"
        self.fc_inst = fc.Friend_Connection()
        
    def run_chosen_function_loop(self):
        choice = self._print_options_with_choice_prompt()
        while not self._check_valid(5,choice):
            choice = self._choice_prompt()
        
        while True:
            if choice is 1:
                new_name = input("What is their name? >>> ")
                self.fc_inst.add_new_person(new_name)
            
            elif choice is 2:
                self.fc_inst.print_all_people()
                num_pop = len(self.fc_inst.return_friends())

                person1 = input("Person 1 number >>> ")
                while not self._check_valid(num_pop, person1):
                    person1 = input("Person 1 number >>> ")
                
                person2 = input("Person 2 number >>> ")
                while not self._check_valid(num_pop, person2):
                    person2 = input("Person 2 number >>> ")

                weight = input ("Strength (weight) of friendship? >>> ")
                while not weight.isnumeric():
                    print ("Numbers only!")
                    weight = input ("Strength (weight) of friendship? >>> ")
                
                self.fc_inst.connect_friends(int(person1), int(person2), int(weight))
                print("Connection established!")
            
            elif choice is 3:
                self.fc_inst.print_all_people()

            elif choice is 4:
                self.fc_inst.print_all_connection()

            elif choice is 5:
                G = nx.Graph()
                print(self.fc_inst.return_friend_connections())

                for connection in self.fc_inst.return_friend_connections():
                    G.add_edge(connection[0], connection[1], weight=connection[2])

                elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
                esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]

                pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility
                
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
            
            elif choice is 6:
                pass
            else: break
            choice = self._print_options_with_choice_prompt()
            while not self._check_valid(6,choice):
                choice = self._choice_prompt()
        
        return (self.fc_inst.return_friends, self.fc_inst.return_friend_connections)