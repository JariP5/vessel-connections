from abc import ABC, abstractmethod
from typing import List
from pydantic import BaseModel, field_validator

class Equipment(BaseModel, ABC):
    """Abstract base class for vessel equipment."""

    id: str
    connected_valves_ids: List[str] = []

    @field_validator('id')
    def validate_id(cls, v: str) -> str:
        """Validate that the equipment ID is not empty or only whitespace."""
        if not v.strip():
            raise ValueError('ID must not be empty or consist solely of whitespace.')
        return v

    @field_validator('connected_valves_ids')
    def check_connected_valves_ids(cls, v: List[str]) -> List[str]:
        """Ensure that the list of connected valves ids is not empty."""
        if not v:
            raise ValueError('Connected valves must not be empty')
        return v

    @abstractmethod
    def get_equipment_type(self) -> str:
        """Return the type of equipment (e.g., 'tank', 'pipe', 'pump')."""
        pass

    def get_connected_valves_ids(self) -> List[str]:
        return self.connected_valves_ids

    def is_connected_to_valve(self, valve_id: str) -> bool:
        return valve_id in self.connected_valves_ids

    def __str__(self) -> str:
        return (f'{self.get_equipment_type().capitalize()} {self.id} '
                f'connected to valves: {', '.join(self.connected_valves_ids)}')

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        if isinstance(other, Equipment):
            return (self.id == other.id and
                    self.get_equipment_type() == other.get_equipment_type())
        return False