def calculadora():
  while True:
    print("Seleccione la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
#editando desde repositorio
    opcion = input("Ingrese su opción (1/2/3/4/5): ")

    if opcion == '5':
      break

    try:
      num1 = float(input("Ingrese el primer número: "))
      num2 = float(input("Ingrese el segundo número: "))

      if opcion == '1':
        resultado = num1 + num2
      elif opcion == '2':
        resultado = num1 - num2
      elif opcion == '3':
        resultado = num1 * num2
      elif opcion == '4':
        if num2 == 0:
          print("No se puede dividir por cero.")
        else:
          resultado = num1 / num2
      else:
        print("Opción inválida.")

      print("El resultado es:", resultado)

    except ValueError:
      print("Por favor, ingrese solo números.")

if __name__ == "__main__":
  calculadora()
