
def diskriminant(a,b,c):
    
    a = float(a)
    b = float(b)
    c = float(c)
    D = b**2 - 4*a*c;
    if D>0:
        x1 = (-b + (D)**2)/(2*a);
        x2 = (-b - (D)**2)/(2*a);
        return ('X1: {} X2: {}'.format(x1,x2))

    elif D==0:
        x1 = -b/(2*a);
        return  ('X1=X2 : {}'.format(x1))
    else:
        print('Tənliyin həqiqi kökləri yoxdur..')
        
        

