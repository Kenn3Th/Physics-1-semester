from random import random #implementerer falsk/uekte-tilfeldige(pseudo-random) nummer

antfeil = 0; N = 10000
x0 = y0 = z0 = 0.0
feil1 = feil2 = 0.0

for i in range(N):
    x = random(); y = random(); #random() genererer et tilfeldig flyttall mellom [0.0,1.0)
    res1 = (x + y)*(x - y) #legger sammen og trekker fra de tilfeldige siffrene og multipliserer de
    res2 = x**2 - y**2 #kvadrerer begge de tilfeldige tallene ogsaa trekker i fra

    if res1 != res2: #hvis res1 ikke er det samme som res2
        antfeil += 1 #legger til 1 i antfeil
        x0 = x; y0 = y #x blir x0 og y blir y0
        feil1 = res1 #res1 blir feil1
        feil2 = res2 #res2 blir feil2

print (100. * antfeil/N) #100. multiplisert med antfeil/10000
print (x0, y0, feil1 - feil2) #skriver ut hva x og y var sist gang de var feil og differansen mellom res1 og res2
