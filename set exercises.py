#create rose garden
rose_garden={"red rose","wite rose","yellow rose"}
print(rose_garden)

#2.add pink rose to rosegarden
rose_garden.add("pink rose")
print(rose_garden)

#3.removing yellow rose
rose_garden.remove("yellow rose")
print(rose_garden)

#4.create botanical_garden
botanical_garden={"sun flower","tulip","red rose"}
print(botanical_garden)

#5.intersection of rose_garden and botanical_garden
common_flowers=rose_garden.intersection(botanical_garden)
print(common_flowers)

#6.difference between rose_garden and botanical_garden
flowers_only_in_rose_garden=rose_garden.difference(botanical_garden)
print(flowers_only_in_rose_garden)

#7.symmetric difference between rose garden and botanical garden
flowers_only_in_rose_garden=rose_garden.symmetric_difference(botanical_garden)
print(flowers_only_in_rose_garden)

#8.use len() function to find no of elements in rose_garden
print(len(rose_garden))

#9.use discard metod to remove pink rose from rose garden
rose_garden.discard("pink rose")
print(rose_garden)

#10.create small garden
small_garden={"red rose","wite rose"}
print(small_garden)
print(rose_garden)
flowers_only_in_subset_of_small_garden=small_garden.issubset(rose_garden)
print(flowers_only_in_subset_of_small_garden)

#11.ceck rose_garden is superset of small garden
flowers_in_superset_of_small_garden=rose_garden.issuperset(small_garden)
print(flowers_in_superset_of_small_garden)

#12.use clear metod remove rose_garden_set
print(rose_garden.clear())

#13.copy() metod for botanical_garden
print(botanical_garden.copy())
print(botanical_garden)
botanical_garden.add("lilly")
print(botanical_garden)

#14.create frozen set
immutable_garden={"orcid","daisy","red rose"}
a=frozenset(immutable_garden)
print(a)


#15.iterate over te botanical_garden set
for val in botanical_garden:
    print(val)

#ceck if sunflower is in te botanical_garden
is_sunflower_in_botanical_garden="sunflower" in botanical_garden
print("sunflower in botanical garden",is_sunflower_in_botanical_garden)

if "sun flower" in botanical_garden:
    print("true")
else:
    print("false")

#intersection update() metod to update botanical_garden set wit oly elements in rose
#rose_garden
botanical_garden={"rose","tulip","orcid"}
rose_garden={"rose","ibiscus","tulip"}
print(rose_garden)
print(botanical_garden)
only_elements_in_botanical_garden=botanical_garden.intersection_update(rose_garden)
print("only elements in botanical garden",only_elements_in_botanical_garden)
print(botanical_garden)

#use differenceupdate metod to remove all elements in small_garden from botanical_garden
unique_elements_in_small_garden=small_garden.difference_update(botanical_garden)
print(unique_elements_in_small_garden)
print(small_garden)
print(botanical_garden)

#even numbers in 1to 10
even_numbers={num for num in range(1,10) if num%2==0}
print(even_numbers)

#remove duplicates
flowers=["rose","tulip","daisy","tulip"]
unique_flowers=set(flowers)
print("unique flowers",unique_flowers)