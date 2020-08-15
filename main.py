

#1
vlr_interes=float(input("Ingrese el precio de los intereses"))
vlr_cap=float(input("Ingrese la cantidad de dinero disponible"))
int=vlr_cap*vlr_interes
if int>7000:
    capTotal=vlr_cap+int
    print(f"el valor total de capital es: {capTotal}")
else:
    print(f"el valor total de capital es: {int}")

#2
nota1=float(input("Ingrese la primera nota"))
nota2=float(input("Ingrese la segunda nota"))
nota3=float(input("Ingrese la tercera nota"))
prom=(nota1+nota2+nota3)/3
if prom >=70:
    print("Aprobo")
else:
    print("Reprobo")



#3
compra=float(input("Digite el valor de la compra"))
if compra>1000:
    dscto=compra*0.20
else:
    dscto=0

totpag=compra-dscto
print(f"El total a pagar es: {totpag}")

#4
cantHw=float(input("Ingrese la cantidad de horas trabajadas"))
if cantHw>40:
    hextras=cantHw-40
    sal_semana=hextras*20 + 40*16
else:
    sal_semana=cantHw*16
print(f"El salario semanal es: $ {sal_semana}")



#6
num1=float(input("Digite el primer número"))
num2=float(input("Digite el segundo número"))
if num1<num2:
    print(f"{num1} {num2}")
else:
    print(f"{num2} {num1}")



nroCamisetas=float(input("Ingrese el número de camisetas"))
precio=float(input("Ingrese el precio de las camisetas"))
vlrCompra=nroCamisetas*precio
if nroCamisetas>=3:
    vlrTotal= vlrCompra-vlrCompra*0.2
else:
    vlrTotal= vlrCompra-vlrCompra*0.1
print(f"El total a pagar es: {vlrTotal}")




