perinba_garden={"rose","marigold","ibiscus"}
print(perinba_garden,type(perinba_garden))

#adding flowers
perinba_garden.add("lilly")
perinba_garden.add("mullai")
print(perinba_garden)

#adding tuplicate flower
perinba_garden.add("rose")
print(perinba_garden)

#removing flowers
perinba_garden.remove("marigold")
print(perinba_garden)

#cecking flower types
is_rose_in_perinba_garden="rose" in perinba_garden
print(is_rose_in_perinba_garden)
is_marigold_in_perinba_garden="marigold" in perinba_garden
print(is_marigold_in_perinba_garden)

#comparing wit anoter garden
jasmine_garden={"jasmine","rose","lotus"}
print(jasmine_garden)
print(perinba_garden)

#intersection
common_flowers=perinba_garden.intersection(jasmine_garden)
print(common_flowers)

#difference
flowers_only_in_perinba_garden=perinba_garden.difference(jasmine_garden)
print(flowers_only_in_perinba_garden)

#union
all_flowers_in_perinba_garden=perinba_garden.union(jasmine_garden)
print(all_flowers_in_perinba_garden)
