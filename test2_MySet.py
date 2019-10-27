
from MySet import MySet


v = MySet()

v.create_set('one', 'two', 'one', 'three', 'three', 8, 99, 99, 120 )
print(v.for_storage)
print ( v.count_values , len(v.for_storage), v.balance_index)

v.add_value('one')
v.add_value('twelve')
v.add_value('TWELVE')
v.del_value('twelve')
v.add_value('99')

print()
print(v.for_storage)
print(v.print_set())
print ( v.count_values , len(v.for_storage), v.balance_index)

v.del_value('one')
v.del_value('two')

print()
print(v.for_storage)
print(v.print_set())
print ( v.count_values , len(v.for_storage), v.balance_index)
