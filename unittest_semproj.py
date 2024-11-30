import unittest
from semproj_acp import SoilAnalysis 

class TestSoilAnalysis(unittest.TestCase):

    def setUp(self):
        # Setup a default instance for testing
        self.soil = SoilAnalysis(soil_type='Clay', soil_bearing_capacity=150, depth_of_soil_layer=5, water_table_depth=3)

    def test_soil_type_info(self):
        # Test soil type info
        self.assertEqual(self.soil.soil_type_info(), "Clay soils are cohesive, sticky, and often have poor drainage.")
        self.soil.soil_type = "Sand"
        self.assertEqual(self.soil.soil_type_info(), "Sand soils are loose, non-cohesive, and drain quickly.")
        self.soil.soil_type = "Unknown"
        self.assertEqual(self.soil.soil_type_info(), "Unknown soil type")

    def test_check_soil_bearing_capacity(self):
        # Test soil bearing capacity classification
        self.assertEqual(self.soil.check_soil_bearing_capacity(), "Medium soil bearing capacity")
        self.soil.soil_bearing_capacity = 50
        self.assertEqual(self.soil.check_soil_bearing_capacity(), "Low soil bearing capacity")
        self.soil.soil_bearing_capacity = 400
        self.assertEqual(self.soil.check_soil_bearing_capacity(), "High soil bearing capacity")

    def test_calculate_soil_bearing_capacity(self):
        # Test calculation of soil bearing capacity
        self.assertAlmostEqual(self.soil.calculate_soil_bearing_capacity(), 300.0)
        self.soil.depth_of_soil_layer = 10
        self.assertAlmostEqual(self.soil.calculate_soil_bearing_capacity(), 600.0)

    def test_calculate_settlement(self):
        # Test calculation of settlement
        self.assertAlmostEqual(self.soil.calculate_settlement(), 1.6483516483516482e-05)

    def test_calculate_lateral_earth_pressure(self):
        # Test lateral earth pressure calculation
        lateral_pressure = self.soil.calculate_lateral_earth_pressure()
        self.assertGreaterEqual(lateral_pressure, 0)
        self.assertLessEqual(lateral_pressure, 1)

    def test_water_table_effect(self):
        # Test water table depth effect
        self.assertEqual(self.soil.water_table_effect(), "Water table depth is adequate for construction.")
        self.soil.water_table_depth = 1.5
        self.assertEqual(self.soil.water_table_effect(), "Water table is too high. This may reduce the bearing capacity significantly.")

if __name__ == '__main__':
    unittest.main()