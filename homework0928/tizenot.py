szam1 = float(input("Kérem adjon meg egy számot"))

szam2 = float(input("Kérem adjon meg egy számot"))

szam3 = float(input("Kérem adjon meg egy számot"))



if szam1 > szam2 and szam2 < szam3:
    print(szam2)

elif szam3 < szam1 and szam1 < szam2:
    print(szam1)

else: szam2 > szam3 and szam1 > szam2
    print(szam3)