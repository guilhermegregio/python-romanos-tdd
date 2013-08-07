from unittest import TestCase
import romanos

class ConversorNumerosParaRomanos(TestCase):

	def test_deve_converter_numero_1_2_e_3(self):
		self.assertEqual('I', romanos.toRomanos(1))
		self.assertEqual('II', romanos.toRomanos(2))
		self.assertEqual('III', romanos.toRomanos(3))

	def test_deve_converter_numero_4_e_9(self):
		self.assertEqual('IV', romanos.toRomanos(4))
		self.assertEqual('IX', romanos.toRomanos(9))

	def test_deve_converter_numero_5(self):
		self.assertEqual('V', romanos.toRomanos(5))

	def test_deve_converter_numero_6_7_e_8(self):
		self.assertEqual('VI', romanos.toRomanos(6))
		self.assertEqual('VII', romanos.toRomanos(7))
		self.assertEqual('VIII', romanos.toRomanos(8))

	def test_deve_converter_numero_10_20_e_30(self):
		self.assertEqual('X', romanos.toRomanos(10))
		self.assertEqual('XX', romanos.toRomanos(20))
		self.assertEqual('XXX', romanos.toRomanos(30))

	def test_deve_converter_numero_11_12_e_13(self):
		self.assertEqual('XI', romanos.toRomanos(11))
		self.assertEqual('XII', romanos.toRomanos(12))
		self.assertEqual('XIII', romanos.toRomanos(13))

	def test_deve_converter_numero_14_e_19(self):
		self.assertEqual('XIV', romanos.toRomanos(14))
		self.assertEqual('XIX', romanos.toRomanos(19))

	def test_deve_converter_numero_40(self):
		self.assertEqual('XL', romanos.toRomanos(40))

	def test_deve_converter_numero_50(self):
		self.assertEqual('L', romanos.toRomanos(50))

	def test_deve_converter_numero_90(self):
		self.assertEqual('XC', romanos.toRomanos(90))

	def test_deve_converter_numero_100(self):
		self.assertEqual('C', romanos.toRomanos(100))

	def test_deve_converter_numero_500(self):
		self.assertEqual('D', romanos.toRomanos(500))

	def test_deve_converter_numero_1000(self):
		self.assertEqual('M', romanos.toRomanos(1000))

	def test_deve_converter_numero_3999(self):
		self.assertEqual('MMMCMXCIX', romanos.toRomanos(3999))

