import unittest
from src.validator import identificar_bandeira
from src.luhn import validar_luhn


class TestCartao(unittest.TestCase):
    def test_bandeiras(self):
        self.assertEqual(identificar_bandeira("4111111111111111"), "Visa")
        self.assertEqual(identificar_bandeira("5105105105105100"), "Mastercard")
    
    def test_american_express(self):
        self.assertEqual(identificar_bandeira("378282246310005"), "American Express")

    def test_discover(self):
        self.assertEqual(identificar_bandeira("6011111111111117"), "Discover")

    def test_numero_invalido(self):
        self.assertEqual(identificar_bandeira("0000000000000001"), "Bandeira desconhecida")
        self.assertFalse(validar_luhn("0000000000000001"))

    
    def test_luhn(self):
        self.assertTrue(validar_luhn("4111111111111111"))
        self.assertFalse(validar_luhn("1234567812345678"))

if __name__ == "__main__":
    unittest.main()
