# Example 1

# create variables of different data types and then
# print the variables names, data types and values,

a= "His name is " # string
b= "Plotina " # string
c= a+b
print (f"a:{type(a)} {a}")
print(f"b:{type (b)} {b}")
print(f"c:{type(c)} {c}")
print()

d= False # boolean
e= True # boolean
print(f"d:{type(d)} {d}")
print(f"e: {type(e)} {e}")
print()

f= 15 #int
g= 7.62 #float
h= f+g # plus float makes float
print(f"f:{type(f)} {f}")
print(f"g:{type(g)} {g}")
print(f"h: {type (h)} {h}")
print()

i = "True" # string because of the surrounding quotes
j:"2.718" #string because of the surrounding quotes
print(f"i: {type(i)} {i}")
print(f"j: {type(j)} {j}")