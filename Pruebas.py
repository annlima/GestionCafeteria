import pytest
from GestionCafe import Cafe, EntradasUsuario

# Test para validar nombres de bebidas correctos e incorrectos
@pytest.mark.parametrize("entrada,esperado", [
    ("Cafe,1,2,3", True),  # Nombre y tamaños válidos
    ("C4,2,3", False),  # Nombre contiene caracteres no alfabéticos
    ("Te,49,50", False),  # Tamaño fuera de rango
    ("CafeLatte,2,1,3", False),  # Tamaños no en orden ascendente
    ("Expresso", False),  # Falta de tamaños
    ("CafeConLeche,1,2,3,4,5,6", False),  # Más de 5 tamaños
    ("C,1,2", False),  # Nombre demasiado corto
    ("CafeDemasiadoLargoDeNombre,1", False),  # Nombre demasiado largo
    ("Cafe, 1, 2, 3", True),  # Espacios que deben ser ignorados correctamente
])
def test_validacion_bebida(entrada, esperado):
    assert Cafe(entrada).ProcesarEntrada() == esperado

# Test para casos específicos como el manejo de espacios y comas
def test_espacios_y_comas_extra():
    entrada = "Cafe , 1 , 2 , 3"
    assert Cafe(entrada).ProcesarEntrada() == True, "Debe manejar espacios extra correctamente"

