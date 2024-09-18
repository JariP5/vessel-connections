from typing import Dict, List
from Equipment import Equipment
from Tank import Tank
from Pipe import Pipe
from Pump import Pump
from Sea import Sea

class Vessel:
    name: str
    version: str
    tanks: Dict[str, Tank]
    pipes: Dict[str, Pipe]
    pumps: Dict[str, Pump]
    sea_connections: Dict[str, Sea]

    def get_all_equipment(self) -> List[Equipment]:
        """Return a list of all equipment in the vessel."""
        return (list(self.tanks.values()) +
                list(self.pipes.values()) +
                list(self.pumps.values()) +
                list(self.sea_connections.values()))

    def __str__(self) -> str:
        """Return a string representation of the vessel."""
        return (f"Vessel: {self.name} (Version: {self.version})\n"
                f"Tanks: {len(self.tanks)}\n"
                f"Pipes: {len(self.pipes)}\n"
                f"Pumps: {len(self.pumps)}\n"
                f"Sea Connections: {len(self.sea_connections)}")