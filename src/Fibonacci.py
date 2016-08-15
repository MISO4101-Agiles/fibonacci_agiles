from pip._vendor.distlib.compat import raw_input

_author_ = 'Luis Sebastian Talero'


class Fibonacci:
    def __init__(self):
        pass

    print(' _______  __  .______     ______   .__   __.      ___       ______   ______  __\n'
          '|   ____||  | |   _  \   /  __  \  |  \ |  |     /   \     /      | /      ||  |\n'
          '|  |__   |  | |  |_)  | |  |  |  | |   \|  |    /  ^  \   |  ,----|   ----| |  |\n'
          '|   __|  |  | |   _  <  |  |  |  | |  . `  |   /  /_\  \  |  |     |  |     |  |\n'
          '|  |     |  | |  |_)  | |  `--   | |  |\   |  /  _____  \ |  `----.|  `----.|  |\n'
          '|__|     |__| |______/   \______/  |__| \__| /__/     \__\ \______| \______||__|\n')
    try:
        number = int(raw_input('Ingresa un numero: '))
        if number < 0:
            print('El numero debe ser positivo')
        elif number == 0:
            print(number)
        elif number == 1:
            print(0)
            print(1)
        else:
            print(0)
            print(1)
            anterior = 0
            actual = 1
            while 0 <= actual <= number:
                aux = actual + anterior
                anterior = actual
                actual = aux
                if actual <= number:
                    print(actual)
    except ValueError:
        print('Debes ingresar un numero!')
