ahorro_inicial = 1000
deposito_mensual = 500
N = 2


def calcular_ahorro(mes, dinero):
    if mes == N:
        return dinero

    return calcular_ahorro(mes + 1, dinero + deposito_mensual)


ahorro_final = calcular_ahorro(0, ahorro_inicial)


print("===================================")
print("       CALCULADORA DE AHORRO")
print("===================================")
print("Ahorro inicial: $", ahorro_inicial)
print("Depósito mensual: $", deposito_mensual)
print("Número de meses (N):", N)
print("-----------------------------------")
print("Ahorro acumulado: $", ahorro_final)
print("===================================")
