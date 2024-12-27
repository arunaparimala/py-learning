fruits=("apple","orange","banana")
print("fruits",fruits,"type is",type(fruits))

t=("apple","banana","cerry")
print(t[1])

t=(1,2,3)
a=t[0]
b=t[1]
c=t[2]
print("a", a)
print("b",b)
print("c",c)

t1=(1,2)
t2=(3,4)
concate_tuples=t1+t2
print(concate_tuples)

t="repeat"
trice=t*3
print(trice)

t=(1,2,3,2,2,4)
print(t.count(2))

t=("a","b","c","d")
print(t.index("c"))

t=("one","two","tree")
print(len(t))

t=(1,2,3,4)
is_5_present_t=5 in t
print(is_5_present_t)

t=(0,1,2,3,4,5)
t1=slice(2,4)
print(t[t1])

l_list=[1,2,3]
l_tuple=tuple(l_list)
print(l_tuple)

t=(5)
print("type is",type(t))

t=("parottasalna","is","good")
print(t[0])
print(t[1])
print(t[2])



l_list=[1,2,3]
l_tuple=tuple(l_list)
print(l_tuple)
t_tuple=(4,5,6)
t_list=list(t_tuple)
print(t_list)

d_dic={"one":1,"two":2}
print(d_dic.values)
d_tuple=tuple(d_dic)
print(d_tuple)

if "one1" in d_dic:
    print(d_dic["one"])

print(d_dic.get("dna"))

l=[1,2,3,4]
print(tuple(l))

word="ello"
ello_tuple=tuple(word)
print(ello_tuple)

def add(num:tuple):
    return(sum(num))
t=(1,2,3,3,5)
print(add(t))


grid={(0,0):"origin",(1,2):"point A"}
grid_tuple=tuple(grid)
print(grid_tuple)
print(grid)
