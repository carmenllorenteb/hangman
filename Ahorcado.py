import random
import string

from Hangman.palabras import palabras
from Hangman.Ahorcado_diagrama import vidas_diccionario_visual  

def obtener_palabra_válida(palabras):
    # Selecionar una palabra al azar de la lista de palabras válidas.
    palabra = random.choice(palabras)

    if palabra:
        print(f"La palabra que te toca tiene {len(palabra)} letras.")

    return palabra.upper()

def ahorcado():

    print("======================================")
    print("¡Bienvenido(a) al juego del Ahorcado!")
    print("======================================")

    palabra = obtener_palabra_válida(palabras)

    letras_por_adivinar = set(palabra)
    letras_adivinadas = set() 
    abecedario = set(string.ascii_uppercase) 

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        # Determinar si usar "vida" o "vidas" y "queda" o "quedan"
        vida_texto = "vida" if vidas == 1 else "vidas"
        queda_texto = "queda" if vidas == 1 else "quedan"
    
        print(f"Te {queda_texto} {vidas} {vida_texto} y has usado estas letras: {' '.join(letras_adivinadas)}")
        # Mostrar el estado actual de la palabra
        palabra_lista = [letra if letra in letras_adivinadas else '_' for letra in palabra]
        # Mostrar el estado del ahorcado
        print(vidas_diccionario_visual[vidas])
        # Mostrar las letras separadas por un espacio 
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input ("\nEscoge una letra: ").upper()

        # Si la letra escogida por el usuario está en el abecedario 
        # y no está en el conjunto de letras que ya se han ingresado
        # Se añade la letra al conjunto de letras ingresadas.  
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            # Si la letra está en la palabra,
            # quitar la letra del conjunto de letras
            # pendientes por adivinar.
            # Si no está en la palabra, quitar una vida. 
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas = vidas -1
                print(f"\nTu letra, {letra_usuario} no está en la palabra.")
        # Si la letra escogida por el usuario ya fue ingresada. 
        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra.Por favor elige una letra nueva.")
        else:
            print("\nEsta letra no es válida.")

    # El juego llega a esta línea cuando se adivina todas las 
    # letras de la palabra o cuando se agotan las vidas del jugador.
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"¡Ahorcado! Perdiste. Lo lamento mucho. La palabra era: {palabra}")
    else:
        print(f"¡Excelente! ¡Adivinaste la palabra {palabra}!")  


ahorcado()