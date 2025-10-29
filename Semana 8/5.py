presupuesto = 1000
gasto = 0

while gasto < presupuesto:
    compra = float(input("Monto a comprar: "))
    gasto += compra
gasto-=compra
print("Ha llegado al limite del presupuesto")
print(f"El monto gastado es: ${gasto:,.2f}")