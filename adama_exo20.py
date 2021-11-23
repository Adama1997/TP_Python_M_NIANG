def ppmc(a,b):
    p=a*b
    while(a!=b):
        if(a<b):
            b-=a
        else:
            a-=b
    return p/a
