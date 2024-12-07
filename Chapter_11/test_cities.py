# test_cities.py
import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):
    
    def test_city_country(self):
        result = city_country('santiago', 'chile')
        self.assertEqual(result, 'Santiago, Chile')
    
    def test_city_country_population(self):
        result = city_country('santiago', 'chile', 5000000)
        self.assertEqual(result, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
    unittest.main()