def f(x,y,a):
    return (x&a==0) <= ((x & 77 == 0) and (x & 44 == 0))
for a in range(200):
    if all(f(x,y,a) for x in range(200) for y in range(200)) == 1:
        print(a)
        break