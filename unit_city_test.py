import unittest
from city_function import city_function 

class Test(unittest.TestCase):

	def test_city_country(self):
		city_function_equal = city_function('santiago', 'chile')

		self.assertEqual(city_function_equal,'Santiago, Chile' ) 


	def test_city_country_population(self):
		test_city_country_population = city_function('santiago', 'chile', '5000000')

		self.assertEqual(test_city_country_population, 'Santiago, Chile 5000000')

unittest.main()