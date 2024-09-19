import unittest
from vessel_connections.valve import Valve
from vessel_connections.equipment.tank import Tank

class TestValve(unittest.TestCase):

    def setUp(self):
        self.valve = Valve(id='001')

    def test_create_valve(self):
        self.assertEqual(self.valve.id, '001')
        self.assertFalse(self.valve.is_open)
        self.assertEqual(len(self.valve.connected_equipment), 0)

    def test_open_and_close_valve(self):
        self.valve.open()
        self.assertTrue(self.valve.is_open)
        self.valve.close()
        self.assertFalse(self.valve.is_open)

    def test_add_connected_equipment(self):
        some_equipment = Tank(id=str('001'), connected_valves_ids=['001', '003'])
        self.valve.add_connected_equipment(some_equipment)
        self.assertIn(some_equipment, self.valve.connected_equipment)

    def test_str_method(self):
        self.assertEqual(str(self.valve), 'Valve 001 is closed.')

    def test_validate_id_empty(self):
        with self.assertRaises(ValueError):
            Valve(id='')
