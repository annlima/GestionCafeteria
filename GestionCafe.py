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
        if not self.nombre.isalpha() or not (2 <= len(self.nombre) <= 15):
            print("El nombre es inválido, solo caracteres alfanuméricos, y nombre de 2 a 15 letras")
            return False
        try:
            self.tamanos = [int(tamano) for tamano in tamanos_str]
        except ValueError:
            print("El tamaño no es válido, ingrese un número")
            return False
        if not (1 <= len(self.tamanos) <= 5) or not all(1 <= tam <= 48 for tam in self.tamanos):
            print("El tamaño está entre números menores a 1 o mayores a 48 o ingresó más de 5")
            return False
        if self.tamanos != sorted(self.tamanos):
            print("Los tamaños no están en orden ascendente")
            return False

        return True

def ValidarBebida(entrada):
    bebida = Cafe(entrada)
    return bebida.ProcesarEntrada()

def EntradasUsuario(entrada):
    esValida = ValidarBebida(entrada)
    print(f"La entrada '{entrada}' es {'válida' if esValida else 'inválida'}")
