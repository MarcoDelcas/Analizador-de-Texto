"""
Este programa analizador texto el texto escrito por un input.
"""

#_*_ coding: utf8 _*_
#Created by MarcoDelCas

#Programa principal
if __name__ == '__main__':
    print("Bienvenido al analizador de texto")
    while True:
        #CODE
        texto = input("Ingrese el texto a analizar: ")
        vocales = ['a','e','i','o','u']
        texto.lower()
        lista_texto = texto.split(' ')
        texto_separado = list(texto)
        print (f"\nEl total de palabras que hay en el texto es: {len(lista_texto)}")
        print (f"El total de letras {vocales[0]} en el texto es: {texto.count(vocales[0])}")
        print (f"El total de letras {vocales[1]} en el texto es: {texto.count(vocales[1])}")
        print (f"El total de letras {vocales[2]} en el texto es: {texto.count(vocales[2])}")
        print (f"El total de letras {vocales[3]} en el texto es: {texto.count(vocales[3])}")
        print (f"El total de letras {vocales[4]} en el texto es: {texto.count(vocales[4])}")
       
        #MENU DE SALIDA
        print("\nMENU")
        print("1. Ingresar otro texto")
        print("2. Salir")
        respuesta_loop= input("¿Quieres ingresar otro texto a analizar? ")
        
        #VALIDACION SALIDA LOOP
        if(respuesta_loop == '1'):
            continue
        else:
            break
        
