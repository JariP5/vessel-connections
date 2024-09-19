from typing import Dict, List, Union
from pydantic import BaseModel
from vessel_connections.equipment.equipment import Equipment
from vessel_connections.equipment.tank import Tank
from vessel_connections.equipment.pipe import Pipe
from vessel_connections.equipment.pump import Pump
from vessel_connections.equipment.sea import Sea
from vessel_connections.valve import Valve
from vessel_connections.vessel.vessel import Vessel

VesselData = Dict[str, Union[str, Dict[str, List[str]]]]

class VesselBuilder(BaseModel):
    name: str = ""
    version: str = ""
    tanks: Dict[str, Tank] = {}
    pipes: Dict[str, Pipe] = {}
    pumps: Dict[str, Pump] = {}
    sea_connections: Dict[str, Sea] = {}
    valves: Dict[str, Valve] = {}

    def load_from_data(self, data: VesselData) -> 'VesselBuilder':
        self.set_name(str(data.get('vessel', '')))
        self.set_version(str(data.get('version', '')))
        self._load_tanks(data.get('tanks', {}))
        self._load_pipes(data.get('pipes', {}))
        self._load_pumps(data.get('pumps', {}))
        self._load_sea_connections(data.get('sea', {}))
        self._load_valves()
        return self

    def set_name(self, name: str) -> 'VesselBuilder':
        self.name = name
        return self

    def set_version(self, version: str) -> 'VesselBuilder':
        self.version = version
        return self

    def _load_tanks(self, tanks_data: Dict[str, List[str]]):
        for tank_id, valves in tanks_data.items():
            try:
                tank = Tank(id=str(tank_id), connected_valves_ids=[str(v) for v in valves])
                self.add_tank(tank)
            except ValueError as e:
                print(f"Error creating tank with ID '{tank_id}': {e}")

    def _load_pipes(self, pipes_data: Dict[str, List[str]]):
        for pipe_id, valves in pipes_data.items():
            try:
                pipe = Pipe(id=str(pipe_id), connected_valves_ids=[str(v) for v in valves])
                self.add_pipe(pipe)
            except ValueError as e:
                print(f"Error creating pipe with ID '{pipe_id}': {e}")

    def _load_pumps(self, pumps_data: Dict[str, List[str]]):
        for pump_id, valves in pumps_data.items():
            try:
                pump = Pump(id=str(pump_id), connected_valves_ids=[str(v) for v in valves])
                self.add_pump(pump)
            except ValueError as e:
                print(f"Error creating pump with ID '{pump_id}': {e}")

    def _load_sea_connections(self, sea_data: Dict[str, List[str]]):
        for sea_type, valves in sea_data.items():
            try:
                sea = Sea(id=str(sea_type), connected_valves_ids=[str(v) for v in valves])
                self.add_sea_connection(sea)
            except ValueError as e:
                print(f"Error creating sea with ID '{sea_type}': {e}")

    def _load_valves(self):
        """Load valves and associate them with equipment."""
        for equipment_dict in [self.tanks, self.pipes, self.pumps, self.sea_connections]:
            for equipment in equipment_dict.values():
                for valve_id in equipment.connected_valves_ids:
                    self._create_or_update_valve(valve_id, equipment)

    def _create_or_update_valve(self, valve_id: str, equipment: Equipment):
        if valve_id not in self.valves:
            try:
                valve = Valve(id=valve_id)
                self.valves[valve_id] = valve
            except ValueError as e:
                print(f"Error creating valve with ID '{valve_id}': {e}")
                return
        self.valves[valve_id].add_connected_equipment(equipment)

    def add_tank(self, tank: Tank) -> 'VesselBuilder':
        self.tanks[tank.id] = tank
        return self

    def add_pipe(self, pipe: Pipe) -> 'VesselBuilder':
        self.pipes[pipe.id] = pipe
        return self

    def add_pump(self, pump: Pump) -> 'VesselBuilder':
        self.pumps[pump.id] = pump
        return self

    def add_sea_connection(self, sea: Sea) -> 'VesselBuilder':
        self.sea_connections[sea.id] = sea
        return self

    def build(self) -> Vessel:
        return Vessel(
            name=self.name,
            version=self.version,
            tanks=self.tanks,
            pipes=self.pipes,
            pumps=self.pumps,
            sea_connections=self.sea_connections,
            valves=self.valves
        )