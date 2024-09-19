import unittest
from vessel_connections.equipment.tank import Tank

class TestTank(unittest.TestCase):

    def setUp(self):
        self.tank = Tank(id='001', connected_valves_ids=['001', '003'])

    def test_get_equipment_type(self):
        self.assertEqual(self.tank.get_equipment_type(), 'tank')

    def test_str_method(self):
        self.assertEqual(str(self.tank), 'Tank 001 connected to valves: 001, 003')

    def test_is_connected_to_valve(self):
        self.assertTrue(self.tank.is_connected_to_valve('001'))
        self.assertFalse(self.tank.is_connected_to_valve('999'))

    def test_equality(self):
        other_tank = Tank(id='001', connected_valves_ids=['001', '003'])
        self.assertEqual(self.tank, other_tank)
