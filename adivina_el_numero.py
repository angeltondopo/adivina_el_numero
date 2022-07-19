import random


def run():
    vidas = 6
    numero_aleatorio = random.randint(1, 100)

    print('Adivina el numero')
    print('Tienes ' + str(vidas) + ' vidas \u2764\uFE0F\u200D\U0001f525')
    numero_elegido = int(input('Elige un número del 1 al 100: '))

    while numero_elegido != numero_aleatorio:
        vidas -= 1
        if vidas == 0:
            print('\U0001f641 Perdiste \U0001f494')
            break
        elif numero_elegido < numero_aleatorio :
            print('Perdiste una vida \n' + '\u2764\uFE0F' * vidas)
            print('Busca un numero más grande')
        else:
            print('Perdiste una vida \n' + '\u2764\uFE0F' * vidas)
            print('Busca un numero más pequeño')
        numero_elegido = int(input('Elige otro número: '))
    if numero_aleatorio == numero_elegido:
        print('\U0001f603 ¡Ganaste! \U0001f3c6')


if __name__ == '__main__':
    run()