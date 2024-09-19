from typing import Set
from pydantic import BaseModel, field_validator
from vessel_connections.Equipment import Equipment

class Valve(BaseModel):
    id: str
    is_open: bool = False
    connected_equipment: Set[Equipment] = set()

    @field_validator('id')
    def validate_id(cls, v: str) -> str:
        """Validate that the equipment ID is not empty or only whitespace."""
        if not v.strip():  # Checks if the string is empty or only contains whitespace
            raise ValueError('ID must not be empty or consist solely of whitespace.')
        return v

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False

    def add_connected_equipment(self, equipment: Equipment):
        self.connected_equipment.add(equipment)

    def __str__(self):
        return f"Valve {self.id} is {'open' if self.is_open else 'closed'}."