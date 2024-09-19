import unittest
from pydantic import ValidationError
from vessel_connections.equipment.equipment import Equipment

# Define a concrete subclass of Equipment for testing
class ConcreteEquipment(Equipment):

    def get_equipment_type(self) -> str:
        return 'test_equipment'

class TestEquipmentClass(unittest.TestCase):

    def setUp(self):
        self.equipment = ConcreteEquipment(id='099', connected_valves_ids=['001', '002'])

    def test_validate_id(self):
        # Valid ID should work
        valid_equipment = ConcreteEquipment(id='099', connected_valves_ids=['001'])
        self.assertEqual(valid_equipment.id, '099')

        # Invalid ID (empty) should raise ValidationError
        with self.assertRaises(ValidationError):
            ConcreteEquipment(id='', connected_valves_ids=['001'])

    def test_validate_connected_valves(self):
        valid_equipment = ConcreteEquipment(id='099', connected_valves_ids=['001'])
        self.assertEqual(valid_equipment.connected_valves_ids, ['001'])

        # Invalid (empty) connected_valves_ids should raise ValidationError
        with self.assertRaises(ValidationError):
            ConcreteEquipment(id='099', connected_valves_ids=[])

    def test_get_equipment_type(self):
        self.assertEqual(self.equipment.get_equipment_type(), 'test_equipment')

    def test_get_connected_valves_ids(self):
        self.assertEqual(self.equipment.get_connected_valves_ids(), ['001', '002'])

    def test_is_connected_to_valve(self):
        self.assertTrue(self.equipment.is_connected_to_valve('001'))
        self.assertFalse(self.equipment.is_connected_to_valve('999'))

    def test_str_method(self):
        self.assertEqual(str(self.equipment), 'Test_equipment 099 connected to valves: 001, 002')

    def test_hash(self):
        self.assertEqual(hash(self.equipment), hash('099'))

    def test_equality(self):
        other_equipment = ConcreteEquipment(id='099', connected_valves_ids=['001', '002'])
        self.assertEqual(self.equipment, other_equipment)

        different_equipment = ConcreteEquipment(id='T02', connected_valves_ids=['001'])
        self.assertNotEqual(self.equipment, different_equipment)
