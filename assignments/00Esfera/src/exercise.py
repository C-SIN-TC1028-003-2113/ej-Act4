import math

def main():
    #escribe tu código abajo de esta línea
    print("Este programa calcula el área y el volumen de una esfera")

    radio = float(input("Dame el valor del radio: "))

    area = 4 * math.pi * math.pow(radio,2)
    volumen = (4/3) * math.pi * math.pow(radio,3)

    print(f"El area de la esfera es: {area}")
    print(f"El volumen de la esfera es: {volumen}")

    print("Termine...")
    
if __name__=='__main__':
    main()
