""" Administrador de clientes """
import re

clients = []

# añadimos mock data
# objectos simulador en programación orientada a objectos

marta = {'nombre':'Marta','apellido':'Pérez','dni':'15J'}
clients.append(marta)

# no hace falta crear la variable
# deben tener las mismas claves 
# eso es muy importante
clients.append({'nombre':'Manolo','apellido':'López','dni':'48H'})
clients.append({'nombre':'Ana','apellido':'García','dni':'28Z'})

if __name__ == '__main__':
	print(clients)


def show(client):
    print(f"{client['dni']}: {client['nombre']} {client['apellido']}")


def show_all():
    for client in clients:
        show(client)

def find():

    dni = input("Introduce el DNI del cliente\n> ")

    for client in clients:
        if client['dni'] == dni:
            show(client)
            return client

    print("No se ha encontrado ningún cliente con ese DNI")


def is_valid(dni):
    """
    >>> is_valid('48H')  # No válido, en uso
    False

    >>> is_valid('X82')  # No válido, incorrecto
    False

    >>> is_valid('21A')  # Válido
    True

    """

    # Comprueba que el dni empieza con un patrón
    if not re.match('[0-9]{2}[A-Z]', dni):
        return False

    # Comprueba que el dni no esté repetido
    for client in clients:
        if client['dni'] == dni:
            return False

    return True

if __name__ == "__main__":
    import doctest
    # doctest.testmod()
    # Añade la capaidad a este fichero (o a este script manager )
    # de ejecutar test en el doctest 

    # y para ejercutarlo debe ser:
    # python manager.py -v