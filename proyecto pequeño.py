print("=====================")
print("LEY DE OMH")
print("=====================")
print("MENU PRINCIPAL")    
def calculo_resistencia(voltaje,corriente):
        resistencia = voltaje / corriente
        return resistencia
def calculo_voltaje(resistencia,corriente):
        voltaje = corriente * resistencia
        return voltaje
def calculo_corriente(voltaje,resistencia):
        corriente = voltaje / resistencia
        return corriente
programa_activo = True
while programa_activo:
    opciones = ["1 resistencia", "2 corriente", "3 voltaje"]
    print(opciones)
    seleccion_de_opciones = int(input("selecciona el numero de la opcion deseada: "))
    if seleccion_de_opciones == 1:
        print("Ingresa los datos que se te piden")
        voltaje = float(input("Ingresa el volje en voltios: "))
        corriente = float(input("Ingresa la corriente en amperios: "))
        if corriente == 0:
              print("la operacion no se puede realizar")
        else:
            resultado_resistencia = calculo_resistencia(voltaje,corriente)
            print(resultado_resistencia, "oms's")
    elif seleccion_de_opciones == 2:
        print("Igrese los datos que se le piden")
        voltaje = float(input("ingresa el voltaje en voltios: "))
        resistencia = float(input("Ingresa la resistencia en omh's: "))
        if resistencia == 0:
             print("La operacion no se puede realizar")
        else:
            resultado_corriente = calculo_corriente(voltaje,resistencia)
            print(resultado_corriente, "ampers")
    elif seleccion_de_opciones == 3:
        print("Ingrese los datos que se le piden")
        corriente = float(input("ingrese la corriente en ampers: "))
        resistencia = float(input("Ingrese la resistencia en omh's: "))
        resultado_voltaje = calculo_voltaje(resistencia,corriente)
        print(resultado_voltaje)
    else:
        print("la opcion seleccionada no existe")