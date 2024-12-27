moonar_trip=("boat ride","1-1-2024","kerala")
coci_trip=("wonde la","1-1-2024","koci")
cennai_trip=("zoo","10-10-2024","cennai")
print(moonar_trip[0])
print("moonar trip",moonar_trip,"-_type is",type(moonar_trip))

poto_album=(moonar_trip,coci_trip,cennai_trip)
print(poto_album)

print(moonar_trip)
location=moonar_trip[2]
date=moonar_trip[1]
description=moonar_trip[0]
print("location",location,"date",date,"description",description)

location,date,description=moonar_trip
print("location",location)
print("date",date)
print("description",description)
print(location,date,description)

combined_trip=moonar_trip+cennai_trip
print(combined_trip)

#repeating tuple
double_coci_trip=coci_trip*2
print(double_coci_trip)

is_moonar_trip_poto=moonar_trip  in poto_album
print("is moonar trip poto",is_moonar_trip_poto)

print(len(poto_album))

for val in coci_trip:
    print(val)

count=poto_album.count
print(count)

print(list(moonar_trip))

GFG_tuple=(cennai_trip,coci_trip,moonar_trip)
      
GFG_list=list(GFG_tuple)
print(GFG_list)