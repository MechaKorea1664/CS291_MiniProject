class Friend_Connection:
    def __init__ (self):
        self.friend_list = []
        self.friend_connection_count_list = []
        self.friend_connection_list = []

    def add_new_person(self, name):
        if (name == ""): return
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
            test_tuple = (self.friend_list[index1],self.friend_list[index2])
            self.friend_connection_list.append( (self.friend_list[index1], self.friend_list[index2], weight) )
            self.friend_connection_count_list[index1] += 1
            if index1 != index2:    
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
        if len(self.friend_connection_count_list) == 0: return []
        highest_list = []
        biggest = self.friend_connection_count_list[0]

        for num in range(len(self.friend_connection_count_list)):
            if self.friend_connection_count_list[num] > biggest:
                biggest = self.friend_connection_count_list[num]

        for num in range(len(self.friend_connection_count_list)):
            if self.friend_connection_count_list[num] == biggest:
                highest_list.append(self.friend_list[num])
            
        return highest_list

    def return_isolated (self):
        isolated_list = []
        for index in range(len(self.friend_connection_count_list)):
            if self.friend_connection_count_list[index] == 0:
                isolated_list.append(self.friend_list[index])
            elif self.friend_connection_count_list[index] == 1:
                target_name = self.friend_list[index]
                for connection in self.friend_connection_list:
                    if (connection[0] == connection[1] and connection[0] == target_name):  isolated_list.append(target_name)
                    else:                                                                   break
        return isolated_list

    def return_average_weight(self):
        total = 0
        if len(self.friend_connection_list) == 0: return 0
        for weight in self.friend_connection_list:
            total += weight[2]
        return total/len(self.friend_connection_list)
    
    def debug_return_all_info(self):
        for num in range(len(self.friend_list)):
            target_name = self.friend_list[num]
            print(f'{num+1}. {target_name}: num connection: {self.friend_connection_count_list[num]}, connections: [',end='')
            for connection in self.friend_connection_list:
                if connection[0] == target_name or connection[1] == target_name:
                    print(connection,end=', ')
            print(']')