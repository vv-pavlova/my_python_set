class MySet:
    def __init__(self, *v_set):
        self.storage = []
        self.temp_storage = []
        self.count_values_in_storage = 0
        self.rebalance_index = 1
        self.min_length = 11
        self.fl_rebalance = True

        self.storage = [None] * self.min_length
        for i in range(len(v_set)):
            self.add_value(v_set[i])

    def get_index(self, v_value):
        return ( hash(v_value) % len(self.storage) )

    def rebalancing_set(self):
        if (self.fl_rebalance):
            self.rebalance_index = self.count_values_in_storage / len(self.storage)

            if self.rebalance_index >= 0.7:
                self.temp_storage = self.storage
                self.count_values_in_storage = 0
                self.storage = [None] * len(self.storage) * 2
                self.fl_rebalance = False
                for i in self.temp_storage:
                    if (i != None and i != [None, 0]):
                        self.add_value(i[0])
                self.fl_rebalance = True

            elif self.rebalance_index <= 0.3 and len(self.storage) > self.min_length:
                self.temp_storage = self.storage
                self.count_values_in_storage = 0
                self.storage = [None] * round ( len(self.storage) / 2 + 1 )
                self.fl_rebalance = False
                for i in self.temp_storage:
                    if (i != None and i != [None, 0]):
                        self.add_value(i[0])
                self.fl_rebalance = True

    def add_value(self, v_value):
        index = exit_index = self.get_index(v_value)
        if (self.has(v_value)):
            return
        else:
            while (True):
                if self.storage[index] == None:
                    self.storage[index] = [v_value,1]
                    self.count_values_in_storage += 1
                    self.rebalancing_set()
                    break
                else:
                    index = (index + 1)%len(self.storage)
                    if index == exit_index:
                        while (True):
                            if self.storage[index] == [None,0]:
                                self.storage[index] = [v_value,1]
                                self.count_values_in_storage += 1
                                self.rebalancing_set()
                                break
                            else:
                                index = (index + 1) % len(self.storage)

    def del_value(self, v_value):
        index = exit_index = self.get_index(v_value)
        while (True):
            if self.storage[index] == [v_value,1]:
                self.storage[index] = [None,0]
                self.count_values_in_storage -= 1
                self.rebalancing_set()
                break
            elif self.storage[index] == None:
                break   # число не нашли
            else:
                index = (index + 1)%len(self.storage)
                if index == exit_index:
                    break   # число не нашли

    def create_set(self, *v_set):
        self.storage = [None] * self.min_length
        for i in range(len(v_set)):
            self.add_value(v_set[i])

    def has(self, v_value):
        index = exit_index = self.get_index(v_value)
        while (True):
            if self.storage[index] == [v_value,1]:
                return True
            elif self.storage[index] == None:
                return False
            else:
                index = (index + 1)%len(self.storage)
                if index == exit_index:
                    return False

    def clear_set(self):
        self.storage = []

    def print_set(self):
        return( [x[0] for x in self.storage if x != None and x != [None,0]] )