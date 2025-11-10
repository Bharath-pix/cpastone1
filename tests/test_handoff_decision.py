import unittest
import math
from src.handoff_decision import calculate_rss, calculate_network_cost, evaluate_battery_life

# Mock classes for MobileNode and AccessPoint for testing purposes
class MockMobileNode:
    def __init__(self, position, battery_level):
        self.position = position
        self.battery_level = battery_level

class MockAccessPoint:
    def __init__(self, position, signal_strength, network_type, cost_per_mb):
        self.position = position
        self.signal_strength = signal_strength
        self.network_type = network_type
        self.cost_per_mb = cost_per_mb

class TestHandoffDecision(unittest.TestCase):

    def test_calculate_rss(self):
        mn = MockMobileNode(position=(0, 0), battery_level=100)
        ap = MockAccessPoint(position=(10, 0), signal_strength=100, network_type='Wi-Fi', cost_per_mb=0.1)
        # Expected RSS = 100 - 20 * log10(10) = 100 - 20 = 80
        self.assertAlmostEqual(calculate_rss(mn, ap), 80)

    def test_calculate_network_cost(self):
        ap = MockAccessPoint(position=(0, 0), signal_strength=100, network_type='Wi-Fi', cost_per_mb=0.1)
        service_requirements = {'bandwidth': 10}
        self.assertEqual(calculate_network_cost(ap, service_requirements), 1.0)

    def test_evaluate_battery_life(self):
        mn = MockMobileNode(position=(0, 0), battery_level=100)
        ap_wifi = MockAccessPoint(position=(0, 0), signal_strength=100, network_type='Wi-Fi', cost_per_mb=0.1)
        ap_cellular = MockAccessPoint(position=(0, 0), signal_strength=100, network_type='Cellular', cost_per_mb=0.5)
        self.assertEqual(evaluate_battery_life(mn, ap_wifi), 90)
        self.assertEqual(evaluate_battery_life(mn, ap_cellular), 70)

if __name__ == '__main__':
    unittest.main()
