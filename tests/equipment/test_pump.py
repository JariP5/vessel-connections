import unittest
from vessel_connections.equipment.pump import Pump

class TestPump(unittest.TestCase):

    def setUp(self):
        self.pump = Pump(id='01', connected_valves_ids=['001', '003'])

    def test_get_equipment_type(self):
        self.assertEqual(self.pump.get_equipment_type(), 'pump')

    def test_str_method(self):
        self.assertEqual(str(self.pump), 'Pump 01 connected to valves: 001, 003')

    def test_is_connected_to_valve(self):
        self.assertTrue(self.pump.is_connected_to_valve('001'))
        self.assertFalse(self.pump.is_connected_to_valve('999'))

    def test_equality(self):
        other_pump = Pump(id='01', connected_valves_ids=['001', '003'])
        self.assertEqual(self.pump, other_pump)
