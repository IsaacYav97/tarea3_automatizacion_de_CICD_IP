import pytest
from app import sumar, restar, multiplicar, dividir, potencia, raiz_cuadrada, modulo, logaritmo

# ── Suma ──────────────────────────────────────────────
def test_sumar_positivos():
    assert sumar(3, 5) == 8

def test_sumar_negativos():
    assert sumar(-2, -4) == -6

def test_sumar_con_cero():
    assert sumar(0, 7) == 7

# ── Resta ─────────────────────────────────────────────
def test_restar_positivos():
    assert restar(10, 4) == 6

def test_restar_resultado_negativo():
    assert restar(2, 9) == -7

# ── Multiplicación ────────────────────────────────────
def test_multiplicar_positivos():
    assert multiplicar(3, 4) == 12

def test_multiplicar_por_cero():
    assert multiplicar(5, 0) == 0

def test_multiplicar_negativos():
    assert multiplicar(-3, -3) == 9

# ── División ──────────────────────────────────────────
def test_dividir_exacta():
    assert dividir(10, 2) == 5

def test_dividir_con_decimal():
    assert dividir(7, 2) == 3.5

def test_dividir_entre_cero():
    with pytest.raises(ValueError, match="No se puede dividir entre cero"):
        dividir(5, 0)

# ── Potencia ──────────────────────────────────────────
def test_potencia_positiva():
    assert potencia(2, 8) == 256

def test_potencia_cero():
    assert potencia(5, 0) == 1

def test_potencia_negativa():
    assert potencia(2, -1) == 0.5

# ── Raíz cuadrada ─────────────────────────────────────
def test_raiz_cuadrada_exacta():
    assert raiz_cuadrada(25) == 5.0

def test_raiz_cuadrada_cero():
    assert raiz_cuadrada(0) == 0.0

def test_raiz_cuadrada_negativa():
    with pytest.raises(ValueError, match="número negativo"):
        raiz_cuadrada(-4)

# ── Módulo ────────────────────────────────────────────
def test_modulo_normal():
    assert modulo(10, 3) == 1

def test_modulo_exacto():
    assert modulo(9, 3) == 0

def test_modulo_entre_cero():
    with pytest.raises(ValueError, match="divisor cero"):
        modulo(5, 0)

# ── Logaritmo ─────────────────────────────────────────
def test_logaritmo_base10():
    assert logaritmo(100) == pytest.approx(2.0)

def test_logaritmo_numero_negativo():
    with pytest.raises(ValueError, match="números positivos"):
        logaritmo(-1)

def test_logaritmo_cero():
    with pytest.raises(ValueError, match="números positivos"):
        logaritmo(0)
