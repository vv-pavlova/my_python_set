class MySet:
    def __init__(self):
        self.for_storage = [];
        self.temp_storage = [];
        self.cell_num = None;
        self.cell_num_start = None;
        self.count_values = 0;
        self.balance_index = 1;
        self.fl_exit = False;

    def rebalancing_set(self):
        self.temp_storage = self.for_storage
        if self.balance_index >= 0.7:
            self.for_storage = [None] * len(self.for_storage) * 2
            self.count_values = 0
        else:
            self.for_storage = [None] * round ( len(self.for_storage) / 2 + 1 )
            self.count_values = 0
        for i in range(len(self.temp_storage)):
            if ( self.temp_storage[i] != None
                and self.temp_storage[i] != [None,None] ):
                self.add_value(self.temp_storage[i])

    def add_value(self, v_val):
        self.cell_num = hash(v_val) % len(self.for_storage)
        self.cell_num_start = hash(v_val) % len(self.for_storage)
        self.fl_exit = False
        while (True):
            if self.for_storage[self.cell_num] == None:
                self.for_storage[self.cell_num] = v_val
                self.count_values += 1
                self.balance_index = self.count_values/len(self.for_storage)
                if self.balance_index >= 0.7:
                    self.rebalancing_set()
                break
            elif self.for_storage[self.cell_num] == v_val:
                break
            else:
                self.cell_num = (self.cell_num + 1)%len(self.for_storage)
                if self.cell_num == self.cell_num_start:
                    while (True):
                        if self.for_storage[self.cell_num] == [None,None]:
                            self.for_storage[self.cell_num] = v_val
                            self.count_values += 1
                            self.balance_index = self.count_values / len(self.for_storage)
                            if self.balance_index >= 0.7:
                                self.rebalancing_set()
                            self.fl_exit = True
                            break
                        elif self.for_storage[self.cell_num] == v_val:
                            self.fl_exit = True
                            break
                        else:
                            self.cell_num = (self.cell_num + 1) % len(self.for_storage)
                    if (self.fl_exit):
                        break

    def del_value(self, v_val):
        self.cell_num = hash(v_val) % len(self.for_storage)
        self.cell_num_start = hash(v_val) % len(self.for_storage)
        while (True):
            if self.for_storage[self.cell_num] == v_val:
                self.for_storage[self.cell_num] = [None,None]
                self.count_values -= 1
                self.balance_index = self.count_values/len(self.for_storage)
                if self.balance_index <= 0.3:
                    self.rebalancing_set()
                break
            elif self.for_storage[self.cell_num] == None:
                break   # число не нашли
            else:
                #break
                self.cell_num = (self.cell_num + 1)%len(self.for_storage)
                if self.cell_num == self.cell_num_start:
                    break   # число не нашли

    def create_set(self, *v_set):
        self.for_storage = [None] * 11
        for i in range(len(v_set)):
            self.add_value(v_set[i])

    def clear_set(self):
        self.for_storage = []

    def print_set(self):
        return( [x for x in self.for_storage if x != None and x != [None,None]] )
