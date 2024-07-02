##x=str(5)
##print(x)
##print(type(x))
##x=int(input("enter a number"))
##print(type(x))
#create
##my_set={"jai"}

##print(len(my_set))

##my_set=set((1,2,3,4))
##
##print(type(my_set))


##my_set={1,2,3,4,5,6,"jai","jkjhdf","asghs",True,False,0}
##print(my_set)

#access
##for i in my_set:
##    print(i)

#add item

##my_set={1,2,3,4}
##
##my_set.add(7)
##
##print(my_set)

#update two sets
##my_set={1,2,3,4}
####new_set={4,5,6,7}
####my_set.update(new_set)
####print(my_set)
##my_list=[8,5,6,7,8]
##my_set.update(my_list)
##print(my_set)


#remove

##my_set={1,2,3,4}
##my_set.discard(5)
##print(my_set)

#join two sets
##my_set={1,2,3,4}
##new_set={4,5,6,7}
##
##my_new2=my_set | new_set
##print(my_new2)

##x = {"a", "b", "c"}
##y = (1, 2, 3)
##m=[6,7,8]
##z = x.union(y,m)
##print(z)

my_set={1,2,3}
my_new_set={1,2,4,5}

my_set.difference_update(my_new_set)
print(my_set)















