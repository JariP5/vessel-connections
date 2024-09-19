from typing import Dict, List, Optional
from pydantic import BaseModel
from vessel_connections.equipment.Equipment import Equipment
from vessel_connections.equipment.Pump import Pump
from vessel_connections.equipment.Pipe import Pipe
from vessel_connections.equipment.Tank import Tank
from vessel_connections.equipment.Sea import Sea
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
        else:
            print(f"Valve with id {valve_id} was not found and could not be opened.")

    def close_valve(self, valve_id: str):
        if valve_id in self.valves:
            self.valves[valve_id].close()
        else:
            print(f"Valve with id {valve_id} was not found and could not be closed.")

    def close_all_valves(self):
        for valve in self.valves.values():
            valve.close()

    def set_only_open_valves(self, valve_ids: List[str]):
        """Open valves specified in the list and close all others."""
        for valve_id, valve in self.valves.items():
            if valve_id in valve_ids:
                valve.open()
            else:
                valve.close()

    def is_valve_open(self, valve_id: str) -> bool:
        return self.valves[valve_id].is_open

    def print_open_valves(self):
        """Print all open valves."""
        open_valves_ids = [valve.id for valve in self.valves.values() if valve.is_open]

        if open_valves_ids:
            open_valves_str = ', '.join(open_valves_ids)  # Join IDs with comma and space
            print(f"Open valves: {open_valves_str}\n")
        else:
            print("No valves are currently open.\n")

    def __str__(self) -> str:
        """Return a string representation of the vessel."""
        return (f"Vessel: {self.name} (Version: {self.version})\n"
                f"Tanks: {len(self.tanks)}\n"
                f"Pipes: {len(self.pipes)}\n"
                f"Pumps: {len(self.pumps)}\n"
                f"Sea Connections: {len(self.sea_connections)}\n"
                f"Valves: {len(self.valves)}\n")