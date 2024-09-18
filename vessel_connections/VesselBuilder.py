from typing import Dict, List, Union
from Tank import Tank
from Pipe import Pipe
from Pump import Pump
from Sea import Sea
from Vessel import Vessel

VesselData = Dict[str, Union[str, Dict[str, List[str]]]]

class VesselBuilder:
    def __init__(self):
        self.name: str = ""
        self.version: str = ""
        self.tanks: Dict[str, Tank] = {}
        self.pipes: Dict[str, Pipe] = {}
        self.pumps: Dict[str, Pump] = {}
        self.sea_connections: Dict[str, Sea] = {}

    def load_from_data(self, data: VesselData) -> 'VesselBuilder':
        self.set_name(str(data.get('vessel', '')))
        self.set_version(str(data.get('version', '')))
        self._load_tanks(data.get('tanks', {}))
        self._load_pipes(data.get('pipes', {}))
        self._load_pumps(data.get('pumps', {}))
        self._load_sea_connections(data.get('sea', {}))
        return self

    def set_name(self, name: str) -> 'VesselBuilder':
        self.name = name
        return self

    def set_version(self, version: str) -> 'VesselBuilder':
        self.version = version
        return self

    def _load_tanks(self, tanks_data: Dict[str, List[str]]):
        for tank_id, valves in tanks_data.items():
            self.add_tank(Tank(id=str(tank_id), connected_valves=[str(v) for v in valves]))

    def _load_pipes(self, pipes_data: Dict[str, List[str]]):
        for pipe_id, valves in pipes_data.items():
            self.add_pipe(Pipe(id=str(pipe_id), connected_valves=[str(v) for v in valves]))

    def _load_pumps(self, pumps_data: Dict[str, List[str]]):
        for pump_id, valves in pumps_data.items():
            self.add_pump(Pump(id=str(pump_id), connected_valves=[str(v) for v in valves]))

    def _load_sea_connections(self, sea_data: Dict[str, List[str]]):
        for sea_type, valves in sea_data.items():
            self.add_sea_connection(Sea(id=str(sea_type), connected_valves=[str(v) for v in valves]))

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
            sea_connections=self.sea_connections
        )