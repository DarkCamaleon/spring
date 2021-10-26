import random
import string

usuarios = ['alejandro', 'pedro', 'diego', 'jessica',
            'fran', 'amanda', 'eric', 'seba', 'emanuel', 'sergio']


def crear_cuenta():
    for i in usuarios:
        if type(i) != dict:
            usuarios.remove(i)
            print(f'te crearemos una cuenta {i}')
            i = {
                'nombre': i,
                'telefono': numero_telefono(),
                'contraseña': crear_contraseña()
            }
            usuarios.append(i)
            crear_cuenta()


def numero_telefono():
    num_telefono = input('ingrese numero telefonico debe ser de 8 digitos : ')
    while len(num_telefono) != 8:
        num_telefono = input(
            'ingrese numero telefonico debe ser de 8 digitos : ')
    return num_telefono


def crear_contraseña():
    numeros = string.digits
    minusculas = string.ascii_lowercase
    mayusculas = string.ascii_uppercase
    contraseña = ''
    for i in range(0, 2):
        numero_random = random.choice(numeros)
        minusculas_random = random.choice(minusculas)
        mayusculas_random = random.choice(mayusculas)
        contraseña += numero_random
        contraseña += minusculas_random
        contraseña += mayusculas_random
    return contraseña


crear_cuenta()
for i in usuarios:
    print(i)
