import re

class Cafe:
    def __init__(self, entrada):
        self.entrada = entrada
        self.nombre = ""
        self.tamanos = []

    def ProcesarEntrada(self):
        partes = self.entrada.replace(" ", "").split(",")
        if len(partes) < 2:
            print("No ingresó los valores adecuados")
            return False

        self.nombre, tamanos_str = partes[0], partes[1:]

        if not re.match("^[A-Za-z]+$", self.nombre):
            print("El nombre es inválido, debe contener solo caracteres alfabéticos sin caracteres especiales")
            return False

        if not (2 <= len(self.nombre) <= 15):
            print("La longitud del nombre debe ser de 2 a 15 caracteres")
            return False

        try:
            tamanos = [int(tamano) for tamano in tamanos_str]
        except ValueError:
            print("Uno o más tamaños especificados no son números válidos")
            return False

        if len(tamanos) != len(set(tamanos)):
            print("Los tamaños no deben repetirse")
            return False

        # Asegúrate de asignar tamanos a self.tamanos antes de la verificación de orden
        self.tamanos = tamanos

        if not (self.tamanos == sorted(self.tamanos)):
            print("Los tamaños deben estar en orden ascendente")
            return False

        if not (1 <= len(self.tamanos) <= 5):
            print("Debe ingresar entre 1 y 5 tamaños")
            return False

        if not all(1 <= tam <= 48 for tam in self.tamanos):
            print("Todos los tamaños deben estar en el rango de 1 a 48")
            return False

        return True


def ValidarBebida(entrada):
    bebida = Cafe(entrada)
    return bebida.ProcesarEntrada()

def EntradasUsuario(entrada):
    esValida = ValidarBebida(entrada)
    print(f"La entrada '{entrada}' es {'válida' if esValida else 'inválida'}")
