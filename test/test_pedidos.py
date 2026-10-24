def calcular_total(precio, cantidad):
    return precio * cantidad


def test_calcular_total():
    assert calcular_total(25, 3) == 75
    assert calcular_total(10, 2) == 20
    assert calcular_total(50, 1) == 50


test_calcular_total()
print("Todas las pruebas pasaron correctamente")