
from MySet import MySet


v = MySet()

v.create_set(2, 2, 4, 4, 6, 5, 17, 28)
print(v.for_storage)
print ( v.count_values , len(v.for_storage), v.balance_index)

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
print(v.for_storage)
print(v.print_set())
print ( v.count_values , len(v.for_storage), v.balance_index)


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

print()
print(v.for_storage)
print(v.print_set())
print ( v.count_values , len(v.for_storage), v.balance_index)