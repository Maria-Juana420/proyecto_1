print("Bienvenido a tu calculadora de IMC")
print("Captura los datos que a continuacion se te piden ")

nombre = input("Cual es tu nombre: ")
apellido_Pa = input("Apellido paterno: ")
apellido_Ma = input("Apellido materno: ")
edad = int(input("¿Que edad tienes?: ")) 
peso = float(input("¿Cual es actualmente tu peso es kilogramos?: "))
talla = float(input("¿Cual es tu estatura en metros?: "))
calculo_Imc = peso / talla**2

print("Hola " + nombre)
print("Tienes " +str(edad) +  "años" )
print("Actualmente pesas " + str(peso) + "Kg")
print("Y mides " + str(talla) + "m")
print("Tu IMC es: " + str(calculo_Imc))

if calculo_Imc >= 0 and calculo_Imc <= 18.5 :
    print("Bajo de peso")
    print("Es necesario acudir con un especialista en Nutrición")
elif calculo_Imc >= 18.6 and calculo_Imc <= 24.9 :
    print("Peso Normal")
    print("Genial, estas dentro de tu peso ideal")
elif calculo_Imc >= 25.0 and calculo_Imc <= 29.9 :
    print("Sobrepeso")
    print("""¡OH OH! estas por arriba de tu peso ideal. 
    Intenta seguir una buena rutina de alimentación combinada con ejercicio""")       
elif calculo_Imc >= 30.0 and calculo_Imc <= 34.9 :
    print("Obesidad Grado I")
    print("""Acude con un especialista en Nutrición, 
    las consecuencias de la obesidad pueden ser mortales""")
elif calculo_Imc >= 35.0 and calculo_Imc <= 39.9 :
    print("Obesidad Grado II")
    print("""Acude con un especialista en Nutrición,
    las consecuencias de la obesidad pueden ser mortales""")
elif calculo_Imc >= 40.0:
    print("Obesidad Morbida Grado III")
    print("""¡¡¡Alerta!!! Acude de inmediato con un Especialista en Nutrición, 
    TU SALUD PODRIA ESTAR EN RIESGO.""")






