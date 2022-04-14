lado = int(input("Ingrese el alto: "))

for i in range(1, lado + 1):
    if i == 1 or i == lado:
        print("* " * lado)
    else:
        print("* " + str("  " * (lado - 2)) + "*")