import unittest
from vessel_connections.equipment.pipe import Pipe

class TestPipe(unittest.TestCase):

    def setUp(self):
        self.pipe = Pipe(id='001', connected_valves_ids=['002', '003'])

    def test_get_equipment_type(self):
        self.assertEqual(self.pipe.get_equipment_type(), 'pipe')

    def test_str_method(self):
        self.assertEqual(str(self.pipe), 'Pipe 001 connected to valves: 002, 003')

    def test_is_connected_to_valve(self):
        self.assertTrue(self.pipe.is_connected_to_valve('002'))
        self.assertFalse(self.pipe.is_connected_to_valve('999'))

    def test_equality(self):
        other_pipe = Pipe(id='001', connected_valves_ids=['002', '003'])
        self.assertEqual(self.pipe, other_pipe)

if __name__ == '__main__':
    unittest.main()
