from meu_pacote import soma, potencia


def test_soma():
    assert soma(2, 3) == 5


def test_potencia():
    assert potencia(2, 3) == 8
