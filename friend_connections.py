class Friend_Connection:
    def __init__ (self):
        self.friend_list = []
        self.friend_connection_count_list = []
        self.friend_connection_list = []

    def add_new_person(self, name):
        self.friend_list.append(name)
        self.friend_connection_count_list.append(0)
    
    def print_all_people(self):
        print("Currently, there are...")
        [print(f"{index+1}.",self.friend_list[index]) for index in range(len(self.friend_list))]

    def connect_friends(self, index1, index2, weight):
        index1 -= 1
        index2 -= 1
        curr_size = len(self.friend_list)
        if (index1 >= 0 and index1 < curr_size) and (index2 >= 0 and index2 < curr_size) and (weight >= 0):
            self.friend_connection_list.append( (self.friend_list[index1], self.friend_list[index2], weight) )
            self.friend_connection_count_list[index1] += 1
            self.friend_connection_count_list[index2] += 1
            return 1
        else:
            return 0
    
    def print_all_connection(self):
        print("Currently, there are...")
        [print(f"{index+1}.",self.friend_connection_list[index]) for index in range(len(self.friend_connection_list))]

    def return_friends (self):
        return self.friend_list
    
    def return_friend_connections (self):
        return self.friend_connection_list

    def return_total_number_of_friendships(self):
        return len(self.friend_connection_list)

    def return_highest_friend_count(self):
        value_high = 0
        index_high = -1
        for total_connection in range(len(self.friend_connection_count_list)):
            if total_connection > value_high:
                value_high = self.friend_connection_count_list[total_connection]
                index_high = total_connection
        
        if index_high != -1:    return self.friend_list[index_high]
        else:                   return -1

    def return_isolated (self):
        isolated_list = []
        for index in range(len(self.friend_connection_count_list)):
            if self.friend_connection_count_list[index] == 0:
                isolated_list.append(self.friend_list[index])

    def return_average_weight(self):
        total = 0
        for weight in self.friend_connection_list:
            total += weight[2]
        return len(total/self.friend_connection_list)