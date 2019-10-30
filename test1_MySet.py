
from MySet import MySet


v = MySet()

v.create_set(2, 2, 4, 4, 6, 5, 17, 28)
print(v.storage)
print ( v.count_values_in_storage , len(v.storage), v.rebalance_index)

v.add_value(77)
v.add_value(99)
v.add_value(99)
v.del_value(77)
v.add_value(77)
v.add_value(99)
v.del_value(77)
v.del_value(2)
v.add_value(121)
v.del_value(121)
v.add_value(121)
v.del_value(121)
v.add_value(121)
v.del_value(121)
v.add_value(121)
v.del_value(121)
v.add_value(121)
v.add_value(77)


print()
print(v.storage)
print(v.print_set())
print ( v.count_values_in_storage , len(v.storage), v.rebalance_index)


v.del_value(77)
v.add_value(77)
v.del_value(77)
v.add_value(77)
v.del_value(77)
v.del_value(121)
v.del_value(99)
v.del_value(4)
v.del_value(510)
v.del_value(5)
v.del_value(510)
v.del_value(28)
v.del_value(6)

print()
print(v.storage)
print(v.print_set())
print ( v.count_values_in_storage , len(v.storage), v.rebalance_index)