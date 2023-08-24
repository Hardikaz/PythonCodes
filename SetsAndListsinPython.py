#Graded Lab 1 Artificial Intelligence
thisIsAset={"One1","Two2","Three3","Four4"}

print("This is my initial Set ")
print(thisIsAset)

#Adding a new element
print("Adding a new element in a set")
thisIsAset.add("Five5")
print("This is our new set")
print(thisIsAset)

#Deleting a new element
print("Deleting an element from a set")
thisIsAset.remove("One1")
print("Deleted an element from the set")
print(thisIsAset)

# print("Merging a new data type in out set")
# thisIsAset.add(44)

#Merging of two same data types
print("Merging same data types")
print("Declaring a new set")
newSet={"AppleA","BananaB","CatC","DogD"}
print("This is our new set")
print(newSet)
print("Merging two data types")
mergedSet=thisIsAset.union(newSet)
print(mergedSet)

#Mutationg a set
#Converting set into list
list=list(thisIsAset)
print(list)
print("Changing the elements of initial set")

list[2]="Mutated"

thisIsAset=set(list)
print(thisIsAset)

"""Sets can be changed but the elements are unmutable
so we convert them first in list and then we mutate it 
and then we again convert it to set by this method we can mutate sets"""



 
