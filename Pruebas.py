import pytest
from GestionCafe import Cafe

@pytest.mark.parametrize("entrada,esperado", [
    # 1. Nombres con mayúsculas y minúsculas
    ("CafeConLeche,2,3", True),
    # 2. Límites de tamaño
    ("Cafe,1,48", True),
    # 3. Tamaños repetidos
    ("Cafe,2,2,3", False),
    # 4. Un solo tamaño
    ("Cafe,10", True),
    # 5. Orden descendente
    ("Cafe,4,3,2", False),
    # 6. Caracteres especiales en el nombre
    ("Café,3,4", False),
    # 7 - 8. Longitud de nombre en límites
    ("Ca,3,4", True),
    ("Cafecitodemasiadolargo,3", False),
    # 9 - 10. Cadena vacía o solo comas
    (",,,", False),
    ("", False),
    # 11. Caracteres especiales o espacios en los tamaños
    ("Cafe,3, 4,a", False),
    # 12 - 13. Casos adicionales de nombres válidos/invalídos
    ("CaféConEspacio, 5,10", False),  # Espacio en el nombre
    ("123Cafe,5,10", False),  # Números en el nombre
    # 14 - 16. Casos adicionales de tamaños
    ("Cafe,0,5", False),  # Tamaño fuera de rango inferior
    ("Cafe,49", False),  # Tamaño fuera de rango superior
    ("Cafe,1,2,3,4,5,6", False)  # Más de 5 tamaños
])
# 17
def test_validacion_bebida(entrada, esperado):
    assert Cafe(entrada).ProcesarEntrada() == esperado
# 18
def test_espacios_y_comas_extra():
    entrada = "Cafe , 1 , 2 , 3"
    assert Cafe(entrada).ProcesarEntrada() == True, "Debe manejar espacios extra correctamente"

