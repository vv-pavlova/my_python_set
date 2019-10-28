
from MySet import MySet


#v = MySet()

v = MySet('one', 'two', 'one', 'three', 'three', 8, 99, 99, 120 )

#v.create_set('one', 'two', 'one', 'three', 'three', 8, 99, 99, 120 )
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


print ( v.has('one') )
v.del_value('one')
print ( v.has('one') )

v.del_value('two')
v.add_value(None)

print ( v.has('None') )
print ( v.has(None) )



print()
print(v.for_storage)
print(v.print_set())
print ( v.count_values , len(v.for_storage), v.balance_index)




vvv = MySet()
vvv.create_set(None,None,None)

print()
print(vvv.for_storage)
print(vvv.print_set())
print ( vvv.count_values , len(vvv.for_storage), vvv.balance_index)

print ( vvv.has(4) )

