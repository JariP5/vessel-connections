import unittest
from pydantic import ValidationError
from vessel_connections.equipment.sea import Sea

class TestSea(unittest.TestCase):

    def setUp(self):
        self.sea_overboard = Sea(id='overboard', connected_valves_ids=['001', '003'])
        self.sea_seachest = Sea(id='seachest', connected_valves_ids=['002', '004'])

    def test_get_equipment_type(self):
        self.assertEqual(self.sea_overboard.get_equipment_type(), 'sea')
        self.assertEqual(self.sea_seachest.get_equipment_type(), 'sea')

    def test_str_method(self):
        self.assertEqual(str(self.sea_overboard), 'Sea overboard connected to valves: 001, 003')
        self.assertEqual(str(self.sea_seachest), 'Sea seachest connected to valves: 002, 004')

    def test_is_connected_to_valve(self):
        self.assertTrue(self.sea_overboard.is_connected_to_valve('001'))
        self.assertFalse(self.sea_overboard.is_connected_to_valve('999'))

    def test_invalid_sea_id(self):
        with self.assertRaises(ValidationError):
            Sea(id='invalid_id', connected_valves_ids=['001', '002'])

    def test_equality(self):
        other_sea = Sea(id='overboard', connected_valves_ids=['001', '003'])
        self.assertEqual(self.sea_overboard, other_sea)
