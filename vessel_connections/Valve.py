from typing import Set
from pydantic import BaseModel
from vessel_connections.Equipment import Equipment

class Valve(BaseModel):
    id: int
    is_open: bool = False
    connected_equipment: Set[Equipment] = set()

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False

    def add_connected_equipment(self, equipment: Equipment):
        self.connected_equipment.add(equipment)

    def __str__(self):
        return f"Valve {self.id} is {'open' if self.is_open else 'closed'}."