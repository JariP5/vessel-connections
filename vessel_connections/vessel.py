from typing import Dict, List, Optional
from pydantic import BaseModel
from vessel_connections.Equipment import Equipment
from vessel_connections.Pump import Pump
from vessel_connections.Pipe import Pipe
from vessel_connections.Tank import Tank
from vessel_connections.Sea import Sea
from vessel_connections.Valve import Valve

class Vessel(BaseModel):
    name: str
    version: str
    tanks: Dict[str, Tank]
    pipes: Dict[str, Pipe]
    pumps: Dict[str, Pump]
    sea_connections: Dict[str, Sea]
    valves: Dict[str, Valve] = {}

    def get_equipment(self, eq_type: str, eq_id: str) -> Optional[Equipment]:
        """Get equipment based on type and ID."""
        equipment_dict = {
            'tank': self.tanks,
            'pipe': self.pipes,
            'pump': self.pumps,
            'sea': self.sea_connections,
        }

        if eq_type.lower() not in equipment_dict:
            print(f"Invalid equipment type: {eq_type}.")
            print(f"Must be tank, pipe, pump or sea.")
            return None

        return equipment_dict[eq_type.lower()].get(eq_id)

    def get_all_equipment(self) -> List[Equipment]:
        """Return a list of all equipment in the vessel."""
        return (list(self.tanks.values()) +
                list(self.pipes.values()) +
                list(self.pumps.values()) +
                list(self.sea_connections.values()))

    def open_valve(self, valve_id: str):
        if valve_id in self.valves:
            self.valves[valve_id].open()

    def close_valve(self, valve_id: str):
        if valve_id in self.valves:
            self.valves[valve_id].close()

    def close_all_valves(self):
        for valve in self.valves.values():
            valve.close()

    def is_valve_open(self, valve_id: str) -> bool:
        return self.valves[valve_id].is_open

    def __str__(self) -> str:
        """Return a string representation of the vessel."""
        return (f"Vessel: {self.name} (Version: {self.version})\n"
                f"Tanks: {len(self.tanks)}\n"
                f"Pipes: {len(self.pipes)}\n"
                f"Pumps: {len(self.pumps)}\n"
                f"Sea Connections: {len(self.sea_connections)}\n"
                f"Valves: {len(self.valves)}")