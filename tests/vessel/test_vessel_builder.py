import unittest
from unittest.mock import patch
from io import StringIO
from vessel_connections.vessel.vessel_builder import VesselBuilder
from vessel_connections.equipment.tank import Tank
from vessel_connections.equipment.pipe import Pipe
from vessel_connections.equipment.pump import Pump
from vessel_connections.equipment.sea import Sea
from vessel_connections.valve import Valve
from vessel_connections.vessel.vessel import Vessel

class TestVesselBuilder(unittest.TestCase):

    def setUp(self):
        self.builder = VesselBuilder()

    def test_set_name(self):
        self.builder.set_name("Test Vessel")
        self.assertEqual(self.builder.name, "Test Vessel")

    def test_set_version(self):
        self.builder.set_version("1.0")
        self.assertEqual(self.builder.version, "1.0")

    def test_load_tanks(self):
        data = {
            'tanks': {
                '001': ['001', '002'],
                '002': ['003']
            }
        }
        self.builder.load_from_data(data)
        self.assertIn('001', self.builder.tanks)
        self.assertIn('002', self.builder.tanks)
        self.assertEqual(len(self.builder.tanks['001'].connected_valves_ids), 2)
        self.assertEqual(self.builder.tanks['002'].connected_valves_ids, ['003'])

    def test_load_pipes(self):
        data = {
            'pipes': {
                '003': ['001'],
                '004': ['002', '003']
            }
        }
        self.builder.load_from_data(data)
        self.assertIn('003', self.builder.pipes)
        self.assertIn('004', self.builder.pipes)
        self.assertEqual(self.builder.pipes['003'].connected_valves_ids, ['001'])
        self.assertEqual(self.builder.pipes['004'].connected_valves_ids, ['002', '003'])

    def test_load_pumps(self):
        data = {
            'pumps': {
                '005': ['004'],
                '006': ['005']
            }
        }
        self.builder.load_from_data(data)
        self.assertIn('005', self.builder.pumps)
        self.assertIn('006', self.builder.pumps)
        self.assertEqual(self.builder.pumps['005'].connected_valves_ids, ['004'])
        self.assertEqual(self.builder.pumps['006'].connected_valves_ids, ['005'])

    def test_load_sea_connections(self):
        data = {
            'sea': {
                'overboard': ['001'],
                'seachest': ['002', '003']
            }
        }
        self.builder.load_from_data(data)
        self.assertIn('overboard', self.builder.sea_connections)
        self.assertIn('seachest', self.builder.sea_connections)
        self.assertEqual(self.builder.sea_connections['overboard'].connected_valves_ids, ['001'])
        self.assertEqual(self.builder.sea_connections['seachest'].connected_valves_ids, ['002', '003'])

    def test_load_valves(self):
        data = {
            'tanks': {
                '001': ['008'],
            },
            'pipes': {
                '002': ['009'],
            }
        }
        self.builder.load_from_data(data)
        self.assertIn('008', self.builder.valves)
        self.assertIn('009', self.builder.valves)
        self.assertIn(self.builder.tanks['001'], self.builder.valves['008'].connected_equipment)
        self.assertIn(self.builder.pipes['002'], self.builder.valves['009'].connected_equipment)

    def test_add_tank(self):
        tank = Tank(id='001', connected_valves_ids=['001'])
        self.builder.add_tank(tank)
        self.assertIn('001', self.builder.tanks)
        self.assertEqual(self.builder.tanks['001'].connected_valves_ids, ['001'])

    def test_add_pipe(self):
        pipe = Pipe(id='001', connected_valves_ids=['001'])
        self.builder.add_pipe(pipe)
        self.assertIn('001', self.builder.pipes)
        self.assertEqual(self.builder.pipes['001'].connected_valves_ids, ['001'])

    def test_add_pump(self):
        pump = Pump(id='001', connected_valves_ids=['001'])
        self.builder.add_pump(pump)
        self.assertIn('001', self.builder.pumps)
        self.assertEqual(self.builder.pumps['001'].connected_valves_ids, ['001'])

    def test_add_sea_connection(self):
        sea = Sea(id='overboard', connected_valves_ids=['001'])
        self.builder.add_sea_connection(sea)
        self.assertIn('overboard', self.builder.sea_connections)
        self.assertEqual(self.builder.sea_connections['overboard'].connected_valves_ids, ['001'])

    def test_build(self):
        self.builder.set_name("Test Vessel")
        self.builder.set_version("1.0")
        tank = Tank(id='001', connected_valves_ids=['001'])
        pipe = Pipe(id='002', connected_valves_ids=['002'])
        self.builder.add_tank(tank)
        self.builder.add_pipe(pipe)
        vessel = self.builder.build()
        self.assertIsInstance(vessel, Vessel)
        self.assertEqual(vessel.name, "Test Vessel")
        self.assertEqual(vessel.version, "1.0")
        self.assertIn('001', vessel.tanks)
        self.assertIn('002', vessel.pipes)

    def test_create_or_update_valve(self):
        valve_id = '001'
        equipment = Tank(id='001', connected_valves_ids=['001'])
        self.builder._create_or_update_valve(valve_id, equipment)
        self.assertIn(valve_id, self.builder.valves)
        self.assertIn(equipment, self.builder.valves[valve_id].connected_equipment)

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_or_update_valve_error(self, mock_stdout):
        valve_id = '001'
        # Force an exception in Valve creation
        with patch('vessel_connections.valve.Valve.__init__', side_effect=ValueError("Invalid ID")):
            self.builder._create_or_update_valve(valve_id, Tank(id='001', connected_valves_ids=['001']))
        output = mock_stdout.getvalue()
        self.assertIn("Error creating valve with ID '001'", output)
