weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == 'L':
    converted = weight * 0.45
    print(f"Ypu are {converted} Kilos")
else:
    converted = weight / 0.45
    print(f"Ypu are {converted} Pounds")
