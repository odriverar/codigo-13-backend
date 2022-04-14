dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
print(dias)
# print(dias[1])
# print(dias[1:2])
# dias.append("jueves")
# print(dias[1:3])
print("pop")
dias.pop()
print(dias)
dias[0] = "Sabado"
print(dias)

for dia in dias:
    print("Hoy es " + dia)