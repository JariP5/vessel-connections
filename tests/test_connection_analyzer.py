import unittest
from unittest.mock import patch
from io import StringIO

from vessel_connections.connection_analyzer import ConnectionAnalyzer
from vessel_connections.equipment.tank import Tank
from vessel_connections.equipment.pump import Pump
from vessel_connections.valve import Valve
from vessel_connections.vessel.vessel import Vessel


class TestConnectionAnalyzer(unittest.TestCase):

    def setUp(self):
        # Create equipment instances
        self.pump1 = Pump(id='001', connected_valves_ids=['001'])
        self.pump2 = Pump(id='002', connected_valves_ids=['002'])
        self.tank1 = Tank(id='003', connected_valves_ids=['001'])

        # Create valves
        self.valve1 = Valve(id='001')
        self.valve1.connected_equipment = {self.pump1, self.tank1}
        self.valve1.is_open = True
        self.valve2 = Valve(id='002')
        self.valve2.connected_equipment = {self.pump2}
        self.valve2.is_open = True
        self.valve3 = Valve(id='003')
        self.valve3.connected_equipment = {self.pump1, self.pump2}
        self.valve3.is_open = False

        # Create vessel instance
        self.vessel = Vessel(
            name='Test Vessel',
            version='1.0',
            tanks={'003': self.tank1},
            pipes={},
            pumps={'001': self.pump1, '002': self.pump2},
            sea_connections={},
            valves={'001': self.valve1, '002': self.valve2, '003': self.valve3}
        )

        # Create ConnectionAnalyzer instance
        self.analyzer = ConnectionAnalyzer(vessel=self.vessel)

    def test_analyze_connections(self):
        connections = self.analyzer.analyze_connections()
        print(connections)
        self.assertEqual(len(connections), 2)
        self.assertEqual(connections[0], {self.pump1, self.tank1})
        self.assertEqual(connections[1], {self.pump2})

    def test_is_equipment_connected(self):
        self.assertTrue(
            self.analyzer.is_equipment_connected(
                'pump', '001', 'tank', '003'
            )
        )
        self.assertFalse(
            self.analyzer.is_equipment_connected(
                'pump', '001', 'pump', '002'
            )
        )
    @patch('sys.stdout', new_callable=StringIO)
    def test_print_connected_sets(self, mock_stdout):
        self.analyzer.print_connected_sets()
        output = mock_stdout.getvalue()
        expected_output = (
            'Connected equipment sets based on valve states:\n'
            'Set 1: Pump 001, Tank 003\n'
            'Set 2: Pump 002\n'
        )
        self.assertEqual(output, expected_output)
