def f1(x,y,w,z):
    return ((w or (not y)) <= ( z == x)) 
def f2(x,y,w,z):
    return ((w or (not y)) == ( x <= z))

for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                print(x,y,w,z,int(f1(x,y,w,z)),int(f2(x,y,w,z)))
