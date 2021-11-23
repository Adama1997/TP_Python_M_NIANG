n=int(input("entrer le nombre: "))
nbrparfait=0
nd=0
for i in range(1,n+1):
    if n%i==0:
        nd+=1
if nd==n or nbrparfait>n:
    print(nbrparfait, "sont des nombres parfait")
