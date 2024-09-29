import statistics
import math

szam1 = float(input("Kérem adjon meg egy számot"))

szam2 = float(input("Kérem adjon meg egy számot"))

szam3 = float(input("Kérem adjon meg egy számot"))

#szam4 = (math.tan(szam1)+(szam2)+(szam3))
print(statistics.mean([szam1,szam2,szam3]))

