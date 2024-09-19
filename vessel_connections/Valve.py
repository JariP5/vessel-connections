from typing import Set
from pydantic import BaseModel, field_validator
from vessel_connections.equipment.Equipment import Equipment

class Valve(BaseModel):
    id: str
    is_open: bool = False
    connected_equipment: Set[Equipment] = set()

    @field_validator('id')
    def validate_id(cls, v: str) -> str:
        if not v.strip():
            raise ValueError('ID must not be empty or consist solely of whitespace.')
        return v

    def open(self) -> None:
        self.is_open = True

    def close(self) -> None:
        self.is_open = False

    def add_connected_equipment(self, equipment: Equipment) -> None:
        self.connected_equipment.add(equipment)

    def __str__(self) -> str:
        return f'Valve {self.id} is {'open' if self.is_open else 'closed'}.'
