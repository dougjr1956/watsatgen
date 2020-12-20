
def archie(resWtr, phi, resTrue):
    print("Using a=1, m=2, n=2")
    formFact = 1/(phi**2)
    resWet = formFact * resWtr
    resFrac = resWet/resTrue
    wtrSat = (resFrac)**(1/2)
    return wtrSat

def humble(resWtr, phi, resTrue):
    print("Using a=0.62, m=2.15, n=2")
    formFact = 0.62/(phi**2.15)
    resWet = formFact * resWtr
    resFrac = resWet/resTrue
    wtrSat = (resFrac)**(1/2)
    return wtrSat

def custom(resWtr, phi, resTrue):
    a = float(input("a = "))
    m = float(input("m = "))
    n = float(input("n = "))
    print(f"Using a={a}, m={m}, n={n}")
    formFact = a/(phi**m)
    resWet = formFact * resWtr
    resFrac = resWet/resTrue
    wtrSat = (resFrac)**(1/n)
    return wtrSat

rw = float(input("Input water resistivity in ohm-m: "))
p = (float(input("Input porosity in percent: ")) / 100)
rt = float(input("Input true resistivity in ohm-m: "))

print("""Choose an equation for water saturation calculation:
1. Archie
2. Humble
3. Custom
Enter 1, 2, or 3
""")

eqChoice = int(input("> "))
if eqChoice > 3 or eqChoice < 1:
    print("Invalid Choice")
    print("Can you follow instructions??")


if eqChoice == 1:
    print("Archie equation")
    sw = archie(rw, p, rt)
    bvw = sw * p
    print("Archie water saturation (frac.) is: ", round(sw, 3))
    print("Bulk volume water is: ", round(bvw, 3))
elif eqChoice == 2:
    print("Humble equation")
    sw = humble(rw, p, rt)
    bvw = sw * p
    print("Humble water saturation (frac.) is: ", round(sw, 3))
    print("Bulk volume water is: ", round(bvw, 3))
elif eqChoice == 3:
    print("Custom equation, Enter a, m, n")
    sw = custom(rw, p, rt)
    bvw = sw * p
    print("Custom water saturation (frac.) is: ", round(sw, 3))
    print("Bulk volume water is: ", round(bvw, 3))
