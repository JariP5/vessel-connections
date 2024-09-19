import unittest
from unittest.mock import patch
from io import StringIO
from vessel_connections.equipment.tank import Tank
from vessel_connections.equipment.pipe import Pipe
from vessel_connections.equipment.pump import Pump
from vessel_connections.equipment.sea import Sea
from vessel_connections.valve import Valve
from vessel_connections.vessel.vessel import Vessel


class TestVessel(unittest.TestCase):

    def setUp(self):
        self.tank1 = Tank(id="001", connected_valves_ids=["001", "002"])
        self.tank2 = Tank(id="002", connected_valves_ids=["003", "004"])
        self.pipe1 = Pipe(id="001", connected_valves_ids=["005"])
        self.pump1 = Pump(id="01", connected_valves_ids=["006"])
        self.sea1 = Sea(id="overboard", connected_valves_ids=["007"])
        self.valve1 = Valve(id="001", is_open=False)
        self.valve2 = Valve(id="002", is_open=False)

        self.vessel = Vessel(
            name="Test Vessel",
            version="0.0.1",
            tanks={"001": self.tank1, "002": self.tank2},
            pipes={"001": self.pipe1},
            pumps={"01": self.pump1},
            sea_connections={"overboard": self.sea1},
            valves={"001": self.valve1, "002": self.valve2},
        )

    def test_get_equipment(self):
        equipment = self.vessel.get_equipment("tank", "001")
        self.assertEqual(equipment, self.tank1)

        equipment = self.vessel.get_equipment("pipe", "001")
        self.assertEqual(equipment, self.pipe1)

        equipment = self.vessel.get_equipment("pump", "01")
        self.assertEqual(equipment, self.pump1)

        equipment = self.vessel.get_equipment("sea", "overboard")
        self.assertEqual(equipment, self.sea1)

        # Test invalid equipment type
        equipment = self.vessel.get_equipment("invalid", "001")
        self.assertIsNone(equipment)

    def test_get_all_equipment(self):
        all_equipment = self.vessel.get_all_equipment()
        self.assertIn(self.tank1, all_equipment)
        self.assertIn(self.pipe1, all_equipment)
        self.assertIn(self.pump1, all_equipment)
        self.assertIn(self.sea1, all_equipment)

    def test_open_valve(self):
        self.vessel.open_valve("001")
        self.assertTrue(self.valve1.is_open)

    def test_close_valve(self):
        self.valve1.is_open = True
        self.vessel.close_valve("001")
        self.assertFalse(self.valve1.is_open)

    def test_set_only_open_valves(self):
        self.vessel.set_only_open_valves(["001"])
        self.assertTrue(self.valve1.is_open)
        self.assertFalse(self.valve2.is_open)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_open_valves(self, mock_stdout):
        self.valve1.is_open = True
        self.vessel.print_open_valves()
        output = mock_stdout.getvalue()
        self.assertIn("Open valves: 001", output)

        self.valve1.is_open = False
        self.vessel.print_open_valves()
        output = mock_stdout.getvalue()
        self.assertIn("No valves are currently open.", output)

    def test_close_all_valves(self):
        self.valve1.is_open = True
        self.valve2.is_open = True
        self.vessel.close_all_valves()
        self.assertFalse(self.valve1.is_open)
        self.assertFalse(self.valve2.is_open)

    def test_str_representation(self):
        vessel_str = str(self.vessel)
        self.assertIn("Vessel: Test Vessel", vessel_str)
        self.assertIn("Tanks: 2", vessel_str)
        self.assertIn("Pipes: 1", vessel_str)
        self.assertIn("Pumps: 1", vessel_str)
        self.assertIn("Sea Connections: 1", vessel_str)
        self.assertIn("Valves: 2", vessel_str)