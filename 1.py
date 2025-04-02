for x in range(2042,1,-1):
    n = 25**61 + 5**178 - x
    nf = ''
    while n > 0:
        nf+= str(n%5)
        n = n // 5
        
    if nf.count('0') == 60:
        print(x)
        break
        
    
    
