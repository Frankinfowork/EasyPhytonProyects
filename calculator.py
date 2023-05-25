# Calculadora básica:programa que solicite al usuario dos números
# y realice las operaciones básicas de suma, resta, multiplicación y división.

print("Dime que desea hacer, escriba el numero")
print("1. suma")
print("2. resta")
print("3. multiplicacion")
print("4 division")

respuesta = int(input())


print("Dime el primer numero")
number1 = int(input())
print("Dime el segundo numero")
number2 = int(input())

if respuesta == 1:
    result = number1+number2
    print(result)
elif respuesta == 2:
    result = number1-number2
    print(result)
elif respuesta == 3:
    result = number1*number2
    print(result)
elif respuesta == 4:
    result = number1/number2
    print(result)
else:
    print("opcion incorrecta")
