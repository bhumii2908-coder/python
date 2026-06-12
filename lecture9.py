# set 
# set is a collection of the uniqe element

# create a set
# value={1,2,34,5,67,8,9,0}
# print(value)
# print(type(value))

# emply_set
# value_empty_set=set()
# print(type(value_empty_set))

# you can convert list and tuple in set
value=set([3,45,6,7,7,88,8,9])
print(value)

# duplicate element ingore set
# v={1,2,3,3,4,4,5,5,6,6,6,7,8,8,9}
# print(v)

# basic set opreation
# adding and removing elements
# solve={1,3,5,6,7,9}
# solve.add(2)
# solve.add(4)
# solve.add(8)
# # solve.add(8)if you are repaet element it give all the elements back
# print(solve)

# removing element
# noise={1,2,3,4,5,6,7,8,9,0}
# noise.remove(1)
# noise.remove(3)
# noise.remove(5)
# noise.remove(7)
# noise.remove(9)
# print(noise)
# if elements are not present in set so it give error so avolid error use

# noise.discard(10)
# noise.discard(11)
# print(noise)

# pop element use to  first elementremove
# ross={1,2,3,4,5}
# ross.pop()
# print(ross)

# remove_element=ross.pop()
# print(remove_element)
# print(ross)

# clear all the elements
# kpop={1,2,3,4,5,6,7,8,9,0}
# kpop.clear()
# print(kpop)

# set membership test
# true and false
# void={1,2,3,4,5,6,7}
# print(4 in void)
# print(10 in void)
# print(7 in void)
# print(8 in void)

# mathmaticals opreations
# union=combain all the elements
# set1={1,2,3,4,5,6}
# set2={4,5,6,7,8,9}
# online=set1.union(set2)
# print(online)

# intersection=common element print
# set1={1,2,3,4,5,6}
# set2={4,5,6,7,8,9}
# offline=set1.intersection(set2)
# print(offline)

# # intersection_update =all opreation done then it update set1
# set1.intersection_update(set2)
# print(set1)

# diffrence
# set1={1,2,3,4,5,6}
# set2={4,5,6,7,8,9}
# summ=set1.difference(set2)
# print(summ)

# summ=set2.difference(set1)
# print(summ)

# symmetric difference=remove the common elemnts
# set1={1,2,3,4,5,6}
# set2={4,5,6,7,8,9}
# common=set1.symmetric_difference(set2)
# print(common)


# set.methods
# is subset/superset=all the common element present
set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}
sub=set1.issubset(set2)
print(sub)
sup=set1.issuperset(set2)
print(sup)


